# Two stages so node never ships in the runtime image: build the React app,
# then hand the static output to FastAPI, which serves both it and the API
# from one process on one port (see backend/app/main.py).

FROM node:22-slim AS frontend
WORKDIR /build
COPY frontend/package.json frontend/package-lock.json ./
# openapi-typescript still declares a typescript@^5 peer range while this
# project is on 6; it runs fine on 6 (it generated the types in src/types/).
# The lockfile was resolved with this flag, so npm ci needs it to match.
RUN npm ci --legacy-peer-deps
COPY frontend/ ./
RUN npm run build

FROM python:3.13-slim
WORKDIR /app

COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ ./backend/
COPY data/ ./data/
COPY prompts/ ./prompts/
# Path must match what main.py expects: <repo>/frontend/dist
COPY --from=frontend /build/dist ./frontend/dist

WORKDIR /app/backend
EXPOSE 8000
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
