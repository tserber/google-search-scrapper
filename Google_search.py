from selenium import webdriver
from bs4 import BeautifulSoup
from docx import Document
import requests
import urllib.request


class Google_search():
    def __init__(self, search, re_finds):
        self.search = search
        self.re_finds = re_finds

    def get_html(self):
        search_input = self.search.replace(" ","+")
        respons = requests.get('https://www.google.com/search?q='+search_input)
        # print(respons.text)
        soup = BeautifulSoup(respons.text, 'lxml')
        # print(soup.prettify())
        # url = f'https://www.google.com/search?q={self.search}'
        # r = requests.get(url)
        # return r.text
        return soup

    def get_headers(self):
        return self.get_html().find_all('h3')

    def get_a_from_names(self):
        list_of_names=[]
        for name in self.get_headers():
            url= 'https://www.google.com'+ name.parent.attrs['href']
            response = urllib.request.urlopen(url)
            res = response.geturl()
            list_of_names.append(res)
        return list_of_names



    def get_href_google_results(self):
        names= self.get_headers()
        list_of_names=[]
        for name in names:
            list_of_names.append(name.parent)
        return list_of_names

    def get_text_google_results(self):
        names = self.get_headers()
        res=[]
        for name in names:
            res.append(name.text)
        return res

def main():
    i=Google_search('krip r','Киев')
    print(i.get_a_from_names())


    # for i in i.get_href_google_results():
        # print(i)

# list_of_names=[]
# for name in names:
#     list_of_names.append(name.parent)
# return list_of_names


if __name__ == '__main__':
    main()
