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
