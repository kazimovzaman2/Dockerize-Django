# inputs_user.py

import inquirer


def ask_use_docker_compose():
    questions = [
        inquirer.List(
            "choice",
            message="Do you want to use Docker Compose for this Django project?",
            choices=["yes", "no"],
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["choice"] == "yes"


def ask_create_django_project():
    questions = [
        inquirer.List(
            "choice",
            message="No Django project found. Do you want to create a new Django Project?",
            choices=["yes", "no"],
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["choice"] == "yes"


def ask_env():
    questions = [
        inquirer.List(
            "choice",
            message="What environments do you want to configure?",
            choices=["Development", "Production"],
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["choice"]


def ask_db_detail():
    questions = [
        inquirer.List(
            "choice",
            message="What database do you want to use?",
            choices=["PostgreSQL",],
        )
    ]
    answers = inquirer.prompt(questions)
    return answers["choice"]


def db_postgres():
    questions = [
        inquirer.Text(
            "db_name",
            message="Enter database name",
        ),
        inquirer.Text(
            "db_user",
            message="Enter database user",
        ),
        inquirer.Text(
            "db_password",
            message="Enter database password",
        ),
    ]
    answers = {}
    for question in questions:
        while True:
            answer = inquirer.prompt([question])
            if answer[
                question.name
            ].strip():  # Check if the answer is not just whitespace
                answers.update(answer)
                break
            else:
                print("Please provide a valid answer.")

    return answers
