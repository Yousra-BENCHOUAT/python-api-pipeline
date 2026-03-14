Python API Pipeline

Description:

Ce projet est un pipeline DevSecOps complet deploye sur Microsoft Azure. Une API Python FastAPI est containerisee avec Docker, testee et scannee automatiquement via GitHub Actions, puis deployee sur un cluster Kubernetes AKS avec un monitoring en temps reel via Prometheus et Grafana.

Ce que j'ai fait:

J'ai commence par creer une API REST avec FastAPI qui expose quatre endpoints : la page d'accueil, le health check, la liste des items et la recuperation d'un item par son ID. J'ai ecrit cinq tests automatiques avec Pytest pour verifier que chaque endpoint repond correctement, puis j'ai containerise l'application avec Docker.
Ensuite j'ai mis en place un pipeline CI/CD avec GitHub Actions qui se declenche automatiquement a chaque commit. Le pipeline execute les tests automatiques, scanne le code Python avec Bandit pour detecter les vulnerabilites de securite, construit l'image Docker et la scanne avec Trivy pour verifier qu'elle ne contient pas de failles connues.
Pour le deploiement j'ai cree un Azure Container Registry pour stocker les images Docker, puis un cluster Kubernetes AKS sur Azure avec deux replicas de l'application et un LoadBalancer pour distribuer le trafic et rendre l'application accessible depuis internet.
Enfin j'ai installe Prometheus et Grafana sur le cluster avec Helm pour monitorer en temps reel le CPU, la memoire et le trafic reseau de tous les pods qui tournent sur le cluster.

Stack technique:

FastAPI, Docker, GitHub Actions, Bandit, Trivy, Azure Container Registry, Kubernetes AKS, Helm, Prometheus, Grafana
