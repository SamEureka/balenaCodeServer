## GitHub & Balena CLI Authentication
---
To use the gh and balena CLIs on balenaCodeServer (bcs) you will need to authenticate/login to the respective services. To do this on balenaCodeServer will require you to generate access tokens for each service, that will be used in the authentication process. This process is very similar in other services or CLIs that you might install on your own balenaCodeServer. I'll provide basic instructions here and links to the documentation if you want to take a deeper dive.

---
### GitHub.com

#### On github.com
* Go to the token generation page at https://github.com/settings/tokens
* Click on the `Generate new token` button
* Give your new token a descriptive name like, `code-server`. This will make it easier to keep track of multiple tokens.
* Select an expiration time or make it perpetual. Do you want to go through this process again in 30-90 days? If not select `does not expire`
* Select the accesses you would like to have in balenaCodeServer. Make sure you understand what you are granting here. Read the help in the top right corner to understand what you are granting.
* Generate the token.
* IMPORTANT! One the next screen you will see your new token. It will look like this: `ghp_dPk94FWALIy1wNFeAsIkuwmOuMR3PB3WcjQW` (not a real token!) Make sure you copy it before leaving the page. It will only be shown ONCE! 

#### On balenaCodeServer
* Open a new Terminal (Ctrl+Shift+`)
* Type `gh auth login --with-token ghp_dPk94FWALIy1wNFeAsIkuwmOuMR3PB3WcjQW` (using your token, not the fake one here)

[gh docs](https://cli.github.com/manual/gh_auth)

---
### Balena.io

#### On Balena.io
* Go to the token generation page at https://dashboard.balena-cloud.com/preferences/access-tokens
* Click on the `Create API key` button
* Give your token a descriptive name and an optional description.
* Create the token
* IMPORTANT! The next modal window will present your API token. It will look like this: `EzqVZFxGvHcFS9BgoTOr7xO1rzqnh0Kk` (not a real token!) Make sure you copy or download the token before closing the modal. It will only be shown ONCE!

#### On balenaCodeServer
* Open a new Terminal (Ctrl+Shift+`)
* Type `balena login --token "EzqVZFxGvHcFS9BgoTOr7xO1rzqnh0Kk"` (using your token, not the fake one here)

[balena cli docs](https://www.balena.io/docs/reference/balena-cli/#login)