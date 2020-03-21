from django.db import models

class Person(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Age = models.IntegerField(null=True)
    AddressID = models.ForeignKey(
        'Address', 
        models.SET_NULL,
        null=True,
        blank=True,
    )
    Email = models.CharField(
        max_length=200, 
        null=True,
        blank=True,
    )
    Phone = models.IntegerField(
        null=True,
        blank=True,
    )
    TemplateEncoding = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    IsInvisible = models.BooleanField(
        default=False,
    ) # TODO: set this to True if a templatephoto is deleted


class Address(models.Model):
    ID = models.IntegerField(primary_key=True)
    Address1 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    Address2 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    CityID = models.ForeignKey(
        'City',
        models.PROTECT,
        blank=True,
        null=True,
    )

class City(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField()

class Message(models.Model):
    ID = models.IntegerField(primary_key=True)
    From = models.ForeignKey(
        'Person',
        models.SET_DEFAULT,
        default=0,
        blank=True,
        related_name='message_from'
    )
    To = models.ForeignKey(
        'Person',
        models.SET_DEFAULT,
        default=0,
        blank=True,
        related_name='message_to'
    )
    Content = models.CharField(max_length=100000)

class Photo(models.Model):
    ID = models.IntegerField(primary_key=True)
    EventID = models.ForeignKey(
        'Event',
        models.CASCADE,
        )
    Filename = models.CharField(max_length=200)

class Event(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)

class EventAttended(models.Model):
    PersonID = models.ForeignKey(
        'Person',
        models.CASCADE,
    )
    EventID = models.ForeignKey(
        'Event',
        models.CASCADE,
    )

    class Meta:
        unique_together = (("PersonID", "EventID"),)

class PhotoOf(models.Model):
    PersonID = models.ForeignKey(
        'Person',
        models.CASCADE,
    )
    PhotoID = models.ForeignKey(
        'Photo',
        models.CASCADE,
    )

    class Meta:
        unique_together = (("PersonID", "PhotoID"),)