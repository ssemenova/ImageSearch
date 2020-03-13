from django.db import models

class People(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    AddressID = models.IntegerField()
    Email = models.CharField(max_length=200)
    Phone = models.IntegerField()
    TemplatePhoto = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)