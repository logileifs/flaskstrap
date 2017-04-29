import os
import sys
from shutil import copyfile
import subprocess


def prepare_file(source, destination, replace):
	with open(source) as f1:
		with open(destination, "w") as f2:
			for line in f1:
				for key in replace:
					line = line.replace(key, replace[key])
				f2.write(line)


def create_directory(name):
	os.mkdir(name)


def run(project_name):
	print('creating project ' + project_name)
	project_dir = os.path.join(os.getcwd(), project_name)
	interpreter = sys.executable
	pip = interpreter.replace('python', 'pip')
	curr_path = os.path.dirname(os.path.realpath(__file__))

	create_directory(project_name)
	create_directory(project_name + '/src')
	create_directory(project_name + '/tests')

	helloworld = os.path.join(curr_path, 'templates/helloworld.py')
	copyfile(helloworld, project_name + '/src/' + project_name + '.py')

	main = os.path.join(curr_path, 'templates/__main__.py')
	replace = {
		'{{project_name}}': project_name
	}
	prepare_file(main, project_name + '/src/__main__.py', replace)

	unit_tests = os.path.join(curr_path, 'templates/unit-tests.py')
	unit_tests_dest = '%s/tests/unit-tests.py' % project_name
	replace = {
		'{{project_name}}': project_name
	}
	prepare_file(unit_tests, unit_tests_dest, replace)

	makefile = os.path.join(curr_path, 'templates/makefile')
	makefile_dest = '%s/makefile' % project_name
	virtualenv = interpreter.replace('/python', '')
	replace = {
		'{{virtualenv}}': virtualenv,
		'{{project_name}}': project_name
	}
	prepare_file(makefile, makefile_dest, replace)


	print('installing requirements')

	cmd1 = (pip + ' install flask nose').split()
	subprocess.Popen(cmd1, cwd=project_dir).wait()
	cmd = (pip + ' freeze').split()

	requirements = os.path.join(project_dir, 'requirements.txt')
	with open(requirements, 'w') as f:
		subprocess.call(cmd, stdout=f)
