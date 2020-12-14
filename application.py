from scenes import MainMenuScene, AddTaskScene
from objects.task_manager import TaskManager


class Application:
    MAIN_MENU_INDEX = 0
    ADD_TASK_INDEX = 1

    def __init__(self):
        self.task_manager = TaskManager('tasks/info.txt')
        print(self.task_manager.read_from_file())
        self.scenes = [MainMenuScene(self), AddTaskScene(self, self.task_manager)]
        self.current_scene = 0
        self.is_end = False

    def process_force_commands(self, command) -> bool:
        if isinstance(command, str):
            command = command.strip().split()
        if command[0] != '!':
            return False
        if len(command) > 1:
            if command[1] == 'exit':
                if len(command) > 2:
                    try:
                        self.change_scene(int(command[2]))
                        return True
                    except ValueError:
                        pass
                self.change_scene(self.MAIN_MENU_INDEX)
                return True
        return False

    @staticmethod
    def get_input_line(allowed=None, max_tries=0, retry_message='Неверная команда, попробуйте еще раз') -> str:
        if not (allowed is None) and not len(allowed):
            allowed = None
        if max_tries == 0:
            max_tries = 1000000000
        cur_try = 0
        while cur_try < max_tries:
            input_line = input().strip()
            if not len(input_line):
                continue
            if (allowed is None) or (input_line in allowed):
                return input_line
            if cur_try < max_tries - 1:
                print(retry_message)
            cur_try += 1
        return ''

    @staticmethod
    def get_input_commands(allowed=None, max_tries=0, retry_message='Неверная команда, попробуйте еще раз') -> list:
        if not (allowed is None) and not len(allowed):
            allowed = None
        if max_tries == 0:
            max_tries = 1000000000
        cur_try = 0
        while cur_try < max_tries:
            commands = input().strip().split()
            if not len(commands):
                continue
            if (allowed is None) or (commands[0] in allowed):
                return commands
            if cur_try < max_tries - 1:
                print(retry_message)
            cur_try += 1
        return []

    @staticmethod
    def action_choice(actions, choice_title='Выберите действие:', reprint_after=5) -> dict:
        allowed = []
        choice_message = choice_title + '\n'
        if reprint_after < 1:
            reprint_after = 1
        for i in range(len(actions)):
            allowed.append(str(actions[i]))
            allowed.append(str(i + 1))
            choice_message = choice_message + '{}. {}\n'.format(i + 1, actions[i])
        print(choice_message)
        action_index = -1
        action_str = ''
        while action_index == -1:
            input_line = Application.get_input_line(allowed=allowed, max_tries=reprint_after)
            if input_line != '':
                try:
                    action_index = int(input_line) - 1
                    action_str = actions[action_index]
                except ValueError:
                    try:
                        action_index = actions.index(input_line)
                        action_str = input_line
                    except ValueError:
                        action_index = -1
                        action_str = ''
            if action_index == -1:
                print()
                print(choice_message)
        return {
            'index': action_index,
            'str': action_str
        }

    @staticmethod
    def process_actions(actions_dict, choice_title='Выберите действие:', reprint_after=5):
        actions_list = []
        for key in actions_dict.keys():
            actions_list.append(key)
        selected_action = Application.action_choice(actions_list, choice_title=choice_title, reprint_after=reprint_after)
        actions_dict[selected_action['str']]()

    def change_scene(self, index):
        self.current_scene = index

    def exit_application(self):
        self.is_end = True

    def main_loop(self):
        while not self.is_end:
            self.scenes[self.current_scene].process_logic()
