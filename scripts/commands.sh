#!/bin/sh

# Exit on error
set -e

# Script modules
wait_psql.sh
collectstatic.sh
migrate.sh
runserver.sh
