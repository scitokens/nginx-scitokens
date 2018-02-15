#!/bin/sh

# Make sure the certificates that nginx expects is there:
if [ ! -e /etc/letsencrypt/live/fullchain.pem ]; then
  ln -s /etc/letsencrypt/live/*/fullchain.pem /etc/letsencrypt/live/fullchain.pem
  ln -s /etc/letsencrypt/live/*/privkey.pem /etc/letsencrypt/live/privkey.pem
  ln -s /etc/letsencrypt/live/*/chain.pem /etc/letsencrypt/live/chain.pem
fi

# Start the server
echo "Starting the Authorizer..."
python authorizer.py -c /etc/scitokens-auth/authorizer.cfg &
auth_pid=$!
echo "Auth PID: $auth_pid"

nginx -g "daemon off;"

kill $auth_pid


