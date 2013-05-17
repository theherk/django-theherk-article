from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _
from cmsplugin_article.models import Article


class CMSPluginArticle(CMSPluginBase):
    model = Article
    name = _("Article")
    render_template = "cmsplugin_article/article.html"
    module = _("TheHerk")

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CMSPluginArticle)
