#!/usr/bin/env python

import sys
import os
import time
import random

if len(sys.argv) != 2:
  sys.stderr.write(f'usage: {sys.argv[0]} [absolute file path]\n')
  sys.exit(1)

number_of_commits = random.randrange(1, 10)
print(f'Creating {number_of_commits} new commits')

# create files directory
files_path = sys.argv[1]
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
