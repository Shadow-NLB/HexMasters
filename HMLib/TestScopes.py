class TestClass(object):
	data = 5
	monkey = 'test'
	def __init__(self):
		self.data = 12

instance = TestClass()
print instance.monkey
print TestClass.data
print instance.data