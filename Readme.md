# 🚀 Azure DevOps E2E Project — Flask App on AKS

This project demonstrates a complete DevOps pipeline using **Azure DevOps**, deploying a containerized **Python Flask app** to **Azure Kubernetes Service (AKS)**. It includes Infrastructure as Code with **Terraform**, image scanning with **Trivy**, and centralized logging via the **ELK stack**.

---

## ⚙️ Tech Stack

- **Language:** Python (Flask)
- **Cloud:** Microsoft Azure
- **IaC:** Terraform
- **CI/CD:** Azure DevOps Pipelines
- **Containerization:** Docker
- **Orchestration:** Kubernetes (AKS)
- **Security:** Trivy
- **Monitoring/Logging:** ELK Stack (Elasticsearch, Logstash, Kibana)

---

## 📁 Project Structure

| Folder         | Description                              |
|----------------|------------------------------------------|
| `app/`         | Flask app, requirements.txt, Dockerfile  |
| `terraform/`   | Terraform scripts for ACR + AKS          |
| `manifests/`   | Kubernetes deployment files              |
| `pipelines/`   | Azure DevOps YAML files                  |
| `elk-stack/`   | YAML configs or Helm charts for ELK      |
| `.github/`     | Optional GitHub Action for Trivy         |
| `README.md`    | Project summary & setup guide            |
| `PROGRESS.md`  | Phase-wise implementation tracker        |

---

## 📝 Setup Instructions (Coming Soon)

1. Provision infrastructure with Terraform
2. Build & scan Docker image with Trivy
3. Push to Azure Container Registry (ACR)
4. Deploy to AKS via Azure DevOps
5. Monitor with ELK stack and Azure Monitor

---

## 📌 Status

> Project is currently under development  
> ✅ Initial setup complete  
> 🔧 Terraform and pipelines in progress  

---

## 🙌 Author

**Ashutosh Pandey**  
[LinkedIn](https://linkedin.com/in/ashutoshp1201) • [GitHub](https://github.com/git-ashu)
