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

variable "instance_type" {
  description = "Tipo de instancia EC2"
  type        = string
  default     = "t4g.micro"
}

# Busca la imagen de Ubuntu ARM mas reciente publicada por Canonical
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-arm64-server-*"]
  }
}

resource "aws_instance" "diagx_tf" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  key_name               = "diagx-key"
  vpc_security_group_ids = [aws_security_group.diagx_api.id]

  tags = {
    Name = "diagx-tf"
  }
}

output "public_ip" {
  description = "IP publica de la instancia"
  value       = aws_instance.diagx_tf.public_ip
}