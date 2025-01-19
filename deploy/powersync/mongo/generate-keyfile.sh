#!/bin/bash

# Directory for MongoDB keyfile
KEYFILE_DIR="./deploy/powersync/mongo"
KEYFILE_PATH="$KEYFILE_DIR/keyfile.txt"

# Create directory if it doesn't exist
mkdir -p $KEYFILE_DIR

# Generate keyfile with specific format
echo "Generating MongoDB keyfile..."
# Use tr to remove any carriage returns and ensure proper line endings
openssl rand -base64 756 | tr -d '\r' > $KEYFILE_PATH

# Verify file content
if [ -s "$KEYFILE_PATH" ]; then
    echo "Keyfile generated successfully at $KEYFILE_PATH"
else
    echo "Error: Keyfile is empty or was not created properly"
    exit 1
fi
