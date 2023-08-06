# create_project.py

import subprocess


def create_django_project(project_dir, default_project_name="myproject"):
    while True:
        project_name = (
            input(
                "Enter the name of the new Django project [{}]: ".format(
                    default_project_name
                )
            )
            or default_project_name
        )
        try:
            subprocess.run(
                ["django-admin", "startproject", project_name, project_dir], check=True
            )
        except subprocess.CalledProcessError:
            pass
        else:
            print("\nDjango project created.\n")
            break
