from io import BytesIO

from django.core.files import File
from django.db import models
from PIL import Image, ImageOps


class Painting(models.Model):
    caption = models.TextField()
    in_stock = models.BooleanField(default=False)
    price = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.title
            

def get_last_painting():
    return Painting.objects.last()

        
class MainPainting(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, default=get_last_painting)

    def __str__(self):
        return self.painting.title

    
    
class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='show')

    def save(self):
        im = Image.open(self.image)
        im = im.convert('RGB')
        im = ImageOps.exif_transpose(im)
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality=90)
        new_image = File(im_io, name=self.image.name)
        self.image = new_image
        super().save()
        
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        return super().delete(using, keep_parents)
