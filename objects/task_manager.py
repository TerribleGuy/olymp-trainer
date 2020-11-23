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
                'id': task.id,
                'description': task.description,
                'href': task.href,
                'tag': task.tag
            }
        else:
            type_name = task.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

    @staticmethod
    def decode_task(dct):
        if '__task__' in dct:
            return Task(dct['id'], dct['description'], dct['href'], dct['tag'])
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
        for task in self.tasks:
            if not isinstance(task, Task):
                self.tasks = []
                return False
        return True

    def add_task(self, task):
        self.tasks.append(task)

    def write_to_file(self):
        file = open(self.filename, 'w')
        json.dump(self.tasks, file, default=self.encode_task)
        file.close()

    def print_all(self):
        for task in self.tasks:
            task.print()
            print()
