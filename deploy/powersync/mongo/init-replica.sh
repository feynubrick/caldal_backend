#!/bin/bash

MAX_RETRIES=30
RETRY_DELAY=5

for i in $(seq 1 $MAX_RETRIES); do
    # Try to connect and check if MongoDB is ready
    if mongosh --host powersync_storage:27017 \
               --username "${MONGO_INITDB_ROOT_USERNAME}" \
               --password "${MONGO_INITDB_ROOT_PASSWORD}" \
               --eval 'quit(0)' &>/dev/null; then

        # Once we can connect, try to initialize the replica set
        OUTPUT=$(mongosh --host powersync_storage:27017 \
                --username "${MONGO_INITDB_ROOT_USERNAME}" \
                --password "${MONGO_INITDB_ROOT_PASSWORD}" \
                --eval '
        try {
            let status = rs.status();
            if (status.ok) {
                print("SUCCESS: Replica set is already initialized");
                quit(0);
            }
        } catch {}

        let result = rs.initiate({
            _id: "rs0",
            version: 1,
            members: [
                {
                    _id: 0,
                    host: "powersync_storage:27017"
                }
            ]
        });

        if (result.ok) {
            print("SUCCESS: Replica set initialized successfully");
            quit(0);
        } else {
            print("FAILED: " + result.errmsg);
            quit(1);
        }
        ')

        if echo "$OUTPUT" | grep -q "SUCCESS:"; then
            echo "============================================"
            echo "$OUTPUT"
            echo "============================================"
            exit 0
        fi
    fi

    echo "Attempt $i of $MAX_RETRIES failed. Waiting $RETRY_DELAY seconds before retrying..."
    sleep $RETRY_DELAY
done

echo "============================================"
echo "Failed to initialize replica set after $MAX_RETRIES attempts"
echo "============================================"
exit 1