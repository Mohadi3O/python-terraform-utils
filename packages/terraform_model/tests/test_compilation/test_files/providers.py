"""
This is a basic Terraform model.
"""
from terraform_model.all import *

Provider('abc')

Provider('abc', alias='an-alias')

Provider('def', property='value')
