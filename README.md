# <img src="logo.png" alt="vs code logo" width="60" /> balenaCodeServer

balenaCodeServer is a free Visual Studio Code based IDE that runs in your browser, served from your Raspberry Pi!

Based on the [linuxserver.io](https://github.com/linuxserver/docker-code-server) code-server Docker image.

Includes the [ZSH Docker Mod](https://github.com/linuxserver/docker-mods/tree/code-server-zsh) Which adds Oh-My-Zsh to your terminal. (Just type `zsh` in the terminal to start using zsh instead of the default bash shell)

---

### Equipment Needed:
* Raspberry Pi (tested on Pi3 B+ and Pi4)
---
### Install
Running this project is as simple as deploying it to a balenaCloud application. You can deploy it in one click by using the button below:

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/SamEureka/balenaCodeServer)

---
### Using balenaCodeServer

* Type <device-ip>:8443 in a browser window _(You can find your device IP address in the Balena Console)_
* The default password for servers deployed with the balena deploy button is `b@13n4!` 
* The default sudu password is `b@13n4!sudu`
* else the password for both is `password`
 

---
### Device Variables:
|Env Variable / Default Value|Function|
|---|---|
|PUID=1000|for UserID|
|PGID=1000|for GroupID|
|TZ=Europe/London| Specify a timezone to use EG Europe/London, America/Los_Angeles|
|PASSWORD=password|Optional web gui password, if PASSWORD or HASHED_PASSWORD is not provided, there will be no auth.|
|HASHED_PASSWORD=|Optional web gui password, overrides PASSWORD, instructions on how to create it is below.|
|SUDO_PASSWORD=password|If this optional variable is set, user will have sudo access in the code-server terminal with the specified password.|
|SUDO_PASSWORD_HASH=|Optionally set sudo password via hash (takes priority over SUDO_PASSWORD var). Format is $type$salt$hashed.|
|PROXY_DOMAIN=code-server.my.domain|If this optional variable is set, this domain will be proxied for subdomain proxying.|
|DEFAULT_WORKSPACE=/config/workspace|If this optional variable is set, code-server will open this directory by default|