from terraform_model.types.terraform_type import TerraformType


class Unknown(TerraformType):

    def __str__(self):
        return str(self.data)
