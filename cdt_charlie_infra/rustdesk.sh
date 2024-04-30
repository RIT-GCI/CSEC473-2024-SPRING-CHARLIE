#!/bin/bash
wget https://github.com/rustdesk/rustdesk/releases/download/1.2.3/rustdesk-1.2.3-x86_64.deb -O /tmp/rustdesk.deb
apt-get update

apt-get install -fy /tmp/rustdesk.deb > null

apt-get install -yq pwgen screen

rustdesk_pw=`pwgen -1 -A -0 -B`

rustdesk_config="9JiI6ISeltmIsIiI6ISawFmIsICOzEjLzMjLxIjL5ITMiojI5FGblJnIsICOzEjLzMjLxIjL5ITMiojI0N3boJye"

/bin/bash -l -c "/usr/bin/rustdesk --password $rustdesk_pw"

/bin/bash -l -c "/usr/bin/rustdesk --config \"$rustdesk_config\""

systemctl restart rustdesk

sleep 15

/bin/bash -l -c "/usr/bin/rustdesk --password $rustdesk_pw"

/bin/bash -l -c "/usr/bin/rustdesk --config \"$rustdesk_config\""

/bin/bash -l -c "/usr/bin/rustdesk --password $rustdesk_pw"

rustdesk_id=$(rustdesk --get-id)

systemctl restart rustdesk

echo $rustdesk_id -- $rustdesk_pw
