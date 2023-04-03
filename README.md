## Docorvter
A Document Converter Backend API

---

## The Development Environment:

### Run The Backend Locally:
- Copy `backend/.env.sample/.env.development` to `backend/.env/.env.development` and update it.
- Run The Backend API:
  ```shell
  docker compose -f backend/.docker-compose/development.yml up -d --build
  ```

### Run The Tests:
- Run Pytest:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "/opt/venv/bin/pytest -rP"
  ```
- Run Pytest Coverage:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "/opt/venv/bin/pytest --cov=."
  ```

### Docs:
- Check Docs Coverage:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "/opt/venv/bin/interrogate -v ."
  ```
- Check Docs Style:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "/opt/venv/bin/pydocstyle ."
  ```
- Copy `docs` and `mkdocs.yml` to The Container:
  ```shell
  docker cp mkdocs.yml backend_development_django:/mkdocs.yml
  docker cp docs backend_development_django:/docs
  ```
- Show Docs Locally:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "cd .. && /opt/venv/bin/mkdocs serve --dev-addr 127.0.0.1:9000"
  ```
- Deploy Docs to GitHub Pages:
  ```shell
  docker exec -it backend_development_django /bin/bash -c "cd .. && /opt/venv/bin/mkdocs gh-deploy"
  ```

---

## The Production Environment:

### Run The Backend Locally:
- Setup and run the [infrastructure](#Infrastructure)
- Get the environment variables from the infrastructure:
  ```shell
  python scripts/get_infra_output.py --c=infrastructure/.docker-compose.yml --m=aws --f=env
  ```
- Copy `backend/.env.sample/.env.production` to `backend/.env/.env.production` and update it.
- Run The Backend API:
  ```shell
  docker compose -f backend/.docker-compose/production.yml up -d --build
  ```

### Deploy Manually on Minikube with Docker and Kubernetes:
- Export Values:
  ```shell
  export ENVIRONMENT=production;
  export PROJECT_NAME=docorvter;
  export DOCKER_HUB=mustafaabdallah;
  export FINAL_IMAGE=$DOCKER_HUB/$PROJECT_NAME
  export NAMESPACE="$PROJECT_NAME-namespace"
  ```
- Build a Docker Image:
  ```shell
  docker build -t $FINAL_IMAGE -f backend/Dockerfile backend --build-arg ENVIRONMENT=$ENVIRONMENT
  ```
- Push to Docker Hub:
  ```shell
  docker push $FINAL_IMAGE
  ```
- Run The Image Locally:
  ```shell
  python3 scripts/run_backend.py --env=backend/.env/.env.production --image=$FINAL_IMAGE
  ```

- Create a Namespace
  ```shell
  kubectl create namespace $NAMESPACE
  ```
- Create Kubernetes secret from the env file
  ```shell
  kubectl create secret generic "$PROJECT_NAME-env-secrets" \
  --from-env-file=.env/.env.production \
  --namespace=$NAMESPACE
  ```
- Apply Kubernetes deployment and service
  ```shell
  kubectl apply -f .kubernetes/deployment.yml
  kubectl apply -f .kubernetes/service.yml
  ```
- Change namespace
  ```shell
  kubectl config set-context --current --namespace=$NAMESPACE
  ```
- Launch the app
  ```shell
  minikube service -n $NAMESPACE --url $PROJECT_NAME
  ```
- Delete a Namespace
  ```shell
  kubectl delete namespace $NAMESPACE
  ```

---

## Infrastructure

**Setup Terraform Backend:**
- Set Bucket Name:
  ```shell
  export BUCKET_NAME=docorvter-terraform-backend;
  ```
- Create a Bucket on AWS S3.
  ```shell
  aws s3api create-bucket --bucket $BUCKET_NAME --region us-east-1
  ```
- Empty The Bucket
  ```shell
  aws s3 rm s3://$BUCKET_NAME --recursive
  ```
- Delete The Bucket
  ```shell
  aws s3api delete-bucket --bucket $BUCKET_NAME
  ```
- Create a file and name it to `.backend.hcl` under `infrastructure` folder.
- Copy the content of file `.backend.hcl.sample` inside it and fill the values.

**Setup Secrets:**
- Create a file with the name `.secrets.auto.tfvars` under `infrastructure` folder.
- Copy the contents of file `.secrets.auto.tfvars.sample` inside it and fill the values.

**Run Terraform Commands:**

- terraform init
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform init -backend-config=.backend.hcl
  ```

---

- terraform plan all
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform plan
  ```
- terraform plan aws
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform plan -target="module.aws"
  ```

---

- terraform apply all
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform apply --auto-approve
  ```
- terraform apply aws
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform apply -target="module.aws" --auto-approve
  ```

---

- terraform destroy all
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform destroy --auto-approve
  ```
- terraform destroy aws
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform destroy -target="module.aws" --auto-approve
  ```

---

- terraform output aws
  ```shell
  docker compose -f infrastructure/.docker-compose.yml run --rm terraform output aws
  ```

---
