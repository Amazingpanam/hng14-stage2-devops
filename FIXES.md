# FIXES.md - Bug Documentation

## Issue #1: Missing health check endpoint
- **File:** api/main.py
- **Line:** N/A (endpoint didn't exist)
- **Problem:** Application had no health check endpoint for Docker
- **Fix:** Added GET /health endpoint returning {"status": "ok"}
- **Impact:** Docker HEALTHCHECK now works properly

## Issue #2: Redis host hardcoded
- **File:** api/main.py, worker/worker.py
- **Line:** (specific line numbers)
- **Problem:** Redis connection used "localhost" instead of environment variable
- **Fix:** Changed to os.getenv('REDIS_HOST', 'redis')
- **Impact:** Services can now connect to Redis container

## Issue #3: Missing dependencies
- **File:** api/requirements.txt
- **Problem:** Missing 'requests' and 'pytest' for testing
- **Fix:** Added to requirements.txt and dev-requirements.txt
- **Impact:** Tests can now run in CI pipeline
