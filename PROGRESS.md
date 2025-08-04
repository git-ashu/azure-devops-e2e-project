# 🚀 Azure DevOps E2E Project – Progress Tracker

This document tracks the complete end-to-end Azure DevOps project—from infrastructure setup to CI/CD and observability.

---

## ✅ Phase 1: Project Setup

- [x] Create Azure DevOps Organization
- [x] Create project and repo
- [x] Initialize folder structure
- [x] Commit `README.md` and `PROGRESS.md`

---

## ⏳ Phase 2: App Development & Dockerization

- [ ] Develop Python Flask app (`app.py`)
- [ ] Create `requirements.txt` and `Dockerfile`
- [ ] Test image locally
- [ ] Push to `app/` directory in repo

---

## ⏳ Phase 3: Infrastructure as Code (Terraform)

- [ ] Write Terraform scripts to provision:
  - [ ] Azure Kubernetes Service (AKS)
  - [ ] Azure Container Registry (ACR)
  - [ ] (Optional) Azure Key Vault
- [ ] Test with `terraform init/plan/apply`
- [ ] Commit to `terraform/` directory

---

## ⏳ Phase 4: Build Pipeline (CI)

- [ ] Create Azure DevOps CI pipeline:
  - [ ] Docker build
  - [ ] Trivy scan
  - [ ] Push to ACR
- [ ] YAML file: `pipelines/build-pipeline.yml`

---

## ⏳ Phase 5: Release Pipeline (CD)

- [ ] Create Azure DevOps release pipeline:
  - [ ] Deploy to AKS
  - [ ] Use manifests or Helm charts
- [ ] YAML file: `pipelines/deploy-pipeline.yml`

---

## ⏳ Phase 6: Secrets & Configuration

- [ ] Store secrets in Azure Key Vault
- [ ] Reference them in pipeline securely
- [ ] Inject into Kubernetes as environment variables or secrets

---

## ⏳ Phase 7: Monitoring & Logging

- [ ] Set up ELK Stack (Elasticsearch, Logstash, Kibana)
- [ ] Forward app logs with Filebeat
- [ ] Create visualizations in Kibana

---

## ⏳ Phase 8: Documentation & Demo

- [ ] Update `README.md` with usage and architecture
- [ ] Finalize `PROGRESS.md`
- [ ] (Optional) Record walkthrough video or publish blog
- [ ] Share on GitHub and LinkedIn

---

## 🛠️ Tools & Services Used

| Category             | Tool/Service            |
|----------------------|-------------------------|
| Cloud Platform       | Azure                   |
| Infrastructure as Code | Terraform             |
| CI/CD                | Azure DevOps Pipelines  |
| Containerization     | Docker                  |
| Orchestration        | Kubernetes (AKS)        |
| Security Scanning    | Trivy                   |
| Logging & Monitoring | ELK Stack (Filebeat)    |
| Scripting Language   | Python                  |

---

## 📅 Progress Log

| Date       | Task Completed                                |
|------------|-----------------------------------------------|
| 2025-08-04 | Project initialized with README & PROGRESS.md |
