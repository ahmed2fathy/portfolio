from django.db import models
from django.urls import reverse
import blog_arab

from blog_arab.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Tag(models.Model):

    name = models.CharField(
        max_length=180, help_text='Enter category name ', verbose_name=_('name'))

    

    des = models.TextField(max_length=340, null=True,
                           blank=True, verbose_name=_('Description'))
    image = image = models.ImageField(
        upload_to='media/blog/frontbage/category', null=True, blank=True, verbose_name=_('image'),)

    slug = models.SlugField(max_length=200, editable=True, allow_unicode=True, blank=True,  help_text=_(
        'You should write some words indicating the content of the article in English'), verbose_name=_(' url'))

    def __str__(self) -> str:
        return self.name

    def get_article(self):
        return blog_arab.models.Blog.objects.filter(tag_ar=self)

     # دالة تحويل اسم المقال الي رابط وازالة المسافات الفارغة ووضع - داش

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = arabic_slugify(self.name)
        # Call the real save() method
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # دالة جلب رابط المقال

    def get_absolute_url(self):

        return reverse('tag_arab:tag_detail', kwargs={'slug': self.slug})


def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str
