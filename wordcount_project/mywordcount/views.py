from django.shortcuts import render
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    html=urlopen("http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37079&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right")
    bsObject=BeautifulSoup(html, "html.parser")

    table = bsObject.find("table")
    titles=table.find_all(class_="title")
    notices={}
    for title in titles:
        x=title.get_text()
        x=x.replace("\t", '')
        x=x.replace("\n", '')
        x=x.strip()
        link=title.a.get('href')
        url='http://www.hufs.ac.kr/user/' +link
        notices[x]=url
    return render(request, 'about.html', {'notices':notices.items()})

def result(request):
    input_text=request.GET['fulltext']
    word_list=input_text.split()

    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
            #dictionary 형태= {}이렇게 되어 있는데, key, value값이 들어 있는데 word_dictionary 를 선언하고 
            #word_dictionary[key]=value되도록 하라는 것임
            #중복되는 값, ex가 처음이면 1개, 그다음께 ex이면 값을 +1로 단어갯수를 증가시켜줌
    return render(request, 'result.html', {'fulltext':input_text, 'total':len(word_list), 'dictionary': word_dictionary.items()})
    #items로 가지고 오면 key값, value값이 따로 가져오게 됨...