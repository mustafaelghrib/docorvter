#AWS Simple Storage Service (S3)

variable "bucket_access_key" { type = string }
variable "bucket_secret_key" { type = string }
variable "bucket_name" { type = string }
variable "bucket_acl" { type = string }

resource "aws_s3_bucket" "main" {
  bucket        = var.bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_acl" "main" {
  bucket = aws_s3_bucket.main.id
  acl    = var.bucket_acl
}

resource "aws_s3_bucket_public_access_block" "main" {
  bucket                  = aws_s3_bucket.main.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

output "AWS_ACCESS_KEY_ID" { value = var.bucket_access_key }
output "AWS_SECRET_ACCESS_KEY" { value = var.bucket_secret_key }
output "AWS_STORAGE_BUCKET_NAME" { value = aws_s3_bucket.main.bucket }
output "AWS_BUCKET_DOMAIN_NAME" { value = aws_s3_bucket.main.bucket_domain_name }
