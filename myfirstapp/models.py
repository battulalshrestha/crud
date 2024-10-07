from django.db import models

# Create your models here
'''class Person(models.Model):
    # i want to detail infromation for the person 

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    def __str__(self):
      return f"{self.first_name} {self.last_name}"   '''




'''class Manager(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=70)
    salery_type = models.FloatField()
    work_type = models.TextField()
    job_post = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return (self.name)

class Employee(models.Model):
    name = models.ForeignKey(Manager, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    position = models.CharField(max_length=40)
    experience = models.IntegerField(max_length =20)'''


#  choice field 
'''class Person(models.Model):
  Book_type = {
    "P":'poem',
    "S":'Story',
    "G":"Gajal",
    "O":'other_book',
  }
  name = models.CharField(max_length=50)
  book_type = models.CharField(max_length=1,choices=Book_type)'''

  # many to many field
'''class College(models.Model):
  College_name = models.CharField(max_length=50)
  collge_location = models.CharField(max_length=70)
  college_distance = models.FloatField(max_length=10)
  college_review = models.CharField(max_length=40)

class Classroom (models.Model):
  room_name = models.ManyToManyField(College,max_length=20)
  room_location = models.CharField(max_length=40)
  room_capacity = models.IntegerField(max_length=10)
  room_review = models.CharField(max_length=40)'''

#abstract class
'''class Common(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    class Meta:
        abstract = True
class Teacher(Common):
    fees = models.IntegerField()
class Student(Common):
    salery = models.IntegerField()'''