import os
from pathlib2 import Path


def py_git_stat():
    # get the current working directory
    cwd = os.getcwd()
    # status messages are friends not food
    print ('Listing git statuses for ' + cwd)
    # set up Path object in cwd to start workin'
    p = Path(cwd)
    # get subdirs of the cwd
    subdirs = [item for item in p.iterdir() if item.is_dir()]
    # then, see if each subdir contains ".git" and put it in git_repos list
    git_repos = []
    for subdir in subdirs:
        q = subdir / '.git'
        if q.exists():
            git_repos.append(subdir)

    print git_repos
