#Amazon Relational Database Service (RDS)

variable "database_identifier" { type = string }
variable "database_name" { type = string }
variable "database_username" { type = string }
variable "database_password" { type = string }
variable "database_port" { type = string }
variable "database_engine" { type = string }
variable "database_engine_version" { type = string }
variable "database_instance_class" { type = string }
variable "database_storage_type" { type = string }
variable "database_allocated_storage" { type = number }

resource "aws_db_instance" "main" {

  identifier = var.database_identifier

  db_name  = var.database_name
  username = var.database_username
  password = var.database_password
  port     = var.database_port

  engine         = var.database_engine
  engine_version = var.database_engine_version

  instance_class    = var.database_instance_class
  storage_type      = var.database_storage_type
  allocated_storage = var.database_allocated_storage

  publicly_accessible      = true
  delete_automated_backups = true
  skip_final_snapshot      = true
  deletion_protection      = false
}

output "POSTGRES_DB" { value = aws_db_instance.main.db_name }
output "POSTGRES_USER" { value = aws_db_instance.main.username }
output "POSTGRES_PASSWORD" { value = aws_db_instance.main.password }
output "POSTGRES_HOST" { value = aws_db_instance.main.address }
output "POSTGRES_PORT" { value = aws_db_instance.main.port }
