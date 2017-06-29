import os
from pathlib2 import Path
import subprocess

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


    # now that we have only top-level git repos, let's execute git status on all of them, then store the
    # command output

    status_results = []
    for git_repo in git_repos:
        os.chdir(str(git_repo.resolve()))
        result = subprocess.check_output(['git', 'status'])
        status_results.append((git_repo.name, result))

    for status_result in status_results:
        print status_result
