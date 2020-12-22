#!/bin/bash

[ -z ${MLSTEAM_CVAT_BASE_URL+x} ] && exit 0
escaped_base_url=$(echo $MLSTEAM_CVAT_BASE_URL | sed 's/\//\\\//g')
echo " Escaped url $escaped_base_url"
echo -n "Start to patch base url $MLSTEAM_CVAT_BASE_URL ..."

sed -i "s/STATIC_URL = '\\/static\\/'/STATIC_URL = '${escaped_base_url}\\/static\\/'/g" /home/django/cvat/settings/base.py
sed -i "s/\\/api\\/v1/${escaped_base_url}\\/api\\/v1/g" /home/django/static/engine/js/*.js
sed -i "s/Worker[(]\"\\/static\\//Worker\\(\"${escaped_base_url}\\/static\\//g" /home/django/static/engine/js/*.js

echo " done"
