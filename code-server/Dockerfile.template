# Install gh and balena CLIs
# Sam Dennon//2022

# Base Image
FROM lscr.io/linuxserver/code-server:4.13.0

# Versions
ENV BALENA_CLI_VERSION=v14.5.12

# Install the repo cert and install gh with some dependencies required by Balena CLI install 
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
  | tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install some stuff for the next step
RUN apt-get update && apt-get install -y wget unzip gh

# Install balena-cli
RUN mkdir -p /config/.local/share/balena-cli ; \
  wget -qO /config/.local/share/balena-cli.zip \
  "https://github.com/balena-io/balena-cli/releases/download/${BALENA_CLI_VERSION}/balena-cli-${BALENA_CLI_VERSION}-linux-x64-standalone.zip"; \
  unzip -o /config/.local//share/balena-cli.zip -d /config/.local/share/ ; \
  rm /config/.local/share/balena-cli.zip ; \
  ln -s /config/.local/share/balena-cli/balena /usr/bin/balena

# Change ownership on the files in /config to stop permission issues later
RUN chown -R abc:abc /config

# Move cont-init.d stuff
COPY root/ /