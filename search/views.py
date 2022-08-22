from .models import Verses
from .serializers import VersesSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.shortcuts import get_object_or_404, render


@api_view(['GET'])
def get_all(request) -> None:
    """
	دریافت تمام آیات از دیتابیس
    """
    verses = Verses.objects.all()
    data = VersesSerializers(verses, many=True).data
    return render(request, 'search/main.html', {'length': len(data), 'data': data})
    #return Response({'length': len(data), 'data': data})


@api_view(['GET'])
def search(request, words) -> str:
    """
        Search in verses using insensitive contains.
        دریافت تمام آیات دارای کلمات پارامتر
    """
    verses = Verses.objects.filter(
        Q(verse__icontains=words) | Q(verseWithoutTashkeel__icontains=words)
    )
    data = VersesSerializers(verses, many=True).data
    return Response({'length': len(data), 'data': data})


@api_view(['GET'])
def get_surah(request, surah_id) -> int:
    """
        دریافت سوره با توجه با آیدی
        verse_pk: S***V*** | surah_pk -> first part of verse_pk (S***).
    """
    surah_pk = f"S{str(surah_id).zfill(3)}"
    verse_id = Verses.objects.filter(verse_pk__icontains=surah_pk)
    data = VersesSerializers(verse_id, many=True).data
    return Response({'length': len(data), 'data': data})


@api_view(['GET'])
def get_verse_in_surah(request, surah_id, verse_id) -> int:
    """
        تبدیل 2 اینتجر در پارامتر به فرمت verse_pk,
        Returns the Verse.
    """
    verse_pk = f'S{str(surah_id).zfill(3)}V{str(verse_id).zfill(3)}'
    verse = get_object_or_404(Verses, verse_pk=verse_pk)
    data = VersesSerializers(verse).data
    return Response({'data': data})


@api_view(['GET'])
def get_verse_in_quran(request, verse_id) -> int:
    """
        دریافت سوره با توجه به شماره ی سوره در قرآن
        Returns the Verse.
    """
    verse = get_object_or_404(Verses, numberInQuran=verse_id)
    data = VersesSerializers(verse).data
    return Response({'data': data})


def api_docs(request):
    return render(request, 'search/main.html')
