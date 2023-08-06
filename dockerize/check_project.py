# check_project.py

import os


def check_django_project(project_dir):
    manage_py_path = os.path.join(project_dir, "manage.py")
    return os.path.exists(manage_py_path)
