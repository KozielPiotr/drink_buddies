# Drink buddies

## Setup
to run:
1. Env variables:
    1. Create **.env** file at the top level of project.

        Example developement data can be found in **.example_dev_env** file.
    2. From the top level of the project:
        ```bash
        set -o allexport; . ./.env; set +o allexport
        ```
       Note, that the command may be slightly different with different shells.

2. Set up database:
    ```bash
    sudo docker run -p 5432:5432 -e POSTGRES_USER=drinking_buddies -e POSTGRES_PASSWORD=drinking_buddies -e POSTGRES_DB=drinking_buddies postgres:12.4-alpine
    ```
