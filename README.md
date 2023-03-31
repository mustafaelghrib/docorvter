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
