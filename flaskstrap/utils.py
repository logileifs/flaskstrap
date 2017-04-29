from . import config as cfg


def dprint(string):
	if cfg.debug:
		print(string)


def exit(reason):
	print(reason)
	raise SystemExit
