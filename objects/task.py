class Task:
    def __init__(self, id, description='-', href='-', tag='-'):
        self.id = id
        self.description = description
        self.href = href
        self.tag = tag

    def print(self):
        print('Task - {}'.format(self.id))
        print(self.description)
        print('Tag: {}\nHref: {}'.format(self.tag, self.href))
