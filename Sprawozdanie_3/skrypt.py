import requests
from bs4 import BeautifulSoup

def source(a):
    result = requests.get(a)
    list = []
    list.append(result.content)
    return print(list)

def status(a):
    result = requests.get(a)
    return print(result.status_code)

def linki(a):
        result = requests.get(a)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        urls = []
        for a_tag in soup.find_all("a"):
            urls.append(a_tag.get('href'))
        return print(urls)

def paragarfy(a):
    result = requests.get(a)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    para = []
    para.append(soup.find_all('p'))
    return print(para)

def divy(a):
    result = requests.get(a)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    divy = []
    divy.append(soup.find_all('div'))
    return print(divy)

def tytul(a):
    result = requests.get(a)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    tytul = []
    tytul.append(soup.title)
    return print(tytul)

def tagi(a):
    result = requests.get(a)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    tagi = []
    tagi.append(soup.find_all('b'))
    return print(tagi)

def headery(a):
    result = requests.get(a)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    headery = []
    headery.append(soup.find_all('h1'))
    return print(headery)

#Funkcje
#   1. Zwraca kod źródłowy strony

#source("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   2. Funkcja na sprawdzanie statusu strony. Wpisujesz wybrany link pomiędzy nawiasy np. google.

#status("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   3. Funkcja zwróci wszystkie linki 'href' ze strony z znaczników <a>.

#linki("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   4. Funkcja ta zwróci paragrafy na stronie

#paragarfy("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   5. Zwraca zawartość wszystkich div'ów na stronie

#divy("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   6. Zwraca tytul strony.

#tytul("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   7. Zwraca tagi bold.

#tagi("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

#   8. Zwraca wszystkie headery 1.

#headery("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
