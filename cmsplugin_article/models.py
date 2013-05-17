from cms.models.pluginmodel import CMSPlugin
from django.db import models

from django.template.defaultfilters import slugify


class Article(CMSPlugin):
    """
    Define the attributes of an article object.
    """
    article_title = models.CharField(max_length=48)
    article_slug = models.SlugField(editable=False)
    article_description = models.CharField(max_length=64, blank=True)
    article_body = models.TextField(help_text='Must be html. Use text plugin if this is a problem.')

    """
    Override the save method to auto-slug the title.
    """
    def save(self, *args, **kwargs):
        if not self.article_slug:
            # Set slug only if new to keep from breaking links.
            self.article_slug = slugify(self.article_title)

        super(Article, self).save(*args, **kwargs)
