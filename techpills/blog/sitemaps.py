from django.contrib.sitemaps import Sitemap
from blog.models import Article

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.7

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.date_time

    def location(self, obj):
        return '/blog/article/' + str(obj.id)
