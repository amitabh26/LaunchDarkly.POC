#!/bin/bash

# LaunchDarkly API token (keep this secure!)
API_TOKEN="api-1d9a18c9-c625-46e0-94e3-798d46f4a906"

# Project and environment settings
PROJECT_KEY="sdk-13c430e2-ab20-4c87-9206-d7042340ff24"
ENVIRONMENT_KEY="staging"

# API endpoint
LD_API="https://app.launchdarkly.com/api/v2/flags/$PROJECT_KEY"

# Fetch flags
RESPONSE=$(curl -s -H "Authorization: Bearer $API_TOKE N" -H "Content-Type: application/json" "$LD_API")

# Parse and display flag keys and status for the environment
echo "Feature flags in project '$PROJECT_KEY':"
#echo "$RESPONSE" | jq ".items[] | {key: .key, enabled: .environments.\"staging\".on}"
