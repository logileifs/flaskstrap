import os
import sys
from . import config as cfg
from termcolor import cprint
import ruamel.yaml as yaml


def dprint(string):
	if cfg.verbose:
		cprint(string, 'cyan', attrs=['bold'])
		#print(string)


def exit(reason):
	print(reason)
	raise SystemExit


def get_project_name2():
	return os.getcwd().split('/')[-1]


def get_project_name():
	cwd = os.getcwd()
	eprint('cwd: ' + cwd)
	project_settings_path = os.path.join(cwd, 'project_settings.yml')
	with open(project_settings_path) as infile:
		project_settings = yaml.round_trip_load(infile)
	eprint('returning project_name: ' + project_settings.get('project_name', None))
	return project_settings.get('project_name', None)


def get_project_settings():
	cwd = os.getcwd()
	eprint('cwd: ' + cwd)
	project_settings_path = os.path.join(cwd, 'project_settings.yml')
	with open(project_settings_path) as infile:
		project_settings = yaml.round_trip_load(infile)
	#eprint('returning project_name: ' + project_settings.get('project_name', None))
	return project_settings


def get_server_settings():
	cwd = os.getcwd()
	eprint('cwd: ' + cwd)
	server_settings_path = os.path.join(cwd, 'server_settings.yml')
	with open(server_settings_path) as infile:
		server_settings = yaml.round_trip_load(infile)
	#eprint('returning project_name: ' + server_settings.get('project_name', None))
	return server_settings


def get_current_path(current_file):
	return os.path.dirname(os.path.realpath(current_file))


def get_pip_path():
	interpreter = sys.executable
	#virtualenv = os.path.dirname(interpreter)
	pip = interpreter.replace('python', 'pip')
	return pip


def prepare_file(source, destination, replace):
	with open(source) as f1:
		with open(destination, "w") as f2:
			for line in f1:
				line = line.format(**replace)
				f2.write(line)


def eprint(error):
	cprint(error, 'red', attrs=['bold', 'underline'])


def iprint(info):
	"""Information print"""
	cprint(info, 'blue', attrs=['bold'])


def sprint(info):
	"""Success print"""
	cprint(info, 'green', attrs=['bold'])


def print_cyan(text):
	cprint(text, 'cyan', attrs=['bold'])
