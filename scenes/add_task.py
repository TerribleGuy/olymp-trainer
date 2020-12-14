from scenes.base_scene import BaseScene


class AddTaskScene(BaseScene):
    def __init__(self, application, task_manager):
        self.task_manager = task_manager
        super().__init__(application)

    def process_logic(self) -> None:
        retry_msg = 'Введите {} или ! exit, чтобы выйти'
        print("Введите описание задачи:")
        description = self.application.get_input_line(retry_message=retry_msg.format('описание задачи'))
        if self.application.process_force_commands(description):
            return
        print('Введите ссылку на задачу:')
        href = self.application.get_input_line(retry_message=retry_msg.format('ссылку на задачу'))
        if self.application.process_force_commands(href):
            return
        print('Введите теги задачи:')
        tags = self.application.get_input_commands(retry_message=retry_msg.format('теги задачи'))
        if self.application.process_force_commands(tags):
            return
        if self.task_manager.add_task(description, href, tags):
            print('Успешно добавлено')
        else:
            print('Ошибка')
        self.task_manager.print_all()
        self.application.change_scene(self.application.MAIN_MENU_INDEX)
