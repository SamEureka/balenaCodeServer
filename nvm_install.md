# Update 10/04/2022:
## The install method of the balena-cli has be migrated away from npm in favor of the standalone ZIP release. This change was made to insure the most recent version was available and to remove any reliance on outdated versions of node.

## //Sam

## ~~Balena CLI node version~~

~~You may get a node version warning when trying to use balena-cli. The easiest fix is to install Node Version Manager (NVM) on your balenaCodeServer. This method also gives you more control over what version you are running. If you need a specific version for a project, changing is as easy as typing `nvm install vX.X.X` in the terminal!~~

### ~~Install Steps~~

~~1. Open a terminal window on your balenaCodeServer.
2. Run this command `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`
3. Close the terminal and open a new one
4. Run this command `nvm install v12.22.10` (latest version supported by the cli)
5. Enjoy balena-cli without node version warnings~~