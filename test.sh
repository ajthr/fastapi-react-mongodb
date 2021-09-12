#!/bin/bash

# Exit in case of error
set -e

# Run this from the root of the project
cookiecutter --no-input -f ./ project_name="test"

cd test

docker-compose build
docker-compose down -v --remove-orphans
docker-compose up -d

# Run api tests
docker-compose run --rm api sh -c "pytest"

# Run web tests
docker-compose run --rm web sh -c "CI=true npm run test"

# Cleanup
docker-compose down -v --remove-orphans
cd ..
rm -rf test

# Print result
echo "\033[0;32m Test Passed."
