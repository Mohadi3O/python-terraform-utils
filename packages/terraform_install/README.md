# Terraform Install

A small wrapper which installs Terraform.

## Usage

Create your virtual environment using something like pipenv or poetry. Once the virtual environment is activated, install `terraform-install`. Once installed, the next time a `terraform` command is run (in the virtual environment), Terraform will be installed prior to running the command. From then on, run Terraform as usual.

### For latest version of Terraform

```shell
poetry add terraform-install
terraform version
```

### For specific version of Terraform

```shell
poetry add terraform-version@1.0.0 terraform-install
terraform version
```

### To change Terraform version after initial installation

```shell
poetry add terraform-version@^1.1
terraform version
```
