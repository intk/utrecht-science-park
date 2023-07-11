FROM node:16-slim

# Update apt packages
RUN runDeps="openssl ca-certificates patch gosu git tmux locales-all curl python3 build-essential" \
    && apt-get update \
    && apt-get install -y --no-install-recommends $runDeps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /opt/frontend/

RUN npm install -g mrs-developer \
    && mkdir -p /opt/frontend/src/addons \
    && rm -rf /opt/frontend/src/addons/*

RUN chown -R node /opt/frontend

USER node

COPY entrypoint.sh /opt/frontend/entrypoint.sh

WORKDIR /opt/frontend/

RUN cd /opt/frontend \
    && rm -rf /opt/frontend/src/addons/* \
    && make develop \
    && yarn \
    && RAZZLE_API_PATH=VOLTO_API_PATH RAZZLE_INTERNAL_API_PATH=VOLTO_INTERNAL_API_PATH yarn build \
    && rm -rf /home/node/.cache
USER root

EXPOSE 3000 3001 4000 4001

HEALTHCHECK --interval=1m --timeout=3s \
  CMD curl -f http://localhost:3000/ || exit 1

ENTRYPOINT ["/opt/frontend/entrypoint.sh"]
CMD ["yarn", "start:prod"]
