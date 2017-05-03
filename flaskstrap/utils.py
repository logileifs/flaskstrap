from . import config as cfg
import os
from termcolor import cprint


def dprint(string):
	if cfg.debug:
		print(string)


def exit(reason):
	print(reason)
	raise SystemExit


def get_project_name():
	return os.getcwd().split('/')[-1]


def get_current_path():
	return os.path.dirname(os.path.realpath(__file__))


def prepare_file(source, destination, replace):
	with open(source) as f1:
		with open(destination, "w") as f2:
			for line in f1:
				for key in replace:
					line = line.replace(key, replace[key])
				f2.write(line)


def print_error(error):
	cprint(error, 'red', attrs=['bold'])


def print_cyan(text):
	cprint(text, 'cyan', attrs=['bold'])
