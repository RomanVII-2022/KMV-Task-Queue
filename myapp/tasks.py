from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def sendEmail(self, email):
    subject = "Login to KMV"
    message = "You have successfully logged into the KMV app. If it not you kindly click on the following link: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html "
    fromEmail = settings.EMAIL_HOST_USER
    recipientList = [email, ]
    send_mail(subject=subject, message=message, from_email=fromEmail, recipient_list=recipientList, fail_silently=True)
    return "Email sent successfully"
    