# -*- coding: utf-8 -*-


"""flaskstrap.flaskstrap: provides entry point main()."""


__version__ = "0.3.6"


import sys
import argparse
from . import commands
from . import config as cfg
from .utils import exit
from .utils import dprint
from .utils import eprint

is_python2 = sys.version_info[0] == 2
if is_python2:
	FileExistsError = OSError
else:
	from builtin import FileExistsError

parser = argparse.ArgumentParser()
parser.add_argument(
	'-i',
	'--interactive',
	action="store_true",
	help='interactive mode'
)
parser.add_argument('command')
parser.add_argument('second', nargs='*')
parser.add_argument(
	'-v',
	'--verbose',
	dest='verbose',
	action='store_true',
	help='increase verbosity'
)

args = vars(parser.parse_args())
#print(args)


def main():
	if args.get('debug', False):
		cfg.debug = True
	if args.get('verbose', False):
		cfg.verbose = True
	dprint(args)
	dprint("flaskstrap version %s." % __version__)
	command = args.get('command', None)
	dprint('command: %s' % command)

	try:
		getattr(commands, command)(args)
	except AttributeError:
		exit('command %s not supported' % command)
	except FileExistsError:
		eprint('Project already exists')
