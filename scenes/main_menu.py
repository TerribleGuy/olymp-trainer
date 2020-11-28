from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def process_logic(self):
        script = {
            'Начать': lambda: self.application.change_scene(0),
            'Настройки': lambda: self.application.change_scene(1),
            'Выйти': lambda: self.application.exit_application()
        }
        self.application.process_actions(script)
