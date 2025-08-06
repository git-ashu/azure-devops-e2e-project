# 📘 DevOps Project Progress Tracker – Azure DevOps E2E (FastAPI on AKS)

## 🔗 Project Links

- **GitHub Repo:** https://github.com/git-ashu/azure-devops-e2e-project  
- **Azure DevOps Project:** https://dev.azure.com/testashuazure/azureexamprep

---

## 📅 8-Day DevOps Execution Plan

| Day | Focus Area                       | Status       | Notes                                   |
|-----|----------------------------------|--------------|-----------------------------------------|
| Day 1 | Scaffold FastAPI App & Dockerize | ✅ Completed | App base + tests + Docker done          |
| Day 2 | Terraform Infra (AKS, ACR, Vault) | ✅ Completed | Infra applied, image pushed, tested     |
| Day 3 | Helm Chart + AKS Deploy          | ⬜ Not Started | Charts + Helm deploy next               |
| Day 4 | CI Pipeline (Build + Scan + Push) | ⬜ Not Started | Azure Pipelines CI setup                |
| Day 5 | CD Pipeline (Helm Deploy)        | ⬜ Not Started | Helm-based CD with approvals            |
| Day 6 | Security (Snyk, Secrets, Harden AKS) | ⬜ Not Started | Start moving tfstate to remote backend  |
| Day 7 | Monitoring (App Insights, Logs)  | ⬜ Not Started |                                           |
| Day 8 | Docs & AZ-400 Exam Prep          | ⬜ Not Started | Final polish + Exam-oriented review     |

---

## ✅ Daily To-Do Breakdown

### 📌 Day 1 – FastAPI App Scaffold

- [x] Create `/src/payment-service/app/` structure  
- [x] Add FastAPI `main.py` with `/payments` POST route  
- [x] Use Pydantic for validation  
- [x] Add `pytest` tests for endpoint  
- [x] Create `requirements.txt`  
- [x] Add `Dockerfile` + `.dockerignore`  
- [x] Build and run app locally with Docker  
- [x] Push to GitHub repo  

---

### 📌 Day 2 – Terraform Infra (AKS + ACR + Key Vault)

- [x] Setup Terraform project in `/infra`  
- [x] Write `main.tf`, `variables.tf`, `outputs.tf`  
- [x] Create:  
  - Resource Group  
  - AKS cluster  
  - Azure Container Registry  
  - Azure Key Vault  
  - Log Analytics Workspace  
- [x] Run `terraform init`, `plan`, `apply`  
- [x] Connect to AKS using `kubectl`  
- [x] Build Docker image and push to ACR  
- [x] Test app endpoint manually via Postman  
- [x] Push code to GitHub (cleaned `.gitignore`)  

---

### 🛡️ Upcoming Hardening Tasks (Start Day 3 or 6)

- [ ] Move Terraform state to Azure Blob Storage (remote backend)  
- [ ] Add `.gitignore` entries for `.terraform/`, state files  
- [ ] Rotate leaked secrets (ACR login)  
- [ ] Add secret scanning rules / GitHub protection  
- [ ] Start planning Key Vault integration with workloads  
- [ ] Add Trivy/Snyk for Docker scan later in CI  

---

## 🧭 Current Phase

> **Day:** 3  
> **Goal:** Helm chart + AKS deployment  
> **Next:** Write Helm chart & test Helm-based app deployment

---

_Last updated: 2025-08-06_
 
