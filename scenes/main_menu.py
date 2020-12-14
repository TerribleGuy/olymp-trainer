from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def process_logic(self):
        script = {
            'Начать': lambda: self.application.change_scene(self.application.MAIN_MENU_INDEX),
            'Добавить задачу': lambda: self.application.change_scene(self.application.ADD_TASK_INDEX),
            'Настройки': lambda: self.application.change_scene(self.application.MAIN_MENU_INDEX),
            'Выйти': lambda: self.application.exit_application()
        }
        self.application.process_actions(script)
