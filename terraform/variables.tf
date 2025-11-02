# AWS Region
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS CLI profile to use"
  type        = string
  default     = "default"
}

# VPC CIDR Block
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

# Public Subnet CIDR Blocks
variable "public_subnet_1_cidr" {
  description = "CIDR block for public subnet 1"
  type        = string
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR block for public subnet 2"
  type        = string
  default     = "10.0.2.0/24"
}

# Private Subnet CIDR Blocks
variable "private_subnet_1_cidr" {
  description = "CIDR block for private subnet 1"
  type        = string
  default     = "10.0.3.0/24"
}

variable "private_subnet_2_cidr" {
  description = "CIDR block for private subnet 2"
  type        = string
  default     = "10.0.4.0/24"
}

# Availability Zones
variable "availability_zone_1" {
  description = "Availability Zone 1"
  type        = string
  default     = "us-east-1a"
}

variable "availability_zone_2" {
  description = "Availability Zone 2"
  type        = string
  default     = "us-east-1b"
}

# My Machine IP (for RDS access)
variable "my_machine_ip" {
  description = "Your machine's public IP address (for RDS access)"
  type        = string
}

# RDS Configuration
variable "db_name" {
  description = "Name of the RDS database"
  type        = string
  default     = "demo_db"
}

variable "db_username" {
  description = "Username for the RDS database"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Password for the RDS database"
  type        = string
  default     = "ChangeMeToAStrongPassword123!"
  sensitive   = true
}

variable "db_instance_class" {
  description = "Instance class for the RDS database"
  type        = string
  default     = "db.t3.micro"
}

variable "db_engine" {
  description = "Database engine for RDS"
  type        = string
  default     = "mysql"
}

variable "db_engine_version" {
  description = "Engine version for RDS"
  type        = string
  default     = "8.0"
}

variable "db_allocated_storage" {
  description = "Allocated storage for RDS (in GB)"
  type        = number
  default     = 20
}
