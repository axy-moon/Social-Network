from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.utils import timezone
# Create your models here.

class NewUser(AbstractUser):
    rollno = models.CharField(max_length=7,null=False,unique=True,verbose_name='Roll Number')
    USERNAME_FIELD = 'rollno'

class Post(models.Model):
    author = models.ForeignKey(NewUser,on_delete=CASCADE)
    title = models.CharField(max_length=30,default='Question')
    post_time = models.DateTimeField(default=timezone.now)
    content = models.TextField(null=False)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title

class tokens(models.Model):
    roll_no = models.CharField(max_length=7,null=False,unique=True,verbose_name='Roll No')
    first_name = models.CharField(max_length=50,verbose_name='First Name')
    last_name = models.CharField(max_length=50,verbose_name='Last Name')

    def __str__(self):
        return self.roll_no

class profile(models.Model):
    username = models.ForeignKey(NewUser,on_delete=CASCADE)
    workplace = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=13,null=True)
    address_line_1 = models.CharField(max_length=50,null=True)
    address_line_2 = models.CharField(max_length=50,null=True)
    pin = models.IntegerField()

