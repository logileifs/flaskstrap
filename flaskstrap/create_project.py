import os
from shutil import copyfile


def run(project_name):
	print('creating project ' + project_name)
	curr_path = os.path.dirname(os.path.realpath(__file__))
	#print('curr_path: %s' % curr_path)
	os.mkdir(project_name)
	os.mkdir(project_name + '/src')
	#os.mkdir(project_name + '/templates')
	os.mkdir(project_name + '/tests')
	helloworld = os.path.join(curr_path, 'templates/helloworld.py')
	#copyfile('templates/helloworld.py', project_name + '/src/' + project_name + '.py')
	copyfile(helloworld, project_name + '/src/' + project_name + '.py')
	unit_tests = os.path.join(curr_path, 'templates/unit-tests.py')
	with open(unit_tests) as f1:
		with open('%s/tests/unit-tests.py' % project_name, "w") as f2:
			for line in f1:
				line = line.replace('{{project_name}}', project_name)
				#line = line.replace('{{user}}', user)
				f2.write(line)
