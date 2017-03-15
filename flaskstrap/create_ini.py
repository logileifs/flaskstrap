import configparser
from settings import Settings

settings = Settings('settings.yml')

cfg = configparser.ConfigParser()
section = 'uwsgi'

project_name = settings.get('project_name')
bootstrap = settings.get(section).get('import')
module = settings.get(section).get('module')
module = module.replace('{{project_name}}', project_name)
#print('module = %s' % module)
master = settings.get(section).get('master')
socket = settings.get(section).get('socket')
socket = socket.replace('{{project_name}}', project_name)
#print('socket = %s' % socket)
chmod_socket = settings.get(section).get('chmod-socket')
vacuum = settings.get(section).get('vacuum')
die_on_term = settings.get(section).get('die-on-term')

cfg.add_section(section)
cfg[section]['import'] = bootstrap
cfg[section]['module'] = module
cfg[section]['master'] = master
cfg[section]['socket'] = socket
cfg[section]['chmod-socket'] = chmod_socket
cfg[section]['vacuum'] = vacuum
cfg[section]['die-on-term'] = die_on_term

with open('test/uwsgi.ini', 'w') as f:
	cfg.write(f)
