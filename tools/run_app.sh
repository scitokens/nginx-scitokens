#!/bin/sh

# Start the server
echo "Starting the authenticator..."
python authenticator.py -c /etc/scitokens-auth/authenticator.cfg &
auth_pid=$!
echo "Auth PID: $auth_pid"

nginx -g "daemon off;"

kill $auth_pid

