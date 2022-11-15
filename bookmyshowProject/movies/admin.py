from django.contrib import admin

from .models import Movies, Moviedimension, Moviegenre, Movielanguages, Agecategory, Actor, \
    Movieactormap, Moviecertificationmap, Moviedimensionmap, Moviegenremap, Movielanguagemap, \
    Reviews

# Register your models here.
admin.site.register(Movies)
admin.site.register(Movielanguages)
admin.site.register(Moviegenre)
admin.site.register(Moviedimension)
admin.site.register(Agecategory)
admin.site.register(Actor)
admin.site.register(Movieactormap)
admin.site.register(Moviecertificationmap)
admin.site.register(Moviedimensionmap)
admin.site.register(Moviegenremap)
admin.site.register(Movielanguagemap)
admin.site.register(Reviews)
