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

        self.outputs=outputs

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
                        Type=self.get_type(image)
                        filename="{}/{}{}{}".format(self.path,self.title,index,Type)
                        urllib.request.urlretrieve(image,filename)
                        if self.outputs==True:
                            print(filename)
                    else:
                        if self.outputs==True:
                            print("Could not fetch url: {}".format(image))
                except urllib.error.HTTPError as error:
                    if self.outputs==True:
                        print(error)
                except urllib.error.URLError as error:
                    if self.outputs==True:
                        print(error)

    def get_type(self,image):
        if ".gif" in image:
            return ".gif"
        elif ".png" in image:
            return ".png"
        elif ".jpg" in image:
            return ".jpg"
        else:
            return ".jpg"
