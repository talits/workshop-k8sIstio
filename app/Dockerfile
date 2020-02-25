FROM node:lts-alpine3.9

LABEL APP V2

COPY . /app

WORKDIR /app

RUN npm install

ENTRYPOINT [ "npm", "start" ]