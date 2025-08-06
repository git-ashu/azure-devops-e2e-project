# 📘 DevOps Project Progress Tracker – Azure DevOps E2E (FastAPI on AKS)

## 🔗 Project Links

- **GitHub Repo:** https://github.com/git-ashu/azure-devops-e2e-project  
- **Azure DevOps Project:** https://dev.azure.com/testashuazure/azureexamprep

---

## 📅 8-Day DevOps Execution Plan

| Day | Focus Area                       | Status       | Notes                           |
|-----|----------------------------------|--------------|---------------------------------|
| Day 1 | Scaffold FastAPI App & Dockerize | ✅ Completed | App base + tests + Docker done |
| Day 2 | Terraform Infra (AKS, ACR, Vault) | ✅ Completed | Infra applied + connected to AKS |
| Day 3 | Helm Chart + AKS Deploy          | ⬜ Not Started |                                 |
| Day 4 | CI Pipeline (Build + Scan + Push) | ⬜ Not Started |                                 |
| Day 5 | CD Pipeline (Helm Deploy)        | ⬜ Not Started |                                 |
| Day 6 | Security (Snyk, Secrets, Harden AKS) | ⬜ Not Started |                                 |
| Day 7 | Monitoring (App Insights, Logs)  | ⬜ Not Started |                                 |
| Day 8 | Docs & AZ-400 Exam Prep          | ⬜ Not Started |                                 |

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
  - [x] Resource Group  
  - [x] AKS cluster  
  - [x] Azure Container Registry  
  - [x] Azure Key Vault  
  - [ ] Log Analytics Workspace *(optional, can do later)*  
- [x] Run `terraform init`, `plan`, `apply`  
- [x] Connect to AKS using `kubectl`  
- [x] Build Docker image and push to ACR  
- [x] Test app manually using Postman

---

### 📌 Day 3 – Helm Chart + Deploy

- [ ] Create `/charts/payment-service/`  
- [ ] Write `Chart.yaml`, `values.yaml`, templates  
- [ ] Add Kubernetes `deployment.yaml`, `service.yaml`  
- [ ] Use `values.yaml` for image, config, secrets  
- [ ] Test deployment to AKS with Helm  
- [ ] Confirm app reachable via public IP

---

### 📌 Day 4 – CI Pipeline (Azure Pipelines)

- [ ] Create `azure-pipelines.yml`  
- [ ] Steps:  
  - Install dependencies  
  - Run `pytest`  
  - Run SonarCloud scan  
  - Build Docker image  
  - Push to ACR  
- [ ] Run pipeline on GitHub commits

---

### 📌 Day 5 – CD Pipeline (Azure Pipelines)

- [ ] Extend pipeline to deploy via Helm  
- [ ] Add AKS auth step  
- [ ] Use `kubectl` + `helm` to deploy  
- [ ] Separate stages for Dev → Staging → Prod  
- [ ] Add manual approval step between environments

---

### 📌 Day 6 – Security & Hardening

- [ ] Add Snyk or Trivy to pipeline  
- [ ] Run image vulnerability scan  
- [ ] Use Key Vault for secrets  
- [ ] Add Git secret scanning (e.g., GitGuardian)  
- [ ] Harden AKS with RBAC & network policies

---

### 📌 Day 7 – Monitoring & Alerts

- [ ] Enable Azure Monitor for AKS  
- [ ] Add Application Insights SDK to app  
- [ ] Send logs and metrics  
- [ ] Set up alerts for latency, 500 errors, etc.  
- [ ] Create dashboard in Azure Monitor

---

### 📌 Day 8 – Documentation & AZ-400 Review

- [ ] Finalize `README.md` and `progress.md`  
- [ ] Add architecture diagram (optional)  
- [ ] Add links to pipeline runs & dashboards  
- [ ] Map features to AZ-400 exam objectives  
- [ ] Review Microsoft Learn + do mock test

---

## 🧭 Current Phase

> **Day:** 3  
> **Goal:** Helm-based Kubernetes Deployment  
> **Next:** Scaffold chart folder and write templates

---

_Last updated: 2025-08-06_
 
