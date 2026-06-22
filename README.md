# 🔐 DevSecOps Pipeline Lab

## 📖 Overview
This repository contains a hands-on DevSecOps CI/CD pipeline built with **GitHub Actions**. The main objective of this lab is to demonstrate the integration of automated security gates into the software development lifecycle (SDLC), enforcing security-as-code from commit to containerization.

## 🏗️ Pipeline Architecture & Tools
The CI/CD pipeline automatically triggers on every `push` and `pull_request` to the `main` branch, executing the following security phases:

| Phase | Security Practice | Tool Used | Status |
| :--- | :--- | :--- | :--- |
| **SCA** | Software Composition Analysis | Trivy (FS) | 🛠️ In Progress |
| **SAST** | Static Application Security Testing | CodeQL / Semgrep | ⏳ Planned |
| **IaC Scan** | Infrastructure as Code Security | Checkov | ⏳ Planned |
| **Container** | Container Image Hardening Scan | Trivy (Image) | ⏳ Planned |
| **DAST** | Dynamic Application Security Testing | OWASP ZAP | ⏳ Planned |

## 🚀 How to Use & Learnings
*(Here you can document how you configured the tools, how to interpret pipeline failures, and how you fixed vulnerable dependencies or misconfigured Dockerfiles).*
