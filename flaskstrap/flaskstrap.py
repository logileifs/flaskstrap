# -*- coding: utf-8 -*-


"""flaskstrap.flaskstrap: provides entry point main()."""


__version__ = "0.2.6"


import argparse
from . import commands
from . import config as cfg
from .utils import exit
from .utils import dprint

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('name')
parser.add_argument('--debug', dest='debug', action='store_true')

args = vars(parser.parse_args())


def main():
	if args.get('debug', False):
		cfg.debug = True
	dprint(args)
	dprint("flaskstrap version %s." % __version__)
	command = args.get('command', None)
	dprint('command: %s' % command)

	try:
		getattr(commands, command)(args)
	except AttributeError:
		exit('command %s not supported' % command)
