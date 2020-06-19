from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Article(models.Model):
    title = models.CharField(_('title'), max_length=256)
    subtitle = models.TextField(_('subtitle'), blank=True)
    contents = models.TextField(_('contents'))
    aid = models.CharField(_('article number'), max_length=12, unique=True)
    url = models.URLField(_('article url'), blank=True)
    pub_date = models.DateField(_('publishing date'))

    pub_company = models.ForeignKey('articles.Company',
                                    on_delete=models.CASCADE,
                                    verbose_name=_('publishing company'),
                                    related_name='articles')

    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(_('company name'), max_length=128)
    oid = models.CharField(_('company number'), max_length=4)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name
