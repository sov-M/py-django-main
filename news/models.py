from django.db import models

class Articles(models.Model):
    title = models.CharField("Название статьи", max_length=70, blank=True)
    anons = models.CharField("Анонс", max_length=270, blank=True)
    full_text = models.TextField("Статья", blank=True)
    date = models.DateTimeField("Дата публикации", auto_now_add=True)  # Поле даты
    cover = models.ImageField(upload_to='images/post', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
