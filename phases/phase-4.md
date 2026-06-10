# Phase 4 — Cloud Infrastructure

**Dates:** Sep 7 – Nov 15, 2026 (Weeks 29–38)
**Certs:** AWS Cloud Practitioner (Oct 5) → Terraform Associate (Oct 19) → AWS SAA (Nov 1) → CKA (Nov 15)
**Goal:** Transform local apps into production-grade, cloud-native systems. Earn 4 certifications.

---

## Key Repos to Clone

```bash
git clone https://github.com/MichaelCade/90DaysOfDevOps
git clone https://github.com/kelseyhightower/kubernetes-the-hard-way
git clone https://github.com/bregman-arie/devops-exercises
```

---

## Certification Schedule

| Cert | Target | Study Hours |
|------|--------|-------------|
| AWS Cloud Practitioner | Oct 5, 2026 | 20 hrs (start Week 30) |
| HashiCorp Terraform Associate | Oct 19, 2026 | 20 hrs |
| AWS Solutions Architect Associate | Nov 1, 2026 | 60 hrs |
| CKA — Certified Kubernetes Administrator | Nov 15, 2026 | 40 hrs |

---

## Week 29 — Linux Fundamentals

| Day | Focus | Task |
|-----|-------|------|
| Mon | File System | Everything is a file. Filesystem hierarchy (`/etc`, `/var`, `/proc`, `/sys`). Permissions (chmod, chown). |
| Tue | Process Management | `ps`, `top`, `htop`, signals, background processes, `systemd` services. |
| Wed | Networking Tools | `netstat`, `ss`, `curl`, `dig`, `traceroute`, `tcpdump` basics. Check open ports on your machine. |
| Thu | Bash Scripting | Variables, loops, functions, conditionals, `$?`, `set -e`. Write a deploy script. |
| Fri | Bash Scripting | Write a script that checks if an API is running, restarts if not, logs output. |
| Sat | Build | Write a Makefile for your project: `make dev`, `make test`, `make build`, `make deploy`. |

---

## Week 30 — Docker ⭐ AWS Cloud Practitioner study starts

| Day | Focus | Task |
|-----|-------|------|
| Mon | Docker Basics | Images vs containers. `docker run`, `docker build`, `docker ps`, `docker logs`. Pull postgres image. |
| Tue | Dockerfile | Multi-stage builds. Layer caching. `.dockerignore`. Write a production Dockerfile. |
| Wed | Docker Compose | Services, volumes, networks, env files. Write `docker-compose.yml` for: API + Postgres + Redis. |
| Thu | Docker Networking | Bridge, host, overlay networks. Container DNS. Service discovery in compose. |
| Fri | Build | Containerize your web app with multi-stage Next.js Dockerfile. |
| Sat | Build | Full stack running in Docker Compose: web + api + db + redis + nginx reverse proxy. |

---

## Week 31 — Kubernetes Fundamentals

| Day | Focus | Task |
|-----|-------|------|
| Mon | K8s Architecture | Control plane (API server, etcd, scheduler, controller manager) + worker nodes (kubelet, kube-proxy). |
| Tue | Core Objects | Pods, ReplicaSets, Deployments. Write manifest for an API deployment. |
| Wed | Services & Networking | ClusterIP, NodePort, LoadBalancer, Ingress. Expose your web app. |
| Thu | ConfigMaps & Secrets | Externalize all config. Add K8s secrets for DB credentials. |
| Fri | Persistent Volumes | PV, PVC, StorageClass. Add persistent storage for Postgres. |
| Sat | Build | Deploy full stack to local K8s (minikube or kind). |

---

## Week 32 — Kubernetes Advanced

| Day | Focus | Task |
|-----|-------|------|
| Mon | Helm | Charts, values files, templating. Install `bitnami/postgresql` and `bitnami/redis` via Helm. |
| Tue | Resource Management | Requests, limits, HPA (Horizontal Pod Autoscaler), VPA. |
| Wed | Health Checks | Liveness, readiness, startup probes. Add to all deployments. |
| Thu | RBAC | ServiceAccounts, Roles, ClusterRoles, RoleBindings. |
| Fri | kubernetes-the-hard-way | Start `kelseyhightower/kubernetes-the-hard-way` — Day 1. |
| Sat | Build | Write a Helm chart for your platform. Parameterize all values. |

> **Oct 5: Take AWS Cloud Practitioner exam**

---

## Week 33 — Terraform + Infrastructure as Code

| Day | Focus | Task |
|-----|-------|------|
| Mon | Terraform Basics | Providers, resources, variables, outputs, state. Write first AWS resource (S3 bucket). |
| Tue | Terraform State | Remote state (S3 + DynamoDB lock). State isolation strategies. |
| Wed | Modules | Write a reusable VPC module. Write an EKS module. |
| Thu | AWS Core | VPC, subnets, security groups, IAM roles + policies. Use Terraform for all of it. |
| Fri | Build | Terraform: provision VPC + EKS cluster + RDS + ElastiCache. |
| Sat | Build | Terraform: add S3 bucket for file uploads + CloudFront CDN. |

---

## Week 34 — CI/CD Pipelines

| Day | Focus | Task |
|-----|-------|------|
| Mon | GitHub Actions Basics | Workflows, jobs, steps, triggers, secrets, environments. |
| Tue | CI Pipeline | Build + test: lint → type-check → test → build Docker image → push to ECR. |
| Wed | CD Pipeline | Deploy: pull new image → `kubectl rollout` → health check → notify. |
| Thu | GitOps | ArgoCD: install on K8s, connect to your repo, sync manifests. |
| Fri | Branch Strategy | Trunk-based development. Feature flags. Environment promotion (dev → staging → prod). |
| Sat | Build | Full CI/CD: push to main → tests → Docker build → push image → ArgoCD syncs → deployed. |

> **Oct 19: Take HashiCorp Terraform Associate exam**

---

## Week 35 — Observability

| Day | Focus | Task |
|-----|-------|------|
| Mon | Logging | Structured JSON logging. ELK stack or CloudWatch logs. |
| Tue | Metrics | Prometheus + Grafana. Instrument your API with custom metrics. |
| Wed | Dashboards | Build Grafana dashboard: request rate, error rate, latency (RED method). |
| Thu | Alerting | AlertManager rules. Alert on: p99 latency > 500ms, error rate > 1%, pod restarts. |
| Fri | Tracing | OpenTelemetry. Add distributed tracing through web → api → db. |
| Sat | Build | Full observability stack deployed to K8s. Runbook for top 3 alert scenarios. |

---

## Week 36 — Cloud Security + Cost

| Day | Focus | Task |
|-----|-------|------|
| Mon | IAM Best Practices | Least privilege. Service accounts. No root access keys. |
| Wed | Secrets Management | AWS Secrets Manager or HashiCorp Vault. Remove all secrets from env files. |
| Thu | Network Security | WAF, security groups, NACLs, private vs public subnets. |
| Fri | Cost Optimization | AWS Cost Explorer. Right-size instances. Spot instances for non-critical workloads. |
| Sat | Build | Security audit: run AWS Trusted Advisor. Fix all critical findings. |

> **Nov 1: Take AWS Solutions Architect Associate exam**

---

## Week 37 — Service Mesh + Advanced Patterns

| Day | Focus | Task |
|-----|-------|------|
| Mon | Service Mesh | Istio or Linkerd concepts. mTLS between services. Traffic management. |
| Tue | Canary Deployments | Argo Rollouts. Deploy v2 to 10% of traffic. |
| Wed | Chaos Engineering | Kill a pod. Kill a node. Verify resilience. |
| Thu | Disaster Recovery | Backup strategy. RTO/RPO targets. Automated DB snapshots. |
| Fri | Cost Architecture | Reserved instances, savings plans, spot fleets. Architect for cost. |
| Sat | Build | Document your full cloud architecture. Draw the production diagram. |

---

## Week 38 — Consolidation + Cert Prep

| Day | Focus | Task |
|-----|-------|------|
| Mon | CKA Review | Study CKA exam domains. Practice `kubectl` speed. |
| Tue | devops-exercises | Work through `bregman-arie/devops-exercises` — K8s and Docker sections. |
| Wed | Mock Scenarios | Scenario: prod is down. Diagnose using only `kubectl`, Prometheus, and logs. |
| Thu | Retrospective | Write Phase 4 retrospective. Document 3 architectural decisions you'd make differently. |
| Sat | Next Phase Prep | Set up Python ML environment: `uv`, PyTorch, Jupyter. |

> **Nov 15: Take CKA (Certified Kubernetes Administrator) exam**

---

## Resources

### Books
- **The DevOps Handbook** — Kim, Humble, Debois, Willis.
- **[Site Reliability Engineering](https://sre.google/books/)** — Google. Free online. The bible for production systems.
- **Terraform: Up & Running** — Brikman. Best practical Terraform resource.
- **Kubernetes in Action** — Luksa. Most complete K8s book.
- **Cloud Native Patterns** — Davis.

### Videos
- **TechWorld with Nana (YouTube)** — Best Docker + K8s + CI/CD channel. Watch everything.
- **Fireship (YouTube)** — Quick cloud concept videos.
- **NetworkChuck (YouTube)** — Linux + networking fundamentals.
- **AWS re:Invent (YouTube)** — Free conference talks from AWS engineers.

### Newsletters
- **The Pragmatic Engineer** — Deep dives on infra at big tech.
- **Last Week in AWS** (Corey Quinn) — Weekly AWS news.
- **Kubernetes Blog** — Official, high quality. Read release notes.
- **AWS Architecture Blog** — Real AWS architecture case studies.

### Exam Prep
- **[killer.sh](https://killer.sh)** — Best CKA/CKAD simulator. Do both practice exams.
- **Stephane Maarek's Udemy courses** — Gold standard for AWS SAA prep.
