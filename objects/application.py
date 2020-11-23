class Application:
    def __init__(self):
        pass

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
    def action_choice(actions, choice_title='Выберите действие:', reprint_after=5) -> int:
        allowed = []
        choice_message = choice_title + '\n'
        if reprint_after < 1:
            reprint_after = 1
        for i in range(len(actions)):
            allowed.append(str(actions[i]))
            allowed.append(str(i + 1))
            choice_message = choice_message + '{}. {}\n'.format(i + 1, actions[i])
        print(choice_message)
        action = -1
        while action == -1:
            commands_list = Application.get_user_input(allowed=allowed, allowed_lines=True, max_tries=reprint_after)
            if len(commands_list):
                try:
                     action = int(commands_list[0]) - 1
                except ValueError:
                    try:
                        action = actions.index(commands_list[0])
                    except ValueError:
                        action = -1
            else:
                print()
                print(choice_message)
        return action

    def main_loop(self):
        is_exit = False
        while not is_exit:
            action = self.action_choice(['Начать', 'Выйти'])
            if action == 1:
                is_exit = True

