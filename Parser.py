from bs4 import BeautifulSoup
import requests

def file(str):
    file = open('OmSTU_kaf.txt', 'w')

    words = str.split("\n")
    print(words)
    for i in words:
        if i != '':
            file.write(i+"\n")
    file.close()
def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'#передаем URL адрес
    page = requests.get(url) # отправляем запрос методом get на данный адрес и получаем ответ в переменную
    # print(page.status_code)
    allKafedra = []
    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup)
    allKafedra = soup.findAll('div', class_='main__content')#находим контейнер с нужным классом и тегом
    StringKafedr = ''
    for kafedra in allKafedra: #проходим циклом по содержимому контейнера
       if kafedra.find('br'):# если есть тег br
          StringKafedr = kafedra.text #записываем в переменную содержимое тега
    # запись в файл
    file(StringKafedr)

