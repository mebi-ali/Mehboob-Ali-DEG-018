terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"  # AWS provider
      version = "~> 4.39"        # Provider version
    }
  }

  required_version = ">= 1.2.0"  # Minimum Terraform version
}

provider "aws" {
  region = "eu-central-1"        # AWS region
}

resource "aws_s3_bucket" "mebi_s3_bucket" {
  bucket = "mebi-s3-bucket"      # S3 bucket name

  tags = {
    Name = "output"              # S3 bucket tag
  }
}

output "s3_bucket_name" {
  description = "AWS S3 bucket name"               # Output description
  value       = aws_s3_bucket.mebi_s3_bucket.id    # Output S3 bucket ID
}
