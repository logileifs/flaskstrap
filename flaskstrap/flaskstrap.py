# -*- coding: utf-8 -*-


"""flaskstrap.flaskstrap: provides entry point main()."""


__version__ = "0.2.1"


#import sys
#from .stuff import Stuff
import argparse
import config as cfg
#import create_project
import commands
from .utils import dprint
from .utils import exit

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('name')
parser.add_argument('--debug', dest='debug', action='store_true')

args = parser.parse_args()


def main():
	if args.debug:
		cfg.debug = True
	dprint("flaskstrap version %s." % __version__)
	command = args.command
	dprint('command: %s' % command)

	try:
		getattr(commands, command)(args)
	except AttributeError as e:
		exit('command %s not supported' % command)
