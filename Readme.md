# ⚙️ Azure DevOps End-to-End Project (FastAPI on AKS)

A complete CI/CD DevOps project using **Python (FastAPI)** deployed on **Azure Kubernetes Service (AKS)**, using **Azure DevOps Pipelines**, **Terraform**, **Helm**, and full lifecycle tools (security, monitoring, and secrets management).

---

## 🚀 Project Summary

| Component     | Tool/Stack                         |
|---------------|------------------------------------|
| Language      | Python 3.11 + FastAPI              |
| Infra as Code | Terraform                          |
| CI/CD         | Azure Pipelines                    |
| Container     | Docker + Azure Container Registry  |
| Deployment    | AKS via Helm Charts                |
| Secrets       | Azure Key Vault                    |
| Monitoring    | Azure Monitor + App Insights       |
| Security      | Snyk or Trivy                      |

---

## 📂 Project Structure

azure-devops-e2e-project/
├── src/
│ └── payment-service/
│ ├── app/
│ │ └── main.py
│ ├── tests/
│ │ └── test_main.py
│ ├── Dockerfile
│ └── requirements.txt
├── infra/
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── charts/
│ └── payment-service/
│ ├── Chart.yaml
│ ├── values.yaml
│ └── templates/
├── azure-pipelines.yml
├── progress.md
└── README.md



---

## 🎯 Features

- ✅ FastAPI microservice (`/payments` API)
- ✅ Unit testing with pytest
- ✅ Docker containerization
- ✅ AKS cluster provisioned via Terraform
- ✅ Helm chart for application deployment
- ✅ Azure Pipelines (CI + CD) with approval gates
- ✅ Secrets managed via Azure Key Vault
- ✅ Code quality checks with SonarCloud
- ✅ Vulnerability scanning with Snyk or Trivy
- ✅ Monitoring via Azure Monitor and Application Insights

---

## 📦 Setup Instructions

### 🔧 Prerequisites

- Azure Subscription
- Azure DevOps Organization
- GitHub account
- Terraform v1.5+
- Docker
- Python 3.11+
- Azure CLI
- Kubectl
- Helm v3+

---

## 🛠️ Step-by-Step Execution

| Phase | Description | Status |
|-------|-------------|--------|
| Day 1 | Scaffold FastAPI App & Dockerize | ⬜ |
| Day 2 | Terraform Infra (AKS, ACR, Vault) | ⬜ |
| Day 3 | Helm Chart + AKS Deployment | ⬜ |
| Day 4 | Azure DevOps CI Pipeline | ⬜ |
| Day 5 | Azure DevOps CD Pipeline | ⬜ |
| Day 6 | Security & Vulnerability Checks | ⬜ |
| Day 7 | Monitoring & Alerts | ⬜ |
| Day 8 | Final Docs & AZ-400 Review | ⬜ |

➡️ See [`progress.md`](./progress.md) for full daily checklist.

---

## 🔒 Security & Best Practices

- Secrets stored in Azure Key Vault
- Pipelines never expose credentials
- RBAC + Network Policies enforced in AKS
- Snyk/Trivy scans on Docker images and code
- Git secrets scanning (GitGuardian or native)

---

## 📊 Monitoring Setup

- Application Insights SDK added to FastAPI
- Logs and metrics pushed to Azure Monitor
- Alerts for 500 errors, latency, and availability
- Optional: Grafana dashboard from Azure Monitor

---

## 📘 Useful Commands

```bash
# Run app locally
uvicorn app.main:app --reload

# Test app
pytest

# Build Docker image
docker build -t payment-api .

# Run Docker container
docker run -p 8000:8000 payment-api

# Helm install to AKS
helm upgrade --install payment charts/payment-service --namespace dev
