# <img src="logo.png" alt="vs code logo" width="60" /> balenaCodeServer

balenaCodeServer is a free Visual Studio Code based IDE that runs in your browser, served from your Raspberry Pi!

* Based on the [linuxserver.io](https://github.com/linuxserver/docker-code-server) code-server Docker image. (v4.9.0)

* Includes:
    * [ZSH Docker Mod](https://github.com/linuxserver/docker-mods/tree/code-server-zsh) Which adds Oh-My-Zsh to your terminal. 
    * [Python3 Docker Mod](https://github.com/linuxserver/docker-mods/tree/code-server-python3) Adding python3 and pip3 (call with `python` and `pip`).
    * [NVM Docker Mod](https://github.com/linuxserver/docker-mods/tree/code-server-nvm) This mod adds Node Version Manager.
    * [Docker-in-Docker Mod](https://github.com/linuxserver/docker-mods/tree/universal-docker-in-docker) Adds Docker-in-Docker (DIND). All docker images run inside the 'code-server' container, sandboxed from the host's docker environment. (*sudo required*)
---

### Equipment Needed
* Raspberry Pi or x86_64 based PC (tested on Pi3 B+, Pi4, and Generic x86_64 (Lenovo M910q))
---
### Install
Running this project is as simple as deploying it to a balenaCloud application. You can deploy it in one click by using the button below:

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/SamEureka/balenaCodeServer)

---
### Using balenaCodeServer

* Type `<device-ip>:8080` in a browser window _(You can find your device IP address in the Balena Console)_
* The default password for servers deployed with the balena deploy button is `b@13n4!` 
* The default sudo password is `b@13n4!sudo`
* else the password for both is `password`

* The GitHub and Balena CLIs are pre-installed. Authentication instructions [here](gh_balena_auth.md).

<!-- This was fixed in https://github.com/SamEureka/balenaCodeServer/pull/12/commits/7145d3db90a1238aa200d451d47e337b08049d0f -->
<!-- * If you get a node version warning when using the balena-cli, installing NVM and a supported version of Node will get rid of the warning. Here are some quick [install instructions](nvm_install.md) --> 

---
### Device Variables
|Env Variable|Default Value|Function|
|---|---|---|
|PORT|8080|code-server port. Default is 8080. The service does not run as 'root'. You cannot set host port <= 1024.|  
|PUID|1000|for UserID|
|PGID|1000|for GroupID|
|GH_TOKEN|ghp_dPk94F...|Populate with GitHub token from [tokens](https://github.com/settings/tokens) page to automate GitHub CLI authentication.|
|SHELL|/usr/bin/zsh|Sets the default terminal shell to ZSH. To use BASH change to '/bin/bash'
|TZ|America/New_York| Specify a timezone to use EG... Europe/London, America/Los_Angeles|
|PASSWORD|password|Optional web gui password, if PASSWORD or HASHED_PASSWORD is not provided, there will be no auth.|
|HASHED_PASSWORD| |Optional web gui password, overrides PASSWORD, instructions on how to create it is below.|
|SUDO_PASSWORD|password|If this optional variable is set, user will have sudo access in the code-server terminal with the specified password.|
|SUDO_PASSWORD_HASH| |Optionally set sudo password via hash (takes priority over SUDO_PASSWORD var). Format is $type$salt$hashed.|
|PROXY_DOMAIN|code-server.my.domain|If this optional variable is set, this domain will be proxied for subdomain proxying.|
|DEFAULT_WORKSPACE|/config/workspace|If this optional variable is set, code-server will open this directory by default|
