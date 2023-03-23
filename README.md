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
- Run Pytest:
  ```shell
  docker exec -it backend_django /bin/bash -c "/opt/venv/bin/pytest"
  ```
