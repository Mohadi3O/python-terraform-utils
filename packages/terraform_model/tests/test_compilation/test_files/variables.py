"""
This is a basic Terraform model.
"""
from terraform_model.all import *

variable('a_null', null)
variable('a_bool', false, type=TfBool)
variable('a_number', 1, type=TfNumber)
variable('a_string', 'abc', type=TfString)
variable('a_list', [1, 2, 3], type=TfList[TfNumber])
variable('a_map', {'x': 1, 'y': 2}, type=TfMap[TfNumber])
variable('with_description', 2, description='the number two')
