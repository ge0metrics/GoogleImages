import urllib.request,requests,os,ast
from bs4 import BeautifulSoup
from requests_html import HTMLSession

class GoogleImages:
    def __init__(self,outputs=True):
        opener=urllib.request.build_opener()
        opener.addheaders=[("User-agent","Mozilla/5.0")]
        urllib.request.install_opener(opener)

        self.title=None
        self.path=None
        self.images=None

    def search(self,query,limit=100):
        url="http://google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi7kd3o-ODcAhWIAcAKHSQnAUMQ_AUICigB&biw=1366&bih=633".format(query)
        self.title=query.replace(" ","_")
        self.path="./{}".format(self.title)

        session=HTMLSession()
        r=session.get(url)
        r.html.render()

        soup=BeautifulSoup(r.text,features="html.parser")
        self.images=[]
        for index,image in enumerate(soup.findAll("div",{"class":"rg_meta notranslate"})):
            if index>limit-1:
                return True
            img=ast.literal_eval(image.contents[0])["ou"]
            self.images.append(img)

        return True

    def download(self):
        if not self.path or not self.images or not self.title:
            print("You must search for images before downloading them.")
        else:
            try:
                os.listdir(self.path)
            except FileNotFoundError:
                os.mkdir(self.path)

            for index,image in enumerate(self.images):
                try:
                    if "http" in image:
                        if "gif" in self.title:
                            filename="{}/{}{}.gif".format(self.path,self.title,index)
                        else:
                            filename="{}/{}{}.png".format(self.path,self.title,index)
                        urllib.request.urlretrieve(image,filename)
                        if outputs==True:
                            print(filename)
                    else:
                        print("Could not fetch url: {}".format(image))
                except urllib.error.HTTPError as error:
                    if outputs==True:
                        print(error)
                except urllib.error.URLError as error:
                    if outputs==True:
                        print(error)
