
from django.db import models

from userprofile.models import User


class Movies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    movies_name = models.CharField(db_column='Movies_name', max_length=100)
    about = models.CharField(
        db_column='About', max_length=150, blank=True, null=True)
    release_date = models.DateTimeField(
        db_column='Release_date', blank=True, null=True)
    duration = models.BigIntegerField(db_column='Duration')
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.movies_name

    class Meta:
        managed = True
        db_table = 'Movies'
        verbose_name_plural = "Movies"


class Movielanguages(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    language = models.CharField(db_column='Language', max_length=20)
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.language

    class Meta:
        managed = False
        db_table = 'MovieLanguages'
        verbose_name_plural = "MovieLanguages"


class Movielanguagemap(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    movielanguageid = models.ForeignKey(
        'Movielanguages', models.DO_NOTHING, db_column='MovieLanguageId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovieLanguageMap'


class Moviegenre(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    genre_name = models.CharField(db_column='Genre_name', max_length=20)

    def __str__(self):
        return self.genre_name

    class Meta:
        managed = True
        db_table = 'MovieGenre'
        verbose_name_plural = "MovieGenre"


class Moviegenremap(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    moviegenreid = models.ForeignKey(
        Moviegenre, models.DO_NOTHING, db_column='MovieGenreId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovieGenreMap'
        verbose_name_plural = 'Moviegenremap'


class Moviedimension(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    dimension = models.CharField(db_column='Dimension', max_length=20)

    def __str__(self):
        return self.dimension

    class Meta:
        managed = True
        db_table = 'MovieDimension'
        verbose_name_plural = "MovieDimension"


class Moviedimensionmap(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    moviedimensionid = models.ForeignKey(
        Moviedimension, models.DO_NOTHING, db_column='MovieDimensionId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovieDimensionMap'
        verbose_name_plural = 'Moviedimensionmap'


class Agecategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    certification = models.CharField(db_column='Certification', max_length=20)

    def __str__(self):
        return self.certification

    class Meta:
        managed = True
        db_table = 'AgeCategory'
        verbose_name_plural = "Certification"


class Moviecertificationmap(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    certificationid = models.ForeignKey(
        Agecategory, models.DO_NOTHING, db_column='CertificationId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovieCertificationMap'
        verbose_name_plural = 'Moviecertificationmap'


class Actor(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    # Field name made lowercase.
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    firstname = models.CharField(
        db_column='Firstname', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(
        db_column='Lastname', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actor'


class Movieactormap(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    actorid = models.ForeignKey(
        Actor, models.DO_NOTHING, db_column='ActorId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovieActorMap'
        verbose_name_plural = 'Movieactormap'


class Reviews(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        Movies, models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
    # Field name made lowercase.
    review_comment = models.CharField(
        db_column='Review_comment', max_length=255)
    # Field name made lowercase.
    ratings_date = models.DateField(
        db_column='Ratings_date', blank=True, null=True)
    # Field name made lowercase.
    isuser = models.BooleanField(
        db_column='isUser', blank=True, null=True, default=False)
    # Field name made lowercase.
    userid = models.ForeignKey(
        User, models.DO_NOTHING, db_column='UserId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reviews'
        verbose_name_plural = 'Reviews'
