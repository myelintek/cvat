#!/bin/bash

BASE_URL_KEYWD='__MLS_CVAT_BASE_URL__'

echo -n  "Start to path base url to cvat ui"
[ -z ${MLSTEAM_CVAT_BASE_URL+x} ] && echo "... MLSTEAM_CVAT_BASE_URL not set" && exit 0
escaped_base_url=$(echo $MLSTEAM_CVAT_BASE_URL | sed 's/\//\\\//g')


sed -i "s/$BASE_URL_KEYWD/${escaped_base_url}/g" /usr/share/nginx/html/index.html
sed -i "s/$BASE_URL_KEYWD/${escaped_base_url}/g" /usr/share/nginx/html/*.js /usr/share/nginx/html/*.map
sed -i "s/$BASE_URL_KEYWD/${escaped_base_url}/g" /usr/share/nginx/html/3rdparty/*.js /usr/share/nginx/html/3rdparty/*.map

echo " ... done"
