variable "region" {
  description = "AWS Region"
  default = "us-east-1"
}

# S3
variable "bucket_name" {
  description = "AWS S3 bucket name"
  default = "mebiali-s3-data"

}