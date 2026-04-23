# FIXES LOG

## API Fixes
- main.py line X: fixed missing endpoint /health
- worker connection issue fixed (redis host was localhost)

## Frontend Fixes
- app.js line X: changed localhost → api service name

## Docker Fixes
- Added multi-stage builds for API, Worker, Frontend
- Added non-root users in all containers
- Added HEALTHCHECK instructions

## Compose Fixes
- Added resource limits
- Fixed environment variable usage
- Fixed Redis networking (no host exposure)

## CI/CD Fixes
- Added Docker registry service
- Fixed missing image tagging (SHA + latest)
- Added caching for Docker builds
- Fixed missing step names
