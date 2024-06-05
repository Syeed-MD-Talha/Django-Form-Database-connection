from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    class Meta:
        db_table = 'Contact_Form'
        managed = True
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'