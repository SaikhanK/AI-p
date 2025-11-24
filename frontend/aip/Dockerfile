# Use a Node.js image as the base for development
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker cache
COPY package*.json ./

# Install all dependencies (dev and prod)
RUN npm install

# Copy the rest of the application source code
# This will be mostly overlaid by the volume mount, but it's good practice
COPY . .

# Expose the default Angular development server port
EXPOSE 4200

# Command to start the Angular development server
# --host 0.0.0.0 is crucial for the app to be accessible from outside the container
# --disable-host-check is often needed when running in a Docker container
CMD ["npm", "start", "--", "--host", "0.0.0.0", "--disable-host-check"]