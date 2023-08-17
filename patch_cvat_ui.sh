#!/bin/sh

echo -n  "Start to path base url to cvat ui"
[ -z ${PREFIX_URL+x} ] && echo "... PREFIX_URL not set" && exit 0

sed -i "s|__PREFIX_URL__|${PREFIX_URL}|g" /usr/share/nginx/html/index.html
sed -i "s|__PREFIX_URL__|${PREFIX_URL}|g" /usr/share/nginx/html/assets/*.js /usr/share/nginx/html/assets/*.map
sed -i "s|__PREFIX_URL__|${PREFIX_URL}|g" /usr/share/nginx/html/assets/3rdparty/*.js /usr/share/nginx/html/assets/3rdparty/*.map

echo " ... done"
