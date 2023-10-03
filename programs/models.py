from django.db import models
from abstract.models import AbstractModel,AbstractManager, Images
import uuid
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class ProgramManager(AbstractManager):
    pass

class Program(AbstractModel, Images):
    description = models.TextField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    objects = ProgramManager()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('inua:activity', args=[self.public_id])


    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'



class ActivityManager(AbstractManager):
    pass


class Activity(AbstractModel, Images):
    description = models.TextField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

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

class BoardManagers(AbstractManager):
    pass

class BoardMember(Images):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    objects = BoardManagers()

    class Meta:
        verbose_name = 'Boardmember'
        verbose_name_plural = 'Boardmembers'

    def __str__(self) -> str:
        return self.first_name

    @property
    def names(self):
        return f'{self.first_name} {self.last_name}'
    

class GalleryManager(AbstractManager):
    pass

class Gallery(Images):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4)
    event = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = GalleryManager()
    
    
    def save(self, *args, **kwargs):
        super(Images, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
           img.thumbnail((300,300))
        img.save(self.image.path,quality=70,optimize=True)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'





class GalleryImageManager(AbstractManager):
    pass

class GalleryImage(Images):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Galleryimage'
        verbose_name_plural = 'Galleryimages'

    


