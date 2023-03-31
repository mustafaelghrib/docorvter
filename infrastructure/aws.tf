variable "aws" {
  type    = map(string)
  default = {
    region     = ""
    access_key = ""
    secret_key = ""
    account_id = ""
  }
}

provider "aws" {
  region     = var.aws.region
  access_key = var.aws.access_key
  secret_key = var.aws.secret_key
}

variable "database_password" { type = string }

module "aws" {
  source = "./modules/aws"

  bucket_access_key = var.aws.access_key
  bucket_secret_key = var.aws.secret_key
  bucket_name       = "${local.project_name}-bucket"
  bucket_acl        = "private"

  database_identifier        = "${local.project_name}-database"
  database_name              = "${local.project_name}_db"
  database_username          = "${local.project_name}_user"
  database_password          = var.database_password
  database_port              = 5432
  database_engine            = "postgres"
  database_engine_version    = "13.7"
  database_instance_class    = "db.t3.micro"
  database_storage_type      = "gp2"
  database_allocated_storage = "20"
}

output "aws" {
  value     = module.aws
  sensitive = true
}

