resource "aws_s3_bucket" "s3_data" {
    bucket = var.bucket_name
}

resource "aws_s3_object" "folder" {
    bucket = "${aws_s3_bucket.s3_data.id}"
    key    = "day2/IaC/"
    acl    = var.acl_value
    source = ""
}
