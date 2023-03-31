## Docorvter
A Document Converter Backend API

---

## Backend:

### Run The Backend Locally:
- Copy `backend/.env.sample` file, rename it to `backend/.env` and update it.
- Run The Backend API:
  ```shell
  docker compose -f backend/docker-compose.yml up -d --build
  ```

### Run The Tests:
- Run Pytest:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/pytest -rP"
  ```
- Run Pytest Coverage:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/pytest --cov=."
  ```

### Docs:
- Check Docs Coverage:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/interrogate -v ."
  ```
- Check Docs Style:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/pydocstyle ."
  ```
- Show Docs Locally:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/mkdocs serve"
  ```
- Deploy Docs to Repo GitHub Pages:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/mkdocs gh-deploy"
  ```

---
