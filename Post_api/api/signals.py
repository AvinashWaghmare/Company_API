from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post

@receiver(post_save, sender=Post)
def send_post_creation_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'Hello "{instance.author}", \n\nYour new post "{instance.title}" has been created.'
        from_email = 'aw422360@gmail.com'
        recipient_list = [instance.author.email]  # Replace with actual recipient email addresses
        send_mail(subject, message, from_email, recipient_list)
