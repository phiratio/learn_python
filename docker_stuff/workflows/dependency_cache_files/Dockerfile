FROM node:8 as npm

COPY package.json /app/package.json

WORKDIR /app

RUN npm config set registry http://127.0.0.1:8081/repository/npmjs.com-proxy/ && \
    npm install

FROM gcr.io/distroless/nodejs
COPY --from=npm /app/node_modules /app/node_modules
COPY index.js /app/index.js

EXPOSE 3000

CMD ["/app/index.js"]
