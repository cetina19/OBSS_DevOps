FROM node:18-alpine AS build
ENV NODE_ENV build
WORKDIR /app
COPY ./package.json /app
COPY . .
RUN npm install
RUN npm run build
RUN yarn install --production
ENTRYPOINT [ "npm", "start", "--" ]
CMD ["node", "src/index.js"]
EXPOSE 3000