![example workflow](https://github.com/KozielPiotr/drink_buddies/actions/workflows/linters.yml/badge.svg)
![example workflow](https://github.com/KozielPiotr/drink_buddies/actions/workflows/tests.yml/badge.svg)
# Drink buddies

### Table of contents:
1. [Setup](#setup)
    1. [Run locally](#run_locally)
        1. [Environment variables](#env_variables)
        2. [Database setup](#database_setup)
        3. [Database migration](#database_migration)
        4. [New superuser creation](#create_superuser)
        5. [Database population](#populate_database)
2. [Graphql schema](https://kozielpiotr.github.io/documentations/drinking_buddies_graphql_schema.html)


## Setup <a name="setup"></a>
### To run locally: <a name="run_locally"></a>
1. Environment variables <a name="env_variables"></a>
    1. Create **.env** file at the top level of the project.

        Example developement data can be found in **.example_dev_env** file.
    2. From the top level of the project:
        ```shell
        $ set -o allexport; . ./.env; set +o allexport
        ```
       Note, that the command may be slightly different with different shells.

2. Database setup: <a name="database_setup"></a>
    ```shell
    $ sudo docker run -p 5432:5432 -e POSTGRES_USER=drinking_buddies -e POSTGRES_PASSWORD=drinking_buddies -e POSTGRES_DB=drinking_buddies postgres:12.4-alpine
    ```
   Example above has user, password and name same as in sample env file. Be sure to change it if you are using different ones.

3. Database migration: <a name="database_migration"></a>

    ```shell
    $ python manage.py migrate
    ```

4. New superuser creation <a name="create_superuser"></a>
    ```shell
    $ python manage.py createsuperuser
    ```

5. Database population <a name="populate_database"></a>
    ```shell
    $ python manage.py loaddata species
    ```
