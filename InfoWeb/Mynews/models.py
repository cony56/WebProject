from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model): 
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for this alias')
    writer = models.CharField('WRITER', max_length=10, blank=True, help_text='name of the press')
    article = models.TextField('ARTICLE', max_length=500)
    href = models.TextField('HREF')
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        db_table = 'news_list'
        ordering = ('-modify_date',)  
    
    def get_absolute_url(self):
        return reverse('Mynews:post_detail', args=(self.slug,)) # -> 1st post -> /blog/post/1st-post

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
    