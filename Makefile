.PHONY: install dev types test

install:
	cd backend && python3 -m venv .venv && . .venv/bin/activate && pip install -q -r requirements.txt
	cd frontend && npm install

# Regenerate frontend/src/types/api.ts from the backend's Pydantic models -
# run this after changing anything in backend/app/models.py.
# openapi-typescript runs via npx rather than as a devDependency: it's a
# one-shot codegen tool the build never needs, and its stale typescript@^5
# peer range broke `npm install` for anyone cloning fresh.
types:
	cd backend && . .venv/bin/activate && python scripts/export_openapi.py
	cd frontend && npx -y openapi-typescript@7 openapi.json -o src/types/api.ts
	rm frontend/openapi.json

test:
	cd backend && . .venv/bin/activate && python -m pytest -q

dev:
	@echo "Starting backend (:8000) and frontend (:5173) - Ctrl+C stops both"
	@trap 'kill 0' EXIT; \
	(cd backend && . .venv/bin/activate && uvicorn app.main:app --reload --port 8000) & \
	(cd frontend && npm run dev) & \
	wait
