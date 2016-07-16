from bs4 import BeautifulSoup

soup = BeautifulSoup(open('Resources\Plain Text HTML.html'),'html.parser', from_encoding="utf-8")

exportfile = open('Resources\out.txt','w')

exportfile.writelines(soup.text)
exportfile.close()