"""
This is a basic Terraform model.
"""
from terraform_model.all import *

RequiredVersion('1.2.3')

S3Backend('us-east-1', 'bucket-name', 'key')

RequiredProvider('provider-name', 'source-str', 'version-str')
