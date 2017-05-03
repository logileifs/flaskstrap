from . import create_project
from . import setup_server
from .utils import dprint


def init(args):
	dprint('init')
	try:
		name = args.get('name', None)
	except Exception:
		exit('project name not provided')
	create_project.run(args)


def setup(args):
	dprint('setup server')
	setup_server.run(args)
