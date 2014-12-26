from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests
import os
import wx
import time


#+++++++++++++++VARIABLES+++++++++++++++++++++++++++++++#
manga_info = {}
manga_base_link = {}
biggest = []
name = []
user_display = {}
dl = {}
uls = []
links = {}
#=+++++++++++++++++++++++++++Intro+++++++++++++++++++++++++++++++++++++#
print "-"*50
print "         CMMD Alpha 4.0               "
print "Coming up:\n1.Faster download\n2.More downloadable sites\n3.Better GUI\n4.User friendlyness(I hope)"
print "Currently sapphire supports only Mangafox.Support for more sites will be included in future builds"
print "-"*50
print "Gathering Manga list from mangafox,please wait....."
#+++++++++++Poorly made functions for gui.. :/ ++++++++++++++++++++++++++++++#
def list_viewer(parent = None,message = '',caption = "Manga List From Mangafox",choices = ''):
  app = wx.App()
  list_box = wx.SingleChoiceDialog(parent,message,caption,choices)
  list_box.ShowModal()
  result = list_box.GetStringSelection()
  list_box.Destroy()
  app.MainLoop()
  return result
def ask_url_manga(parent = None,message = '',caption = "URL to desired manga..."):
    app = wx.App()
    dlg = wx.TextEntryDialog(parent,message,caption)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    app.MainLoop()
    return result
def ask_chapter_number(parent = None,message = '',caption = "Chapter number?"):
    app = wx.App()
    dlg = wx.TextEntryDialog(parent,message,caption)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    app.MainLoop()
    return result
def ask_folder_name(parent = None,message = '',caption = "Folder to download to?"):
    app = wx.App()
    dlg = wx.TextEntryDialog(parent,message,caption)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    app.MainLoop()
    return result

#===================DO NOT UNCOMMENT=======================#
"""
source = urlopen("http://mangafox.me/manga")
mangafox = open("mangafox.dat",'w')
mangafox.write(source.read())
mangafox.close()
fox = open("mangafox.dat",'r')
soup = BeautifulSoup(fox)
fox.close()
mangalist = soup.find_all("div",{"class":"manga_list"})
uls = []
links = {}
for x in mangalist:
  for li in x.findAll('li'):
    for y in li.findAll('a'):
      uls.append(y.text)
      links.update({y.text:y['href']})
"""
if os.path.isfile("mangafox.dat"):
  start = time.time()
  fox = open("mangafox.dat",'r')
  soup = BeautifulSoup(fox)
  fox.close()
  mangalist = soup.find_all("div",{"class":"manga_list"})
  for x in mangalist:
    for li in x.findAll('li'):
        for y in li.findAll('a'):
          uls.append(y.text)
          links.update({y.text:y['href']})
  print "exsisted"
  print "time",(time.time()-start)
else:
  start = time.time()
  source = urlopen("http://mangafox.me/manga")
  mangafox = open("mangafox.dat",'w')
  mangafox.write(source.read())
  mangafox.close()
  fox = open("mangafox.dat",'r')
  soup = BeautifulSoup(fox)
  fox.close()
  mangalist = soup.find_all("div",{"class":"manga_list"})
  for x in mangalist:
    for li in x.findAll('li'):
      for y in li.findAll('a'):
        uls.append(y.text)
        links.update({y.text:y['href']})
  print "Had to download"
  print "time",(time.time()-start)
print "Done! Prompting user..."
xx = list_viewer(message = 'Manga?',choices = uls)
print links[xx]

#++++++++++++Primary URL+++++++++++++++++++++++++++++++++#
#source_url = ask_url_manga(message = "URL for the manga's info page: ")
#source_url = raw_input("URL for the manga's info page: ")
source_url = links[x]
source = urlopen(source_url)



#++++++++++++++Chapter Names+++++++++++++++++++++++++++++#
init_soup = BeautifulSoup(source)
chpt_link = init_soup.find_all("a",{"class":"tips"})
for links in chpt_link:
	found = links.string
	manga_info.update({found:links['href']})
	manga_base_link.update({found:links['href'][:-6]})
	name.append(found)

a = name
a.reverse()
y = -1
print"+"*50
print" --------            ---------------"
print"|Chapter |-----------| Chapter Name |"
print" --------            ---------------"
for x in range(len(a)):
    y +=1
    xx = y+1
    print " "+str(xx)+"---------------"+a[y]
    user_display.update({xx:a[y]})


#++++++++++++++++++Page Counter+++++++++++++++++++++++++#
#Get the chapter user wants to download
chpt_num = int(ask_chapter_number(message = 'Chapter to download'))
#Analyze page number
chapter_url = manga_info[a[chpt_num-1]]
print "Chapter link: ",manga_info[a[chpt_num-1]]

chapter_parse = urlopen(chapter_url)
chapter_soup = BeautifulSoup(chapter_parse)
c = chapter_soup.find("select",{"class":"m"}).find_all("option")
for value in c:
  biggest.append(value.text)
total_page = int(biggest[-2])
manga_info.update({"page":biggest[-2]})
direc = ask_folder_name(message = 'please input the folder name you want the manga to be downloaded to: ')
#os.mkdir(a[chpt_num])
#os.chdir(a[chpt_num])
os.mkdir(direc)
os.chdir(direc)

print manga_base_link[a[chpt_num-1]]

dl_url = manga_base_link[a[chpt_num-1]]


#++++++++++++++++++Downloader+++++++++++++++++++++++++++#
x = 0
while x < total_page:
  x +=1
  base = dl_url+str(x)+".html"
  dl.update({x:base})
  #print dl
for i in range(100):
  key = i+1
  format = str(key)+".jpg"
  print "downloading page "+str(key)
  url = urlopen(dl[key])
  soup = BeautifulSoup(url)
  image = soup.find("img",{"id":"image"})
  f = open(format,'wb')
  f.write(requests.get(image['src']).content)
  f.close()
print "Download compleat"
