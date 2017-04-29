from . import create_project
from .utils import dprint


def init(args):
	dprint('init')
	try:
		name = args.get('name', None)
	except Exception:
		exit('project name not provided')
	create_project.run(name)
