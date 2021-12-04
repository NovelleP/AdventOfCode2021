import re

available_commands = ('forward', 'up', 'down')
available_commands = '|'.join(available_commands)
command_parser = re.compile(f'({available_commands}) ([0-9]+)')


def apply_command(command, hor, depth, aim):
    command_type, val = command_parser.search(command).groups()
    val = int(val)
    if command_type == 'forward':
        return hor + val, depth + (aim * val), aim
    elif command_type == 'up':
        return hor, depth, aim - val
    elif command_type == 'down':
        return hor, depth, aim + val


def solve(commands):
    hor, depth, aim = 0, 0, 0
    for command in commands:
        hor, depth, aim = apply_command(command, hor, depth, aim)
    return hor * depth


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        commands = fp.readlines()
    print(solve(commands))
