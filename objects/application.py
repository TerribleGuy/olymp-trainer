from scenes.main_menu import MainMenu


class Application:
    def __init__(self):
        self.scenes = []
        self.scenes.append(MainMenu(self))
        self.current_scene = 0
        self.is_end = False

    @staticmethod
    def get_user_input(allowed=None, allowed_lines=False, max_tries=0, retry_message='Неверная команда, попробуйте еще раз') -> list:
        if not (allowed is None) and not len(allowed):
            allowed = None
        if max_tries == 0:
            max_tries = 1000000000
        for i in range(max_tries):
            command = input().strip()
            if len(command):
                if allowed is None:
                    if allowed_lines:
                        return [command]
                    else:
                        return command.split()
                else:
                    if allowed_lines:
                        if command in allowed:
                            return [command]
                    else:
                        command = command.split()
                        if command[0] in allowed:
                            return command
            if i < max_tries - 1:
                print(retry_message)
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
            commands_list = Application.get_user_input(allowed=allowed, allowed_lines=True, max_tries=reprint_after)
            if len(commands_list):
                try:
                     action_index = int(commands_list[0]) - 1
                     action_str = actions[action_index]
                except ValueError:
                    try:
                        action_index = actions.index(commands_list[0])
                        action_str = commands_list[0]
                    except ValueError:
                        action = -1
            else:
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
