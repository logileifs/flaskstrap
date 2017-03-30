import create_project
from utils import dprint


def init(args):
	dprint('init')
	try:
		name = args.name
	except Exception as e:
		exit('project name not provided')
	create_project.run(name)
