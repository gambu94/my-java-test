#!/usr/bin/env python

import sys
import git
import os
import collections
from pathlib import Path

from pydriller import RepositoryMining

from utils import clone_repo, clean_tmp_dir, check_file_extension, tmp_dir


def count_repo(repo) :
    path = repo.path
    path = path.absolute().as_posix()
    counts = collections.defaultdict(int)
    for commit in RepositoryMining(path).traverse_commits() :
        for mod in commit.modifications :
            counts[mod.new_path] += 1
    return counts

def count_file_len(path) :
    with open(path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def files_complexity_repo(repo, method = 'len'):
    path = repo.path
    files_len_count = collections.defaultdict(int)
    if method == 'len' :
        for file_path in repo.files() :
            key = os.path.relpath(file_path, path)
            files_len_count[key] = count_file_len(file_path)
        return files_len_count
    elif method == 'cyclomatic' :
        path = repo.path
        path = path.absolute().as_posix()
        for commit in RepositoryMining(path).traverse_commits():
            for mod in commit.modifications :
                print(mod.new_path ,mod.complexity)
        return files_len_count
    elif method == 'otherMethod' :

        return None

def main(url):
    repo = clone_repo(url)
    path = repo.path
    print("Ci sono {} commit.".format(repo.total_commits()))
    commit_count = count_repo(repo)
    files_len_count = files_complexity_repo(repo, 'cyclomatic')
    for key in commit_count.keys():
        print(key, commit_count[key], files_len_count[key])
    clean_tmp_dir(path)
    return

if __name__ == "__main__":
    main(sys.argv[1])