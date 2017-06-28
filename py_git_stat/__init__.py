import os

def py_git_stat():
    # get the current working directory
    cwd = os.listdir(os.getcwd())

    # and make a second list once we narrow the contents down
    cwd_dirs = []
    for item in cwd:
        if os.path.isdir(item):
            cwd_dirs.append(item)


    for dir_item in cwd_dirs:
        print(os.path.abspath(item))
    # now, search the cwd_dirs for ones that have .git as a subdirectory




