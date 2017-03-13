import nginx
from settings import Settings

settings = Settings('settings.yml')

project_name = settings.get('project_name')

nginx_settings = settings.get('nginx')

listen = nginx_settings.get('listen')
server_name = nginx_settings.get('server_name')
location = nginx_settings.get('location')
include = nginx_settings.get('location_keys').get('include')
uwsgi_pass = nginx_settings.get('location_keys').get('uwsgi_pass')
uwsgi_pass = uwsgi_pass.replace('{{project_name}}', project_name)

c = nginx.Conf()
s = nginx.Server()
s.add(
	nginx.Key('listen', listen),
	#nginx.Comment('Yes, python-nginx can read/write comments!'),
	nginx.Key('server_name', server_name),
	nginx.Location(
		location,
		nginx.Key('include', include),
		nginx.Key('uwsgi_pass', uwsgi_pass),
	)
)
c.add(s)
nginx.dumpf(c, 'test/' + project_name)
