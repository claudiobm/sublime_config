# to run 
# python resolver_test.py

import unittest
from resolver import *

class ResolverTest(unittest.TestCase):

	def test_is_spec_returns_true(self):
		file = '/spec/foo/something_spec.rb'
		r = Resolver().is_spec(file)
		self.assertEqual(r, True)

	def test_is_spec_returns_true_for_erb(self):
		file = '/spec/views/something.html.erb_spec.rb'
		r = Resolver().is_spec(file)
		self.assertEqual(r, True)

	def test_is_spec_returns_false(self):
		file = '/app/foo/something.rb'
		r = Resolver().is_spec(file)
		self.assertEqual(r, False)

	# get_source

	def test_finds_source(self):
		file = '/spec/something/foo_spec.rb'
		r = Resolver().get_source(file)
		self.assertEqual(r, '/app/something/foo.rb')

	def test_finds_source_from_erb(self):
		file = '/spec/views/namespace/users/_something.html.erb_spec.rb'
		r = Resolver().get_source(file)
		self.assertEqual(r, '/app/views/namespace/users/_something.html.erb')

	def test_finds_source_from_haml(self):
		file = '/spec/views/documents/update.html.haml_spec.rb'
		r = Resolver().get_source(file)
		self.assertEqual(r, '/app/views/documents/update.html.haml')

	def test_finds_source_from_lib(self):
		file = '/spec/lib/something/foo_spec.rb'
		r = Resolver().get_source(file)
		self.assertEqual(r, '/lib/something/foo.rb')

	# get_spec

	def test_finds_spec(self):
		file = '/app/models/user.rb'
		r = Resolver().get_spec(file)
		self.assertEqual(r, '/spec/models/user_spec.rb')

	def test_finds_spec_from_lib(self):
		file = '/lib/foo/utility.rb'
		r = Resolver().get_spec(file)
		self.assertEqual(r, '/spec/lib/foo/utility_spec.rb')

	def test_finds_spec_from_erb(self):
		file = '/app/views/users/new.html.erb'
		r = Resolver().get_spec(file)
		self.assertEqual(r, '/spec/views/users/new.html.erb_spec.rb')

	def test_finds_spec_from_haml(self):
		file = '/app/views/account/login.html.haml'
		r = Resolver().get_spec(file)
		self.assertEqual(r, '/spec/views/account/login.html.haml_spec.rb')

		# run

	def test_run(self):
		file = '/app/decorators/namespace/user_decorator.rb'
		r = Resolver().run(file)
		self.assertEqual(r, '/spec/decorators/namespace/user_decorator_spec.rb')

	def test_run_from_lib(self):
		file = '/lib/utilities/namespace/foo.rb'
		r = Resolver().run(file)
		self.assertEqual(r, '/spec/lib/utilities/namespace/foo_spec.rb')

	def test_run_from_spec(self):
		file = '/spec/controllers/namespace/foo_controller_spec.rb'
		r = Resolver().run(file)
		self.assertEqual(r, '/app/controllers/namespace/foo_controller.rb')

	def test_run_from_spec_lib(self):
		file = '/spec/lib/namespace/foo_spec.rb'
		r = Resolver().run(file)
		self.assertEqual(r, '/lib/namespace/foo.rb')

	def test_run_for_erb_spec(self):
		file = '/spec/views/namespace/users/_new.html.erb_spec.rb'
		r = Resolver().run(file)
		self.assertEqual(r, '/app/views/namespace/users/_new.html.erb')

if __name__ == '__main__':
	unittest.main()