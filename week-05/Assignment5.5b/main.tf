terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  region  = var.region
}

module "s3_module" {
    source      = "./s3_data/"
    bucket_name = var.bucket_name
}

output "bucket_name" {
  value = module.s3_module.s3_bucket_name
}
