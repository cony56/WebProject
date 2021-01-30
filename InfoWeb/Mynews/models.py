from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model): 
    title = models.TextField('TITLE', max_length=500)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for this alias')
    writer = models.TextField('WRITER', max_length=10, blank=True, help_text='name of the press')
    article = models.TextField('ARTICLE', max_length=500)
    href = models.TextField('HREF')
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        db_table = 'news_list'
    
    def get_absolute_url(self):
        return reverse('Mynews:post_detail', args=(self.pk,)) # -> 1st post -> /blog/post/1st-post

    def get_previous_post(self):
        if self.pk >2:
            return reverse('Mynews:post_detail', args=(int(self.pk)-1,))
    
    def get_next_post(self):
        if self.pk <100:
            return reverse('Mynews:post_detail', args=(int(self.pk)+1,))
    # def get_previous_post(self):
    #     return self.get_previous_by_modify_date()

    # def get_next_post(self):
    #     return self.get_next_by_modify_date()
    