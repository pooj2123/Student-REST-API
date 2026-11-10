QUESTION 3 - DOCKERIZE A PYTHON APPLICATION

REQUIREMENTS
- Docker Desktop installed and running
- VS Code (optional)
- Terminal / PowerShell

STEP 1: Open the Q3_Docker_Python_App folder in VS Code.
STEP 2: Open a terminal in this folder.
STEP 3: Check Docker:
    docker --version
    docker info
Docker Desktop must be running. If docker info shows a daemon/engine error,
open Docker Desktop and wait until it says Docker is running.

STEP 4: Build the Docker image:
    docker build -t simple-python-app .

STEP 5: Check that the image exists:
    docker images

STEP 6: Run a container and map host port 8080 to container port 5000:
    docker run -d --name my-python-container -p 8080:5000 simple-python-app

STEP 7: Check the running container:
    docker ps

STEP 8: Test the application using curl:
    curl.exe http://localhost:8080/
Expected response:
    Hello! My Python application is running inside Docker.

STEP 9: Test the health endpoint:
    curl.exe http://localhost:8080/health
Expected response:
    {"status":"healthy"}

STEP 10: Stop and remove the container when finished:
    docker stop my-python-container
    docker rm my-python-container

IMPORTANT
- 8080 is the port on your Windows host.
- 5000 is the port used by Flask inside the container.
- If the container name is already in use, remove the old container first:
    docker rm -f my-python-container
- If Docker Desktop is not installed, install it from:
  https://www.docker.com/products/docker-desktop/
