# -*- coding: utf-8 -*-


"""flaskstrap.flaskstrap: provides entry point main()."""


__version__ = "0.2.1"


import sys
#from .stuff import Stuff
import create_project
#from create_project import run


def main():
	print("flaskstrap version %s." % __version__)
	#print("List of argument strings: %s" % sys.argv[1:])
	command = sys.argv[1]
	print('command: %s' % command)

	if command == 'init':
		name = sys.argv[2]
		create_project.run(name)
	#print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo():
	pass
