from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
from categorias.models import Categoria


class Post(models.Model):
    titulo_post = models.CharField(max_length=255)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = RichTextField(blank=True, null=True)
    excerto_post = RichTextField(blank=True, null=True)
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True)
    publicado_post = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return "{}".format(self.titulo_post)