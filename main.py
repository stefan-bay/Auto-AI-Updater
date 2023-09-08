#!/usr/local/bin/python3

import sys
import os
import time
import random
import git

if len(sys.argv) != 2:
  sys.stderr.write(f'usage: {sys.argv[0]} [files path]\n')
  sys.exit(1)

# create files directory
files_path = sys.argv[1]
if not os.path.exists(files_path):
  print(f'Creating files path: {files_path}')
  print(f'Creating files path: {files_path}')
  os.makedirs(files_path)

# get base repo by going up a directory from the selected files path
repo_path = os.path.normpath(os.path.join(files_path, '..'))
repo = git.Repo(repo_path)

# save changes
initial_branch = repo.active_branch.name
print(f'Saving changes on currently checked out branch "{initial_branch}')
repo.git.stash()

repo.git.checkout('main')
repo.git.pull()

number_of_commits = random.randrange(1, 5)
print(f'Creating {number_of_commits} new commits')

number_of_commits = random.randrange(1, 5)
print(f'Creating {number_of_commits} new commits')

for i in range(0, number_of_commits):
  # make some change to a file
  epoch_time = str(int(time.time()))
  file_name =  epoch_time + f'_{i}' + '.txt'
  f = os.path.join(files_path, file_name)

  new_file = open(f, 'w')
  new_file.close()

  new_file = open(f, 'w')
  new_file.close()

  # commit the change with message
  commit_message = f'Added {file_name}'
  repo.git.add(f)
  repo.git.commit(m=commit_message)

  print(f'- {file_name}')

  print(f'- {file_name}')

# push the commits to github
print('Uploading commits')
print('Uploading commits')
repo.git.push()

# restore changes
print(f'Restoring changes to {initial_branch}')
repo.git.checkout(initial_branch)
repo.git.stash('pop')

# restore changes
print(f'Restoring changes to {initial_branch}')
repo.git.checkout(initial_branch)
repo.git.stash('pop')
