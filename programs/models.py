from django.db import models
from abstract.models import AbstractModel,AbstractManager
import uuid
from django.contrib.auth.models import User


class ProgramManager(AbstractManager):
    pass

class Program(AbstractModel):
    description = models.TextField()
    image = models.ImageField(null=True,upload_to='uploads/programs-pics/')
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    objects = ProgramManager()

    def __str__(self) -> str:
        return self.title




class ActivityManager(AbstractManager):
    pass


class Activity(AbstractModel):
    description = models.TextField()
    image = models.ImageField(null=True,upload_to='uploads/activity-pics/')
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

# Create your models here.
class AboutUsManager(AbstractManager):
    pass

class AboutUs(models.Model):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False)
    description = models.TextField()
    vision = models.CharField(max_length=255)
    mission = models.CharField(max_length=400)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    objects = AboutUsManager()

class BoardMember(models.Model):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/board-members-pics',null=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.first_name

    @property
    def names(self):
        return f'{self.first_name} {self.last_name}'
    

class Gallery(models.Model):
    image = models.FileField(upload_to='uploads/gallery')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)





