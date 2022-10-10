#TAG: ubuntu-latest
ARG SOURCE=ubuntu:latest
FROM ${SOURCE}

# Image updates
RUN apt update
RUN apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends tzdata
RUN apt install -y git curl

# Env
ENV ENV=/etc/profile
ENV NVM_DIR=/usr/local/nvm
ENV PATH=/usr/local/nvm:$PATH

# Node and Yarn Setup
RUN mkdir -p /usr/local/nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
RUN echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> /etc/profile
RUN [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"; \
    nvm install %%NODE_VERSION%%
RUN [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"; \
    npm install --global npm@latest; \
    npm install --global yarn; \
    yarn global add typescript vite; \
    yarn global add create-svelte create-react-app create-next-app create-vite create-vue create-tauri-app
