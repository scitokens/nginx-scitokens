SciTokens Web Authorizer
===========================

This Authorizer is designed to work with a webserver to permit or deny access
to resources given a [SciToken](https://scitokens.org/).

This repo also includes the necessary configuration for an NGINX webserver to provide WebDav access using SciTokens for authorization.  With this configuration, you may provide authenticated access to write (PUT) or read (GET) on the webserver.

Authorizer configuration
------------------------

The Authorizer works along with the webserver, NGINX in this case, to determine if a specific action is authorized given a SciToken.  

An example configuration is provided in [configs/authorizer.cfg](configs/authorizer.cfg).

    [Global]
    audience = testing

    [Issuer OSG-Demo]

    issuer = https://demo.scitokens.org
    base_path = /protected

* `audience`: The audience that the service should respond.  Any tokens attempting to access this resource must have exactly the same audience.
* `Issuer`: A list of possible multiple issuers which will be accepted to access this resource.
* `issuer`: The URL path of the issuer which will respond with the OAuth public key retrieval.
* `base_path`: The base path for which this issuer may access.  All URL's must be prepended by this base_path.  But, tokens should not include this base path.

For example, imagine attempting to access the resource at `/protected/important/data`.

* The `base_path` is shown in the configuration above, which is `/protected`
* The `scp` (scope) in the token must be at the least `read:/important`
* The URL that is requested must be `/protected/important/data`

The configuration above should not be used in production.  Since it is using the demo.scitokens.org issuer, anyone can create a scitoken from that issuer that could read or write to your server.

Installation
------------

### Securing Server with LetsEncrypt

SciTokens are passed unencrypted in the HTTP headers, therefore it is recommended to encrypt the connection with HTTPS.  Here we will discuss how to use [LetsEncrypt](https://letsencrypt.org/) to secure your server.  If you already have an SSL certificate that you would like to use, you may skip this section.

You may run certbot directly from docker with the following command.  You will need to replace the `email` and the domain (`-d` option).  The domain should be the public hostname of the server that will be running this service.

    sudo docker run -v `pwd`/certs:/etc/letsencrypt --net=host --rm certbot/certbot certonly --standalone --email <email> -d <domain> --agree-tos

After you run this command, it should report success and your certificates will be located in the `certs` directory.  To renew the certificate, run the command:

    sudo docker run -v `pwd`/certs:/etc/letsencrypt --net=host --rm certbot/certbot renew --standalone --email <email> -d <domain> --agree-tos

Full instructions on how to run [CertBot](https://certbot.eff.org/) is available on the official webiste.

### NGINX Configuration

An example NGINX configuration is provided in [nginx.conf](configs/nginx.conf) within the configs directory.  It will enable HTTPS and use the provided python script for authorization.

If you would like to built-in NGINX, the configuration should replace the existing `nginx.conf` configuration file.

Running from Docker
-------------------

A [NGINX-SciTokens](https://hub.docker.com/r/scitokens/nginx-scitokens/) Docker container is provided.  You may run the command directly using `docker`, or use something like [docker-compose](https://docs.docker.com/compose/) to manage the container for you.  An example [`docker-compose.yml`](docker-compose.yml) file is provided.

From the command line, the command would be:

    sudo docker run --net=host -v `pwd`/certs:/etc/letsencrypt -v `pwd`/data:/data scitokens/nginx-scitokens
    
In this command, it would expect the LetsEncrypt command from before to be executed.  The certificates should be in `./certs`.  Further, it will read / write all data from the `./data` directory.

Testing Your Installation
-------------------------

Testing your installation is dependent on a lot of factors:

* The issuer that you will be using
* The directory structure
* Permissions that should be tested (read/write)

But, if you used the default configuration above (which would leave your server open to read or write from anyone), then you can test it with a provided script.  You will have to edit the script, near the top, with some values that pertain to your server.  You should only have to edit the hostname.


