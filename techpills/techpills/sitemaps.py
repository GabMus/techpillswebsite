from django.contrib.sitemaps import Sitemap
from blog.models import Article

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Article.objects.all()
