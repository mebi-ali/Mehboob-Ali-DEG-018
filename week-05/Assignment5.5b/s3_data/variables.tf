variable "bucket_name" {
  description = "AWS S3 bucket name"
  default = "mebiali-s3-data"
}

variable "acl_value" {
  description = "Access control list"
  default = "private"
}
