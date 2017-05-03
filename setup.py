# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
	'^__version__\s*=\s*"(.*)"',
	open('flaskstrap/flaskstrap.py').read(),
	re.M
).group(1)


with open("README.rst", "rb") as f:
	long_descr = f.read().decode("utf-8")


setup(
	name="flaskstrap",
	packages=["flaskstrap"],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'pyyaml',
		'paramiko',
		'termcolor',
	],
	entry_points={
		"console_scripts": [
			'flaskstrap = flaskstrap.flaskstrap:main',
			'fstrap = flaskstrap.flaskstrap:main',
			#'fstrap-init = flaskstrap.flaskstrap:init'
		]
	},
	version=version,
	description="Easily create a flask, nginx, uwsgi and bootstrap project ready for deployment",
	long_description=long_descr,
	author="Logi Leifsson",
	author_email="logileifs@gmail.com",
	url='https://github.com/logileifs/flaskstrap',
)
