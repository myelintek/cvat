#!/bin/sh

envsubst '$MLSTEAM_CVAT_UUID' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf
