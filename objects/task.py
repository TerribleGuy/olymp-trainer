class Task:
    def __init__(self, task_id, title, **kwargs):
        self.task_id = task_id
        self.title = title
        self.process_kwargs(kwargs)

    def process_kwargs(self, kwargs):
        settings = {'description': '-',
                    'href': '-',
                    'main_topics': [],
                    'topics': [],
                    'tags': []}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError('Task has no keyword {}'.format(kwarg))
        self.__dict__.update(settings)

    def print(self):
        print('Task - {}'.format(self.task_id))
        print(self.title)
        print('Tag: {}\nHref: {}'.format(self.tags, self.href))
