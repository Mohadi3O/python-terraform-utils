# Terraform Install

## Usage

Create your virtual environment using something like pipenv or poetry. Once the virtual environment is activated, run the following commands.

### For latest version of Terraform

```shell
poetry add terraform-install
terraform-install
```

### For specific version of Terraform

```shell
poetry add terraform-version@1.0.0 terraform-install
terraform-install
```

### To change Terraform version after initial installation

```shell
poetry add terraform-version@^1.1
terraform-install
```
