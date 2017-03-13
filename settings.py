import yaml


class Settings():
	def __init__(self, path):
		self.data = None
		self.path = path
		try:
			with open(path, 'r') as ymlfile:
				self.data = yaml.load(ymlfile)
		except Exception as e:
			print('failed to read config file')
			print(e)
			raise SystemExit

	def write(self):
		with open(self.path, "w") as f:
			yaml.dump(self.data, f)

	def get(self, what, default=None):
		return self.data.get(what, default)

	def set(self, what, value):
		self.data.set(what, value)
