#!/bin/bash

echo "Moving core files to project's root $(pwd)/."

mv ./quickview-streaming/.gitignore $(pwd)/
mv ./quickview-streaming/.pre-commit-config.yaml $(pwd)/
mv ./quickview-streaming/docker-compose.yaml $(pwd)/
mv ./quickview-streaming/README.md $(pwd)/
mv ./quickview-streaming/.github $(pwd)/
mv ./quickview-streaming/_clickhouse $(pwd)/
