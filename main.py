# main.py

import os
from dockerize.check_project import check_django_project
from dockerize.create_project import create_django_project
from dockerize.generate_compose import create_docker_compose_file
from dockerize.inputs_user import *
from dockerize.setup_env import setup_development_environment


def main():
    current_dir = os.getcwd()

    if check_django_project(current_dir):
        print("\n")
        if ask_use_docker_compose():
            create_docker_compose_file()
        setup_development_environment()
    else:
        if ask_create_django_project():
            create_django_project(current_dir)
            if ask_use_docker_compose():
                create_docker_compose_file()
            setup_development_environment()
        else:
            print("Exiting.")


if __name__ == "__main__":
    main()
