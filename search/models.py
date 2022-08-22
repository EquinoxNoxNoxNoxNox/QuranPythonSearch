from django.db import models


# Create your models here.

class Verses(models.Model):
    verse_pk = models.CharField(max_length=8, null=False, blank=False, unique=True, verbose_name="آیه کلیدی")
    page = models.PositiveIntegerField(null=False, blank=False, verbose_name='صفحه')
    hizbQuarter = models.PositiveIntegerField(null=False, blank=False, verbose_name='ربع')
    juz = models.PositiveIntegerField(null=False, blank=False, verbose_name='جزء')
    surah = models.ForeignKey('Surah', on_delete=models.CASCADE, null=True, blank=True, related_name='surah',
                              verbose_name='سوره')
    verse = models.CharField(max_length=5000, null=False, blank=False, verbose_name='آیه')
    verseWithoutTashkeel = models.CharField(max_length=1000, null=False, blank=False, verbose_name='آیه بدون شکل گیری')
    numberInSurah = models.PositiveIntegerField(null=False, blank=False, verbose_name='شماره آیه در سوره')
    numberInQuran = models.PositiveIntegerField(null=False, blank=False, unique=True,
                                                verbose_name='شماره آیه در قرآن')
    audio = models.URLField(null=False, blank=False, unique=True, verbose_name='منبع تلاوت اولیه')
    audio1 = models.URLField(null=True, blank=True, unique=True, verbose_name='منبع تلاوت ثانویه 1')
    audio2 = models.URLField(null=True, blank=True, unique=True, verbose_name="منبع تلاوت ثانویه 2")
    sajda = models.BooleanField(verbose_name='آیا آیه دارای سجده است؟')

    class Meta:
        ordering = ['id']
        verbose_name = 'آیه'
        verbose_name_plural = 'آیات'

    def __str__(self):
        return self.verse[:50]


class Surah(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام سوره")
    nameWithoutTashkeel = models.CharField(max_length=30, verbose_name="نام سوره بدون تشکیل")

    class Meta:
        ordering = ['id']
        verbose_name = 'سوره'
        verbose_name_plural = 'السور'

    def __str__(self):
        return self.name
