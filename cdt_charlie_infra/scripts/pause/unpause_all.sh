#!/bin/bash

server_ids=$(openstack server list -c ID -f value)

for server_id in $server_ids; do
    if [ "$server_id" == "086e9a72-5aeb-4e74-85ba-87a9e7d4ac0e" ]; then
        echo "Skipping Deploy_box_v2"
        continue
    fi
    echo "Unpausing server: $server_id"
    openstack server unpause "$server_id"
done

echo "All servers paused"
