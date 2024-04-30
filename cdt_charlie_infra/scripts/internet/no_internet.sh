#!/bin/bash

# Security group to add
SEC_GROUP_ADD="34b404ff-f6e8-4a39-8cc8-ca9136e3e226"

# Security group to remove
SEC_GROUP_REMOVE="8f09a9f5-8167-4d45-813b-e9283679918a"

# List all servers and extract the IDs
server_ids=$(openstack server list -c ID -f value)

# Loop through each server ID
    for server_id in $server_ids; do
    if [ "$server_id" == "086e9a72-5aeb-4e74-85ba-87a9e7d4ac0e" ]; then
        echo "Skipping server with ID: $server_id"
        continue
    fi
    echo "Modifying server: $server_id"

    # Add the security group to the server
    echo "Adding security group $SEC_GROUP_ADD"
    openstack server add security group $server_id $SEC_GROUP_ADD

    # Remove the security group from the server
    echo "Removing security group $SEC_GROUP_REMOVE"
    openstack server remove security group $server_id $SEC_GROUP_REMOVE

    echo "Modification completed for server: $server_id"
done

echo "All servers have been processed."

