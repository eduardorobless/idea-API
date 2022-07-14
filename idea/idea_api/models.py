from django.db import models
from django.conf import settings
# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        to_field='username',
        db_column='usuario_id'
    )
    class Meta:
        models.UniqueConstraint(fields=['name'], name='unique_idea')

    def __str__(self):
        return self.name