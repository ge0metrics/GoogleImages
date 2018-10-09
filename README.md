# GoogleImages
Search and download up to 100 images in full resolution from google images

# How to use (programmers)
* Make sure you have the following libraries installed:
  * beautifulsoup4
  * requests-html
* Download and extract this repository
* Move `GoogleImages.py` to your working directory
* Include in your code `from GoogleImages import GoogleImages` to import the script
* Instantiate the class with `gi=GoogleImages()` 
  * You can do `gi=GoogleImages(outputs=False)` if you would rather not see any output
* `gi.search("cat memes")` to start a search and load `gi` with the results
  * You can do `gi.search("cat memes",limit=5)` if you want to limit the search to only 5 results
  * It is limited to a maximum of 100, you cannot exceed this
* `gi.download()` to download the images to a folder that will be created by the script
  * Sometimes URLs are broken and the image cannot be downloaded from them
  * If `outputs=True`, you will be able to see when an image couldn't be downloaded
* `print(gi.images)` to see what images have been found
  * They are stored in URL format
  * It will be reset and overwritten every time a new search is performed
  
# How to use (everyone else)
* Assuming you just want to use this to download lots of images quickly
* Download and extract this repository
* Run `Downloader.exe`
* Type in your search query
* Set a limit, bearing in mind the maximum is 100
* Watch as your images are downloaded

# Extra notes (for everybody)
* The program will now detect `.png`, `.jpg` and `.gif` filetypes. If it doesn't detect those, it will save as `.jpg`.
* Due to the way this program works, very fast and repetitive access may cause Google to block you from making more requests, therefore it is advised you don't abuse this tool
