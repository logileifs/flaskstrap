import os
import sys
from shutil import copyfile
import ruamel.yaml as yaml
import subprocess
from .utils import prepare_file
from .utils import iprint
from .utils import sprint
from .utils import dprint
from .utils import get_current_path
from . import utils


def create_directory(name):
	os.mkdir(name)


def make_project_structure():
	create_directory(project_name)
	create_directory(project_name + '/src')
	create_directory(project_name + '/dist')
	create_directory(project_name + '/tests')
	create_directory(project_name + '/requirements')


def make_main_app_file():
	curr_path = get_current_path(__file__)
	helloworld = os.path.join(curr_path, 'templates/helloworld.py')
	copyfile(helloworld, project_name + '/src/' + project_name + '.py')


def make_app_entry_point(replace):
	curr_path = get_current_path(__file__)
	main = os.path.join(curr_path, 'templates/__main__.py')
	prepare_file(main, project_name + '/src/__main__.py', replace)


def install_requirements():
	iprint('Installing requirements')
	pip = utils.get_pip_path()
	project_dir = os.path.join(os.getcwd(), project_name)

	cmd1 = (pip + ' install flask nose').split()
	devnull = open(os.devnull, 'w')
	subprocess.call(cmd1, cwd=project_dir, stdout=devnull)
	devnull.close()


def make_project_settings():
	dprint('making project settings')
	data = {'project_name': project_name}
	path = '{0}/project_settings.yml'.format(project_name)
	with open(path, 'w') as outfile:
		yaml.round_trip_dump(data, outfile)


def make_server_settings():
	dprint('making server settings')
	curr_path = get_current_path(__file__)
	server_settings_path = os.path.join(curr_path, 'templates/server_settings.yml')
	with open(server_settings_path) as infile:
		data = yaml.round_trip_load(infile)

	data['username'] = data['username'].format(**{'project_name': project_name})
	path = '{0}/server_settings.yml'.format(project_name)
	with open(path, 'w') as outfile:
		yaml.round_trip_dump(data, outfile)


def run(args):
	global project_name
	project_name = args.get('second', None)[0]
	iprint('Creating project {0}'.format(project_name))

	project_dir = os.path.join(os.getcwd(), project_name)
	interpreter = sys.executable
	virtualenv = os.path.dirname(interpreter)
	pip = interpreter.replace('python', 'pip')
	#curr_path = os.path.dirname(os.path.realpath(__file__))
	curr_path = get_current_path(__file__)

	replace = {
		'virtualenv': virtualenv,
		'project_name': project_name
	}

	make_project_structure()

	make_main_app_file()

	make_app_entry_point(replace)

	unit_tests = os.path.join(curr_path, 'templates/unit-tests.py')
	unit_tests_dest = '{0}/tests/unit-tests.py'.format(project_name)
	prepare_file(unit_tests, unit_tests_dest, replace)

	makefile = os.path.join(curr_path, 'templates/makefile')
	makefile_dest = '{0}/makefile'.format(project_name)
	prepare_file(makefile, makefile_dest, replace)


	install_requirements()

	cmd = (pip + ' freeze').split()
	requirements = os.path.join(project_dir, 'requirements', 'dev.txt')
	with open(requirements, 'w') as f:
		subprocess.call(cmd, stdout=f)


	make_project_settings()
	make_server_settings()

	sprint('{0} created'.format(project_name))
