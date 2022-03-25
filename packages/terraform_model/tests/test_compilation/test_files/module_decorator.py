"""
This is a basic Terraform model.
"""
from terraform_model.all import *


@module
def a_module():
    variable('x', 1)
    local('y', 2)
    output('z', 3)


a_module(name='asdf', x=2)
