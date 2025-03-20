#!/bin/bash

# Check for `api_key=` in staged changes
if git diff --cached | grep -q "api_key="; then
  echo "❌ Commit blocked: Found 'api_key=' in staged changes."
  exit 1 # Prevent commit
fi

exit 0 # Allow commit
