#!/usr/bin/env bash

set -e
set -o pipefail # if any code doesn't return 0, exit the script
cd client
if [[ $NODE_ENV = "production" ]]; then
  yarn start
else
  yarn run dev-server
fi



# function start_client() {
#   if [[ $NODE_ENV = "production" ]]; then
#     yarn start
#   else
#     yarn run dev-server
#   fi
# }

# start_client
