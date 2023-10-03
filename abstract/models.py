from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import uuid
import os
from PIL import Image


class AbstractManager(models.Manager):
    def get_object_by_public_id(self,public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance

        except (ObjectDoesNotExist,ValueError, TypeError):
            return Http404



class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)

    objects = AbstractManager()

    class Meta:
        abstract = True

def image_upload(instance, filename):
    model_name = instance._meta.verbose_name.replace(' ','-')
    return '/'.join(['uploads',model_name,filename])

class Images(models.Model):
    image = models.FileField(null=True,upload_to=image_upload)

    def save(self, *args, **kwargs):
        super(Images, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 900:
           img.thumbnail((600,900))
        img.save(self.image.path,quality=70,optimize=True)

    class Meta:
        abstract = True