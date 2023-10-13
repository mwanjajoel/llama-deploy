# Llama Deploy
This repo contains source code for deploying Llama2 via a REST API endpoint using FastAPI and Docker. 

## How to install
The assumption is that you have `Pipenv` installed on your computer. 

Follow the steps below

1. Clone this repository
2. Run `pipenv install` command to install the dependencies
3. Copy the `.env-sample` and create a `.env` file then fill in the details.
4. Run the system using the docker command `docker-compose up -d`
5. Send a prompt to the API endpoint `/prompt` to get a response.