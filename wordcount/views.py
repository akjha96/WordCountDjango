from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hii !!!')
    return render(request, 'home.html', {'A': ':-)'})


def wordcount(fulltext):
    word_list = fulltext.split()
    word_dict = dict()
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return sorted(word_dict.items(), key=lambda x: x[1], reverse=True)


def count(request):
    fulltext = request.GET['fulltext']
    word_dict = wordcount(fulltext)
    return render(request, 'count.html', {'fulltext': fulltext, 'word_count': word_dict})


def aboutme(request):
    return render(request, 'aboutme.html')
