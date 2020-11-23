from objects.application import Application


class BaseScene:
    def __init__(self, application):
        self.application = application

    def main_loop(self):
        pass
