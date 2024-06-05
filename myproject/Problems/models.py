from django.db import models

# Create your models here.
class online_judge(models.Model):
    judge_name=models.CharField(max_length=20)
    total_problem=models.IntegerField()
    handle_name=models.CharField(max_length=10)

class GeeksModel(models.Model):
    title=models.CharField(max_length=10)
    description=models.TextField()
    topic=models.CharField(max_length=10)

    class Meta:
        db_table='talha'
