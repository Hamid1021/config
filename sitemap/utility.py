from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse

# from items.models import Category, Item


# class ItemSitemap(Sitemap):
#     changefreq = 'always'
#     priority = 1

#     def items(self):
#         return Item.objects.filter(status="p")

#     def lastmod(self, obj):
#         return obj.updated


# class CategorySitemap(Sitemap):
#     changefreq = 'always'
#     priority = 1

#     def items(self):
#         return Category.objects.filter(status=True)


# class StaticViewSitemap(sitemaps.Sitemap):
#     changefreq = 'always'
#     priority = 1

#     def items(self):
#         return ['Home:Home', 'account:login', "Home:gallery", "Home:cantact", ]

#     def location(self, item):
#         return reverse(item)


# ##############################################################
SiteMaps = {}


# def add_to_sitemaps(key, value, flag=0):
#     # add
#     if flag == 0:
#         SiteMaps[key] = value
#     # update
#     else:
#         SiteMaps.update({key: value})



# add_to_sitemaps('static', StaticViewSitemap)
# add_to_sitemaps('Category', CategorySitemap)
# add_to_sitemaps('Item', ItemSitemap)

