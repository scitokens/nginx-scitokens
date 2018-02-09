SciTokens Web Authenticator
===========================

This authenticator is designed to work with a webserver to permit or deny access
to resources given a SciToken.


Authenticator configuration
---------------------------

An example configuration is provided in [configs/authenticator.cfg](configs/authenticator.cfg).

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

NGINX Configuration
-------------------

An example nginx configuration is shown in [nginx.conf](configs/nginx.conf) within the configs directory.


