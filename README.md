# Run Django Project
1. Clone the project in your working directory
2. Create a virtual environment

> python3 venv -m virtual

3. Install all the packages in the requirements.txt file

> pip install -r requirements.txt

4. Ensure you are in the myproject folder

5. Start the project

> python manage.py runserver

6. Run celery worker

> celery -A myproject worker -l INFO

7. Run celery beat

> celery -A myproject beat -l INFO

# Run Docker Compose
1. Ensure you have docker and docker compose installed 
2. Initialize docker compose

> docker compose up

## NB:
1. Check all docker images

> docker images

2. Check all running docker containers

> docker ps

3. Check all docker containers

> docker ps -a
>
## Note: If you're not running it via docker ensure that you have installed Redis in your server. Also remeber to change the broker url in the settings.py file in the main project directory
