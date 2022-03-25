"""
This is a basic Terraform model.
"""
from terraform_model.all import *

Resource('sub-type', 'name-str', property='value')

Resource('sub-type-2', 'name-str-2', abc='def')
