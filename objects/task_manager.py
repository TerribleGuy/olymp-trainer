from objects.task import Task
import json


class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    @staticmethod
    def encode_task(task):
        if isinstance(task, Task):
            return {
                '__task__': True,
                'id': task.task_id,
                'description': task.description,
                'href': task.href,
                'tags': task.tags
            }
        else:
            type_name = task.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

    @staticmethod
    def decode_task(dct):
        if '__task__' in dct:
            return Task(dct['id'], dct['description'], href=dct['href'], tags=dct['tags'])
        return dct

    def read_from_file(self) -> bool:
        try:
            file = open(self.filename, 'r')
        except FileNotFoundError:
            file = open(self.filename, 'w')
            json.dump([], file)
            file.close()
            return True
        try:
            self.tasks = json.load(file, object_hook=self.decode_task)
        except TypeError:
            self.tasks = []
            return False
        if not isinstance(self.tasks, list):
            self.tasks = []
            return False
        used_ids = set()
        for task in self.tasks:
            if not isinstance(task, Task) or (task.task_id in used_ids):
                self.tasks = []
                return False
            else:
                used_ids.add(task.task_id)
        return True

    def add_task(self, description, href, tags) -> bool:
        used_ids_line = [0] * 10000
        for task in self.tasks:
            used_ids_line[task.id] = 1
        new_id = -1
        for i in range(len(used_ids_line)):
            if not used_ids_line[i]:
                new_id = i
                break
        if new_id == -1:
            return False
        self.tasks.append(Task(new_id, description, href=href, tags=tags))
        self.write_to_file()
        return True

    def write_to_file(self) -> bool:
        try:
            file = open(self.filename, 'w')
        except IOError:
            return False
        json.dump(self.tasks, file, default=self.encode_task)
        file.close()
        return True

    def print_all(self):
        for task in self.tasks:
            task.print()
            print()
