# balenaCodeServer

***This Works***

|Env Variable / Default Value|Function|
|---|---|
|PUID=1000|for UserID - see below for explanation|
|PGID=1000|for GroupID|
|TZ=Europe/London| Specify a timezone to use EG Europe/London, America/Los_Angeles|
|PASSWORD=password|Optional web gui password, if PASSWORD or HASHED_PASSWORD is not provided, there will be no auth.|
|HASHED_PASSWORD=|Optional web gui password, overrides PASSWORD, instructions on how to create it is below.|
|SUDO_PASSWORD=password|If this optional variable is set, user will have sudo access in the code-server terminal with the specified password.|
|SUDO_PASSWORD_HASH=|Optionally set sudo password via hash (takes priority over SUDO_PASSWORD var). Format is $type$salt$hashed.|
|PROXY_DOMAIN=code-server.my.domain|If this optional variable is set, this domain will be proxied for subdomain proxying.|
|DEFAULT_WORKSPACE=/config/workspace|If this optional variable is set, code-server will open this directory by default|