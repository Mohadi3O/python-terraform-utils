# std
import json
import os
import unittest

# internal
from terraform_model.compilation.compile import import_module_from_filepath
from terraform_model.helpers.scope import Scope
from terraform_model.model import model
from terraform_model.utils.json import dumps


class TestCompile(unittest.TestCase):
    _terraform_py = os.path.join(os.path.dirname(__file__), 'test_files/terraform.py')
    _terraform_json = os.path.join(os.path.dirname(__file__), 'test_files/terraform.json')
    _variables_py = os.path.join(os.path.dirname(__file__), 'test_files/variables.py')
    _variables_json = os.path.join(os.path.dirname(__file__), 'test_files/variables.json')
    _locals_py = os.path.join(os.path.dirname(__file__), 'test_files/locals.py')
    _locals_json = os.path.join(os.path.dirname(__file__), 'test_files/locals.json')
    _outputs_py = os.path.join(os.path.dirname(__file__), 'test_files/outputs.py')
    _outputs_json = os.path.join(os.path.dirname(__file__), 'test_files/outputs.json')
    _providers_py = os.path.join(os.path.dirname(__file__), 'test_files/providers.py')
    _providers_json = os.path.join(os.path.dirname(__file__), 'test_files/providers.json')
    _data_py = os.path.join(os.path.dirname(__file__), 'test_files/data.py')
    _data_json = os.path.join(os.path.dirname(__file__), 'test_files/data.json')
    _resources_py = os.path.join(os.path.dirname(__file__), 'test_files/resources.py')
    _resources_json = os.path.join(os.path.dirname(__file__), 'test_files/resources.json')
    _modules_py = os.path.join(os.path.dirname(__file__), 'test_files/modules.py')
    _modules_json = os.path.join(os.path.dirname(__file__), 'test_files/modules.json')
    _module_decorator_py = os.path.join(os.path.dirname(__file__), 'test_files/module_decorator.py')
    _module_decorator_a_json = os.path.join(os.path.dirname(__file__), 'test_files/module_decorator_a.json')
    _module_decorator_b_json = os.path.join(os.path.dirname(__file__), 'test_files/module_decorator_b.json')
    _module_function_decorator_py = os.path.join(os.path.dirname(__file__), 'test_files/module_function_decorator.py')
    _module_function_decorator_a_json = os.path.join(os.path.dirname(__file__), 'test_files/module_function_decorator_a.json')
    _module_function_decorator_b_json = os.path.join(os.path.dirname(__file__), 'test_files/module_function_decorator_b.json')
    _expressions_py = os.path.join(os.path.dirname(__file__), 'test_files/expressions.py')
    _expressions_json = os.path.join(os.path.dirname(__file__), 'test_files/expressions.json')

    @staticmethod
    def read(filepath) -> str:
        with open(filepath, 'r') as fh:
            return fh.read().strip()

    def assertModelEqual(self, model: dict, filepath: str):
        model_str = dumps(model).strip()
        expected = self.read(filepath)
        self.assertEqual(expected, model_str)

    def tearDown(self) -> None:
        Scope.clear_scopes()

    def test_terraform_block(self):
        import_module_from_filepath(self._terraform_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._terraform_json)

    def test_variables(self):
        import_module_from_filepath(self._variables_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._variables_json)

    def test_locals(self):
        import_module_from_filepath(self._locals_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._locals_json)

    def test_outputs(self):
        import_module_from_filepath(self._outputs_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._outputs_json)

    def test_providers(self):
        import_module_from_filepath(self._providers_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._providers_json)

    def test_data(self):
        import_module_from_filepath(self._data_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._data_json)

    def test_resources(self):
        import_module_from_filepath(self._resources_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._resources_json)

    def test_modules(self):
        import_module_from_filepath(self._modules_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._modules_json)

    def test_module_decorator(self):
        import_module_from_filepath(self._module_decorator_py)
        scope_a = Scope.get_scope()
        self.assertModelEqual(model(scope_a), self._module_decorator_a_json)
        scope_b = scope_a.children[0]
        self.assertModelEqual(model(scope_b), self._module_decorator_b_json)

    def test_module_function_decorator(self):
        import_module_from_filepath(self._module_function_decorator_py)
        scope_a = Scope.get_scope()
        self.assertModelEqual(model(scope_a), self._module_function_decorator_a_json)
        scope_b = scope_a.children[0]
        self.assertModelEqual(model(scope_b), self._module_function_decorator_b_json)

    def test_expressions(self):
        import_module_from_filepath(self._expressions_py)
        scope = Scope.get_scope()
        self.assertModelEqual(model(scope), self._expressions_json)
