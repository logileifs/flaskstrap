import os
import sys
from shutil import copyfile

project_name = sys.argv[1]

os.mkdir(project_name)
os.mkdir(project_name + '/src')
os.mkdir(project_name + '/templates')
os.mkdir(project_name + '/tests')
copyfile('helloworld.py', project_name + '/src/' + project_name + '.py')