class BaseScene:
    def __init__(self, application) -> None:
        self.application = application

    def on_activate(self) -> None:
        pass

    def process_logic(self) -> None:
        pass

    def on_deactivate(self) -> None:
        pass
