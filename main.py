#!/usr/bin/env python

import time
import random
import os

number_of_commits = random.randrange(1, 10)
print(f'Creating {number_of_commits} new commits')

# create files directory
files_path = os.path.join('.', 'files')
if not os.path.exists(files_path):
  os.makedirs(files_path)

for i in range(0, number_of_commits):
  # make some change to a file
  epoch_time = str(int(time.time()))
  file_name =  epoch_time + f'_{i}' + '.txt'
  f = os.path.join(files_path, file_name)
  with open(f, 'w') as new_file:
    new_file.write(f'This file was created on {epoch_time}\n')

  # commit the change with message

# push the commits to github
