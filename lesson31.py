import os
from os.path import join, getsize

prefix = prev_path = ''
prefix_f = '    '
 
orroot = 'D:/sandro/education/py_edu_1/py_edu_1/lesson31'
tree = os.walk(orroot)
for root, dirs, files in tree:
    if prev_path != os.path.dirname(root):
        prefix+='    '
    print(prefix,os.path.basename(root))
    for file in files:
        print(prefix_f,prefix, file)
    prev_path = os.path.dirname(root)
    