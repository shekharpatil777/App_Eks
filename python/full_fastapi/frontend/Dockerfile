FROM node:18-alpine as build

WORKDIR /app

# Copy package.json first to cache dependencies
COPY package.json ./
RUN npm install --silent

# Now, copy all of the project files, including 'public'
COPY . .

# Run the build command
RUN npm run build

# Stage 2: Serve the build output with Nginx
FROM nginx:stable-alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
