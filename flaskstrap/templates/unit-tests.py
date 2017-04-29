from {{project_name}} import app


class TestUnits():

	@classmethod
	def setup_class(self):
		global client
		client = app.test_client()

	def test_true_is_true(s):
		assert True is True

	def test_index(s):
		rsp = client.get('/')
		assert rsp is not None
		assert rsp.status_code == 200
