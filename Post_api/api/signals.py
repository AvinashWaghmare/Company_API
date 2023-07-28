from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post

@receiver(post_save, sender=Post)
def send_post_creation_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'A new post "{instance.title}" has been created.'
        from_email = 'your_email@example.com'
        recipient_list = ['recipient@example.com']  # Replace with actual recipient email address(es)
        send_mail(subject, message, from_email, recipient_list)