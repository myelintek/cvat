#!/bin/bash


docker compose -p test_cvat \
       	-f docker-compose.yml \
	-f docker-compose.dev.yml \
	-f components/serverless/docker-compose.serverless.yml \
	-f docker-compose.mlsteam.yml \
	$@
