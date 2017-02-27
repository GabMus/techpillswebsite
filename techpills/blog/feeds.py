from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Article

class BlogFeed(Feed):
    title = "Tech Pills Blog"
    link = "/blog/"
    description = "Tech Pills Blog"
    
    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content.splitlines()[0]

    def item_link(self, item):
        return '/blog/article/'+str(item.id)
