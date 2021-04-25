from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from posts.models import Post


# Create your models here.

class Comentario(models.Model):
    nome_comentario = models. CharField(max_length=150)
    email_comentario = models.EmailField()
    comentario = RichTextField(blank=True, null=True)
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comentário'

    def __str__(self):
        return "{}".format(self.nome_comentario)