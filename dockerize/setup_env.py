# setup_env.py

from dockerize.inputs_user import ask_env


def create_file():
    file = f"""FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip uninstall django
RUN pip install -r requirements.txt

COPY . .
"""
    with open("Dockerfile", "w") as f:
        f.write(file)


def setup_development_environment():
    env = ask_env()
    if env == "Development":
        create_file()
    else:
        create_file()
