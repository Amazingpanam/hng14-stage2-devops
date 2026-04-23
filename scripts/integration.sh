#!/bin/bash

set -e

echo "Starting stack..."
docker compose up -d --build

sleep 20

echo "Submitting job..."
JOB=$(curl -s -X POST http://localhost:3000/submit | jq -r '.job_id')

echo "Job ID: $JOB"

for i in {1..10}
do
  STATUS=$(curl -s http://localhost:8000/jobs/$JOB | jq -r '.status')

  echo "Status: $STATUS"

  if [ "$STATUS" = "completed" ]; then
    echo "SUCCESS"
    docker compose down
    exit 0
  fi

  sleep 2
done

echo "FAILED"
docker compose down
exit 1
