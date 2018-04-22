from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subjectType(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class subject(models.Model):
    title = models.CharField(max_length=30,verbose_name="标题")
    content = models.TextField(verbose_name="介绍",null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    flag = models.CharField(max_length=30,verbose_name="FLAG",default="yctf{F1ag_H3r3!}")
    subject_addr = models.CharField(max_length=50,default="https://yoki.cloud/",null=True,blank=True)
    subject_type = models.ForeignKey(subjectType,on_delete=models.DO_NOTHING)
    answer_number = models.IntegerField(verbose_name="解答数",default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_answer_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class subjectPackage(models.Model):
    package_name = models.CharField(max_length=30)
    package_content = models.TextField(verbose_name="包介绍")
    package_type = models.ForeignKey(subjectType,on_delete=models.DO_NOTHING)
    package_include = models.ManyToManyField(subject)

    def __str__(self):
        return self.package_name