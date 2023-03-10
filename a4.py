# Benjoseph Villamor
# villamob@uci.edu
# 62443909

import ds_client
import ui
from pathlib import Path
import os
import re
import Profile
import ds_client

open_vars = 'default'
create_vars = 'default'
port = 3021


# handles the input for when the user wants to list files with no options
def no_options(inputPath):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_file():
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():
                print(currentPath)
    except FileNotFoundError:
        print('ERROR')


# handles input for the f option
def option_f(inputPath):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_file():
                print(currentPath)
    except FileNotFoundError:
        print('ERROR')


# handles input for the e option
def option_e(inputPath, input_extension):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.suffix == f'.{input_extension}':
                print(currentPath)
    except FileNotFoundError:
        print('ERROR')


# handles input for the s option
def option_s(inputPath, input_file):
    try:
        file_test = 0
        myPath = Path(inputPath)
        myFile = myPath / input_file
        for currentPath in myPath.iterdir():
            if myFile == currentPath:
                print(currentPath)
                file_test += 1
        if file_test == 0:
            print('ERROR')
    except FileNotFoundError:
        print('ERROR')


# handles input for the recusive option
def recursion(inputPath):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_file():
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():
                print(currentPath)
                recursion(currentPath)
    except FileNotFoundError:
        print('ERROR')


# handles input for the recusive option with f
def recursion_with_f(inputPath):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_file():
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():
                recursion_with_f(currentPath)
    except FileNotFoundError:
        print('ERROR')


# handles input for the recusive option with e
def recursion_with_e(inputPath, input_extension):
    try:
        myPath = Path(inputPath)
        for currentPath in myPath.iterdir():
            if currentPath.suffix == f'.{input_extension}':
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():
                recursion_with_e(currentPath, input_extension)
    except FileNotFoundError:
        print('ERROR')


# handles input for the recusive option with s
def recursion_with_s(inputPath, input_file):
    try:
        myPath = Path(inputPath)
        myFile = myPath / input_file
        for currentPath in myPath.iterdir():
            if myFile == currentPath:
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():
                recursion_with_s(currentPath, input_file)
    except FileNotFoundError:
        print('ERROR')


# creates a new file
def create(inputPath, input_file):
    checker = 'on'
    try:
        input_file += '.dsu'
        if inputPath[-1] == '/' or inputPath[-1] == '\\':
            myFile = inputPath + input_file
        else:
            if os.name == 'nt':
                myFile = f'{inputPath}\\{input_file}'
            else:
                myFile = f'{inputPath}/{input_file}'
        if Path(myFile).exists():
            print('This file already exists, it is now loaded')
            prof = Profile.Profile()
            prof.load_profile(myFile)
            return prof, myFile
        else:
            f = open(Path(myFile), 'x')
            print(f'Created {myFile}')
            f.close()
            try:
                prof = Profile.Profile()
                print('Please input a username(no spaces allowed):')
                username = input()
                if ' ' in username:
                    checker = 'off'
                print('Please input a password(no spaces allowed):')
                password = input()
                if ' ' in password:
                    checker = 'off'
                print('Please input a bio:')
                bio = input()
                if (not username.isspace()) and (username != ''):
                    prof.username = username
                if (not password.isspace()) and (password != ''):
                    prof.password = password
                prof.bio = bio
                print('Please enter desired DSU server to post to:')
                server = input()
                prof.dsuserver = server
                if checker == 'off':
                    print('ERROR')
                if checker == 'on':
                    prof.save_profile(myFile)
                return prof, myFile
            except (Profile.DsuFileError):
                print('Error')
    except (FileNotFoundError, FileExistsError):
        print('ERROR')


# delete a file
def delete(inputPath):
    try:
        if inputPath[-4:] == '.dsu':
            d_file = Path(inputPath)
            d_file.unlink()
            print(f'{inputPath} DELETED')
        else:
            print('ERROR')
    except FileNotFoundError:
        print('ERROR')


# read the file
def read(inputPath):
    try:
        if inputPath[-4:] == '.dsu':
            f = open(Path(inputPath), 'r')
            if os.stat(inputPath).st_size == 0:
                print('EMPTY')
            else:
                print(f.read(), end='')
        else:
            print('ERROR')
    except FileNotFoundError:
        print('ERROR')


def open_dsu(inputPath):
    try:
        if Path(inputPath).exists():
            if inputPath[-4:] == '.dsu':
                prof = Profile.Profile()
                prof.load_profile(inputPath)
                print(f'Successfully opened {inputPath}!')
                return prof, inputPath
            else:
                print('ERROR')
        else:
            print('ERROR')
    except (FileNotFoundError, Profile.DsuFileError, Profile.DsuProfileError):
        print('ERROR')


def edit(o_vars, c_vars, user_input):
    check = 'on'
    if o_vars != 'default':
        prof = o_vars[0]
        path = o_vars[1]
    elif c_vars != 'default':
        prof = c_vars[0]
        path = c_vars[1]
    search = re.compile(r'(\-\w+)\s((("[^"]*"))|(\d+))')
    res = search.findall(user_input)
    lst1 = []
    for i in range(len(res)):
        lst2 = []
        for j in range(len(res[i])):
            if '-' in res[i][j]:
                lst2.append(res[i][j])
                count_q = res[i][j + 1].count('\"')
                if count_q % 2 != 0:
                    check = 'off'
                temp = res[i][j + 1].strip('"')
                lst2.append(temp)
        lst1.append(lst2)
    if user_input[2:] == '-publishbio':
        # No additional option parameters
        # Publishes the current bio
        ds_client.send(prof.dsuserver, port, prof.username,
                       prof.password, message=None, bio=prof.bio)
    for option in range(len(lst1)):
        if lst1[option][0] == '-usr':
            prof.username = lst1[option][1]
            if ' ' in (lst1[option][1]):
                check = 'off'
        elif lst1[option][0] == '-pwd':
            prof.password = lst1[option][1]
            if ' ' in (lst1[option][1]):
                check = 'off'
        elif lst1[option][0] == '-bio':
            prof.bio = lst1[option][1]
        elif lst1[option][0] == '-addpost':
            post = Profile.Post()
            post.set_entry(lst1[option][1])
            prof.add_post(post)
        elif lst1[option][0] == '-delpost':
            prof.del_post(int(lst1[option][1]))
        elif lst1[option][0] == '-publishpost':
            # Followed by the post id
            # Publishes the post associated with the id
            posts = prof.get_posts()
            if len(posts) > 0:
                ds_client.send(prof.dsuserver, port, prof.username, prof.password, posts[int(lst1[option][1])]['entry'])
            else:
                print('No posts to send')
        elif lst1[option][0] == '-publish':
            # Followed by the post id
            # Publishes both the post associated with the id and the bio
            posts = prof.get_posts()
            if len(posts) > 0:
                ds_client.send(prof.dsuserver, port, prof.username, prof.password, posts[int(lst1[option][1])]['entry'], prof.bio)
            else:
                print('No posts to send')
        elif lst1[option][0] == '-srv':
            prof.dsuserver = lst1[option][1]
        else:
            print('ERROR')
    if check == 'off':
        print('ERROR')
    if check == 'on':
        prof.save_profile(path)


def print_dsu(o_vars, c_vars, user_input):
    if o_vars != 'default':
        prof = o_vars[0]
        path = o_vars[1]
    elif c_vars != 'default':
        prof = c_vars[0]
        path = c_vars[1]
    lst1 = user_input.split()
    lst2 = ['P', '-usr', '-pwd', '-bio', '-posts', '-post', '-all']
    for option in range(len(lst1)):
        if (lst1[option] in lst2) or (lst1[option].isnumeric()):
            if lst1[option] == '-usr':
                print(f'Username: {prof.username}')
            if lst1[option] == '-pwd':
                print(f'Password: {prof.password}')
            if lst1[option] == '-bio':
                print(f'Bio: {prof.bio}')
            if lst1[option] == '-posts':
                posts = prof.get_posts()
                for i in range(len(posts)):
                    entry = posts[i]['entry']
                    print(f'Post ID: {i} - Entry: {entry}')
            if lst1[option] == '-post':
                if lst1[option + 1].isnumeric():
                    posts = prof.get_posts()
                    if len(posts) > 0:
                        entry = posts[int(lst1[option + 1])]['entry']
                        print(f'Entry: {entry}')
                    else:
                        print('ERROR')
                else:
                    print('ERROR')
                    return
            if lst1[option] == '-all':
                print(f'Username: {prof.username}')
                print(f'Password: {prof.password}')
                print(f'Bio: {prof.bio}')
                posts = prof.get_posts()
                for i in range(len(posts)):
                    entry = posts[i]['entry']
                    print(f'Post ID: {i} - Entry: {entry}')
        else:
            print('Error')
            return
    prof.save_profile(path)


# main file operations
def file_operations(user1):
    global open_vars
    global create_vars
    if user1[0:2] == 'P ':
        print_dsu(open_vars, create_vars, user1)
    if user1[0:2] == 'E ':
        edit(open_vars, create_vars, user1)
    if ' -' in user1 and (user1[0] != 'E' or user1[0] != 'P'):
        user_path = re.findall('. (.*?)(?= -[rfens])', user1)
    else:
        user_path = re.findall('. (.*)', user1)
    if user1 == 'Q':
        quit()
    if ('/' in user1 or '\\' in user1) and (len(user1.split()) > 1):
        user1 = user1.replace(user_path[0], '')
        user2 = user1.split()
    elif user1[0:2] == 'P ' or user1[0:2] == 'E ':
        return
    else:
        print('ERROR')
        return
    if len(user2) == 1:
        if user2[0] == 'L':
            no_options(user_path[0])
        elif user2[0] == 'D':
            delete(user_path[0])
        elif user2[0] == 'R':
            read(user_path[0])
        elif user2[0] == 'O':
            open_vars = open_dsu(user_path[0])
        else:
            print('ERROR')
    if len(user2) == 2:
        if user2[0] == 'L' and user2[1] == '-r':
            recursion(user_path[0])
        elif user2[0] == 'L' and user2[1] == '-f':
            option_f(user_path[0])
        else:
            print('ERROR')
    if len(user2) == 3:
        if user2[0] == 'L' and user2[1] == '-r' and user2[2] == '-f':
            recursion_with_f(user_path[0])
        elif user2[0] == 'L' and user2[1] == '-s':
            option_s(user_path[0], user2[2])
        elif user2[0] == 'L' and user2[1] == '-e':
            option_e(user_path[0], user2[2])
        elif user2[0] == 'C' and user2[1] == '-n':
            create_vars = create(user_path[0], user2[2])
        else:
            print('ERROR')
    if len(user2) == 4:
        if user2[0] == 'L' and user2[1] == '-r' and user2[2] == '-e':
            recursion_with_e(user_path[0], user2[3])
        elif user2[0] == 'L' and user2[1] == '-r' and user2[2] == '-s':
            recursion_with_s(user_path[0], user2[3])
        elif user2[0] == 'C' and user2[1] == '-n':
            del user2[0]
            del user2[0]
            file = ''
            for item in user2:
                if item == user2[-1]:
                    file += item
                else:
                    file += item
                    file += ' '
            create_vars = create(user_path[0], file)
        else:
            print('ERROR')
    if len(user2) >= 5:
        del user2[0]
        del user2[0]
        file = ''
        for item in user2:
            if item == user2[-1]:
                file += item
            else:
                file += item
                file += ' '
        create_vars = create(user_path[0], file)


def ui_operations(user_input):
    file_operations(user_input)
    ui.main()


if __name__ == "__main__":
    ui.main()
