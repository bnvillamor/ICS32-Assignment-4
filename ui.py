# Benjoseph Villamor
# villamob
# 62443909
import a4
import sys


def after_command(command):
    if command == 'Q':
        sys.exit()
    print('Now please enter a valid path!(or option if using command P or E)')
    s_user = input()
    return s_user


def main():
    welcome = 'Welcome to the Py File Explorer and Journal!'
    print('~' * 80)
    print(f'{welcome:^80}')
    print('~' * 80)
    print('Here is a list of possible commands:')
    print('C: Create a file a new file in a specified directory')
    print('D: Delete a file')
    print('R: Read the contents of a file')
    print('O: Open an existing dsu file')
    print('L: List the contents of a specified directory')
    print('E: Edit a DSU file loaded by the C or O commands. ', end='')
    print('When writing a post, there are currently 2 available keywords:')
    print('\t@weather: Bound to temperature high')
    print('\t@lastfm: Bound to artist top album')
    print('P: Print data stored in a DSU file loaded by the C or O commands')
    print('Q: Quit the program')
    
    print('Please input a valid command. Remember that it is case sensitive!')
    command = input()
    if command in ('C', 'D', 'R', 'O', 'L', 'Q', 'E', 'P'):
        path = after_command(command)
    else:
        print('Invalid command! Please try again')
        main()
    print('Now please enter an optional input if your command needs it.')
    print('(if the command does not need one, just enter none)')
    option = input()
    if option == '':
        full_input = f'{command} {path}'
    else:
        full_input = f'{command} {path} {option}'
    a4.ui_operations(full_input)
