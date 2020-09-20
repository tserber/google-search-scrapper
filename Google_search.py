from selenium import webdriver
from bs4 import BeautifulSoup
from docx import Document
import requests
from urllib.request import Request, urlopen


class Google_search():
    def __init__(self, search, sought):
        self.search = search
        self.sought = sought

    def get_html_soup(self, url = False):
        # print(respons.text)
        if url:
            respons = requests.get(url)
        else:
            search_input = self.search.replace(" ","+")
            respons = requests.get('https://www.google.com/search?q='+search_input)
        soup = BeautifulSoup(respons.text, 'lxml')
        # print(soup.prettify())
        # url = f'https://www.google.com/search?q={self.search}'
        # r = requests.get(url)
        # return r.text
        return soup
    def get_headers(self):
        return self.get_html_soup().find_all('h3')

    def get_href_from_headers(self):
        list_of_names=[]
        for name in self.get_headers():
            if name.parent.attrs: # if h3 had attributes then do
                url= 'https://www.google.com'+ name.parent.attrs['href']
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response=urlopen(req)
                res = response.geturl()
                list_of_names.append(res)
            else:                 # without h3 attributes pass
                pass

        return list_of_names

    # def get_href_google_results(self):
    #     names= self.get_headers()
    #     list_of_names=[]
    #     for name in names:
    #         list_of_names.append(name.parent)
    #     return list_of_names

    def get_text_google_results(self):
        names = self.get_headers()
        res=[]
        for name in names:
            res.append(name.text)
        return res

    def get_sought_from_url(self):
        self.get_href_from_headers()
        for url in self.get_href_from_headers():
            list_of_p = self.get_html_soup(url).find_all('p')
            print(url)
            for p in list_of_p:
                if any(word in p.text for word in self.sought): # search in every p tag our sought and gives it back
                    print(p.text)
            print('\n'*5)





def main():
    i=Google_search('kiev',['kiev','киев','Kiev'])
    # print(i.get_href_from_headers())
    i.get_sought_from_url()


    # for i in i.get_href_google_results():
        # print(i)

# list_of_names=[]
# for name in names:
#     list_of_names.append(name.parent)
# return list_of_names

if __name__ == '__main__':
    main()
