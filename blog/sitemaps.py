from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'  # indicate the change frequency of your post pages
    priority = 0.9         # their relevance in your website (the maximum value is 1).

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
