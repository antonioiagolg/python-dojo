if __name__ == '__main__':
    N = int(input())
    commands = []
    data = []

    for i in range(N):
        commands.append(input())

    for command in commands:
        command_parts = command.split(sep=' ')

        if command_parts[0] == 'insert':
            position = int(command_parts[1])
            elem     = int(command_parts[2])
            data.insert(position, elem)

        elif command_parts[0] == 'print':
            print(data)

        elif command_parts[0] == 'remove':
            elem = int(command_parts[1])
            data.remove(elem)

        elif command_parts[0] == 'append':
            elem = int(command_parts[1])
            data.append(elem)

        elif command_parts[0] == 'pop':
            data.pop()

        elif command_parts[0] == 'sort':
            data.sort()

        elif command_parts == 'reverse':
            data.reverse()

        else:
            print(f'invalid command: {commmand_parts[0]}')


