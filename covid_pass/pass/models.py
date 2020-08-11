from django.db import models

# Create your models here.


class Pass(models.Model):
    """"
    create some attributes
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id_number = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_pass(self):
        return self.name

    def __repr__(self):
        return self.name
