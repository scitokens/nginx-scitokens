#!/bin/sh

# Start the server
python authenticator.py -c /etc/scitokens-auth/authenticator.cfg &

nginx -g "daemon off;"



