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