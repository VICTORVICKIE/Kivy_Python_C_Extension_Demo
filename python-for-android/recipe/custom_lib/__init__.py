from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class BillBookLibRecipe(CompiledComponentsPythonRecipe):

	site_packages_name = 'custom_lib'
	depends = ['setuptools']
	call_hostpython_via_targetpython = False

	
	def should_build(self, arch):
		return True

recipe = BillBookLibRecipe()