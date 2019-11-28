#!/usr/bin/env bash

set -e
set -o pipefail # if any code doesn't return 0, exit the script

if [ $NODE_ENV = "production" ]; then
  yarn start
else
  npm run start:dev
fi





function start_client() {
  cd client
  yarn start:dev &
}
