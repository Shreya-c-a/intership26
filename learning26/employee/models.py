from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    age = models.IntegerField()
    post = models.CharField(max_length=100)
    joining_date = models.DateField()

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name
    
class course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name

class library(models.Model):
    bookName = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    price = models.IntegerField()
    publishedDate = models.DateField(null=True)

    class Meta:
        db_table = "library"

    def __str__(self):
        return self.bookName
class event(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.DateField()
    location = models.CharField(max_length=100)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.eventName