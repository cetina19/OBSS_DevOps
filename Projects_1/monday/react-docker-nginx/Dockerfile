FROM node:alpine AS build
ENV NODE_ENV build
WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 4200
FROM nginx
COPY --from=builder /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]
CMD ["--host", "0.0.0.0"]