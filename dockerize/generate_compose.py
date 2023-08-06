# generate_compose.py


from dockerize.inputs_user import ask_db_detail, db_postgres


def generate_docker_compose_postgres():
    database = db_postgres()
    db_name = database["db_name"]
    db_user = database["db_user"]
    db_password = database["db_password"]
    compose = f"""version: "3.8"
services:
    django:
        build: .
        container_name: django
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"
        depends_on:
            - postgres
    postgres:
        image: postgres:latest
        container_name: postgres
        environment:
            - POSTGRES_DB={db_name}
            - POSTGRES_USER={db_user}
            - POSTGRES_PASSWORD={db_password}
        volumes:
            - postgres_data:/var/lib/postgresql/data/
volumes:
    postgres_data:
        """
    return compose


def create_docker_compose_file():
    db_detail = ask_db_detail()
    if db_detail == "PostgreSQL":
        compose = generate_docker_compose_postgres()

    with open("docker-compose.yml", "w") as f:
        f.write(compose)

    print("Docker Compose file generated.")
