provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "UpSales-BizHub"
      Environment = var.environment
      ManagedBy   = "Terraform"
      Owner       = "Upskill Consultancy Inc"
      Platform    = "Enterprise Automation"
      Repository  = "upsales-bizhub-infra"
    }
  }
}

module "vpc" {
  source = "../../modules/vpc"

  environment = var.environment
  vpc_cidr    = var.vpc_cidr
  azs         = var.availability_zones

  public_subnet_cidrs = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]

  private_subnet_cidrs = [
    "10.0.10.0/24",
    "10.0.11.0/24",
    "10.0.12.0/24"
  ]
}

module "eks" {
  source = "../../modules/eks"

  environment        = var.environment
  cluster_name       = "upsales-dev-eks"
  kubernetes_version = "1.30"

  private_subnet_ids = module.vpc.private_subnet_ids

  desired_capacity = 1
  min_capacity     = 1
  max_capacity     = 2

  instance_types = ["t3.medium"]
}

module "rds" {
  source = "../../modules/rds"

  environment        = var.environment
  db_name            = "upsalesdb"
  db_username        = var.db_username
  db_password        = var.db_password
  private_subnet_ids = module.vpc.private_subnet_ids
  vpc_id             = module.vpc.vpc_id
  instance_class     = "db.t3.micro"
}