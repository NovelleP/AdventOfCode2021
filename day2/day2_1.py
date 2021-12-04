import re

available_commands = ('forward', 'up', 'down')
available_commands = '|'.join(available_commands)
command_parser = re.compile(f'({available_commands}) ([0-9]+)')


def apply_command(command, hor, depth):
    command_type, val = command_parser.search(command).groups()
    if command_type == 'forward':
        return hor + int(val), depth
    elif command_type == 'up':
        return hor, depth - int(val)
    elif command_type == 'down':
        return hor, depth + int(val)


def solve(commands):
    hor, depth = 0, 0
    for command in commands:
        hor, depth = apply_command(command, hor, depth)
    return hor * depth


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        commands = fp.readlines()
    print(solve(commands))
