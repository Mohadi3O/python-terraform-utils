"""
This is a basic Terraform model.
"""
from terraform_model.all import *


@module_function
def a_module(x=1):
    local('y', 2)
    return 3


a_module(name='asdf', x=2)
