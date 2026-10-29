variable "api_port" {
  description = "Puerto en el que escucha la API"
  type        = number
  default     = 8000
}

variable "aws_region" {
  description = "Region de AWS"
  type        = string
  default     = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

 provider  "aws" {
  region = var.aws_region
}

resource "aws_security_group" "diagx_api" {
  name        = "diagx-api-tf"
  description = "Security group de Diagx creado con Terraform"

  ingress {
    description = "API de Diagx"
    from_port   = var.api_port
    to_port     = var.api_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}