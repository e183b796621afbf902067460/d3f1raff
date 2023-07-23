# ylab-backend-engineer

---

Project which implements the restaurant business-logic.

# Configuration

First of all to configure FastAPI correctly need to do next steps:

- Clone current repository:
```
git clone https://github.com/e183b796621afbf902067460/ylab-backend-engineer.git
```

- Get into the project folder:
```
cd ylab-backend-engineer/
```

# Docker

- Run docker compose (`sudo`):
```
docker-compose up -d --build --force-recreate
```

- To stop docker-containers (`sudo`):
```
docker-compose down
```

# Documentation
FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at http://localhost:8000/docs.
