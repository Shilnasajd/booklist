from django.db import models

# Create your models here.

books=[
    {"id":1,"name":"heaven","author":"scds","price":80},
    {"id":2,"name":"space","author":"ascsc","price":68},
    {"id":3,"name":"galaxy","author":"nhmhm","price":75},
    {"id":4,"name":"orbit","author":"wewqer","price":87},
]


class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=150)
    price=models.PositiveIntegerField()

    def str(self):
        return self.name