# %%
import time
import pandas as pd
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


#Biz has 10 pages
df_all = []
i=0
dataframe = pd.DataFrame(columns=['Subject', 'Comment', 'Post Number', 'Replies'])
for i in range(10):
    i=i+1
    url = (("https://a.4cdn.org/biz/") + str(i) + '.json')
    data = get_jsonparsed_data(url)

    list = len(data['threads'])
   
    for i in range(0, list): 
      try:
          comment = data['threads'][i]['posts'][0]['com']
          subject = data['threads'][i]['posts'][0]['sub']
          postno = data['threads'][i]['posts'][0]['no']
          replies = data['threads'][i]['posts'][0]['replies']
      except KeyError:
          subject = 'No subject'
          postno = data['threads'][i]['posts'][0]['no']
          replies = data['threads'][i]['posts'][0]['replies']
      except KeyError:
          comment = data['threads'][i]['posts'][0]['sub']
      dataframe = dataframe.append({'Subject':subject, 'Comment':comment, 'Post Number':postno, 'Replies':replies}, ignore_index=True)
    time.sleep(.02)
    i=i+1

dataframe

# %%
df2 = dataframe

for i in range(0,5):
  try:
    postno, replies = get_numbers(i) 
    url = (("https://a.4cdn.org/biz/thread/") + str(postno) + '.json')
    data = get_jsonparsed_data(url)
    replies_text = []
    print(replies_text)
    dataframe2['reply_list'][i] = url
  except HTTPError:
    dataframe2['reply_list'][i] = '404'
    print(replies_text)
    pass
 
    for j in range(replies):
      time.sleep(.5)
      try:
        reply = data['posts'][j]['com']
        replies_text.append(reply)
        print(replies_text)
      except KeyError: 
        reply = 'Key Error'
        print(replies_text)
      except IndexError:
        reply = 'Index Error'
        print(replies_text)
    print(replies_text)
    dataframe2['reply_list'][i] = replies_text


dataframe2


# %%
#for i in range(0,10):
url = (("https://a.4cdn.org/biz/thread/") + str(44454159) + '.json')
data = get_jsonparsed_data(url)
reply = data['posts'][5]
#print(reply)
#print(dataframe.iloc[197])
#data['threads'][18]['posts'][0]['sub']
reply
#dataframe['Post Number'][6]
#https://a.4cdn.org/biz/thread/44454159.json

# %% [markdown]
# ##some dudes working code 
# 
# '''import requests
# r = requests.get('https://a.4cdn.org/pol/catalog.json')
# r = r.json()
# for pages in range(0, len(r)):
#     for threads in r[pages]['threads']:
#         print(threads)

# %%
dataframe2 = dataframe
dataframe2['reply_list'] = 1

# %%
from urllib.error import HTTPError

replies_text = []

def get_numbers(i):  
    postno = dataframe2['Post Number'][i]
    replies = dataframe2['Replies'][i]
    return(postno, replies)



#for i in range(0,len(dataframe2['Replies']))
#for i in range(len(dataframe2['Replies'])):

for i in range(0,len(dataframe2['Replies'])):
  try:
    postno, replies = get_numbers(i) 
    url = (("https://a.4cdn.org/biz/thread/") + str(postno) + '.json')
    data = get_jsonparsed_data(url)
    replies_text = []
  except HTTPError:
    dataframe2['reply_list'][i] = '404'
    pass
    for j in range(0, replies):
      try:
        reply = data['posts'][j]['com']
        replies_text.append(reply)
      except KeyError: 
        reply = 'Key Error'
      except IndexError:
        reply = 'Index Error'
    print(replies_text)
    dataframe2['reply_list'][i] = replies_text
   

#for i in range(10):
 #   i=i+1
  #  url = (("https://a.4cdn.org/biz/") + str(i) + '.json')
  #  data = get_jsonparsed_data(url)
#print(replies_text)

# %%


# %%
for i in range(10):
    i=i+1
    url = (("https://a.4cdn.org/biz/") + str(i) + '.json')
    data = get_jsonparsed_data(url)
print(replies_text)

#dataframe2.tail(50)
#for j in range(0,10):
 # print('penis')
  #for i in range(0,20):
   # print(str(i))
#postno, reply = get_numbers(2)
#print(postno)
#print(reply)


# %%
replies_text

# %%


# %%
#CATALOG

url = ("https://a.4cdn.org/biz/5.json")
data = get_jsonparsed_data(url)

# %%

num_replies = int(data['posts'][0]['replies'])
replies = []

for i in range(num_replies):
    reply = data['posts'][i]['com']
    replies.append(reply)

replies

soup = BeautifulSoup() 
def beautify (reply): 
  soup = BeautifulSoup(reply) 
  reply = soup.get_text() 
  return reply

#df["clean_text"] = df.description.apply(lambda text: beautify(reply))

replies


# %%
''''This is to get the replies into a long string for NLP, need to use regex too

#stringy = str(replies)
#soup = BeautifulSoup(stringy)
#print(soup.get_text())

'''



# %%
threads['no'][1]

# %%
import requests
from datetime import datetime as dt
r = requests.get('https://a.4cdn.org/pol/catalog.json')
r = r.json()
def gen_chan():
    for idx, page in enumerate(r):
        for thread in r[idx]['threads']:
            yield thread
def get_threads(key: str, default='NaN'):
    return threads.get(key, default)
for threads in gen_chan():
    no = get_threads('no')
    now = get_threads('now')
    time = get_threads('time')
    my_time = dt.today()
    com = TextMaster.strip_html(get_threads('com'))
    name = get_threads('name')
    trip = get_threads('trip')
    ids = get_threads('id')
    capcode = get_threads('capcode')
    filename = get_threads('filename') + get_threads('ext')
    resto = get_threads('resto')
    semantic_url = get_threads('semantic_url')
    replies = get_threads('replies')
    images = get_threads('images')
    url = TextMaster.extract_url(get_threads('com'))
    sent = TextMaster.textblob_sentiment(get_threads('com'))
    if 'last_replies' in threads:
        for comment in threads['last_replies']:
            com_com = comment.get('com', 'NaN')
            resto_com = comment.get('resto', 'NaN')
            now_com = comment.get('now', 'NaN')
            time_com = comment.get('time', 'NaN')
            fname_com = comment.get('filename', 'NaN')
            url_com = comment.get('com')
            sent_com = comment.get('com')

# %%
gen_chan()

# %%
def update_dataframe():

    for i in range(0, list): 
        try:
            comment = data['threads'][i]['posts'][0]['com']
            subject = data['threads'][i]['posts'][0]['sub']
        except KeyError:
            subject = 'No subject'
        print(subject)
        print(comment + ' ,')
        dataframe = dataframe.append({'Subject':subject, 'Comment':comment}, ignore_index=True)
    return

# %%
def update_dataframe():
    dataframe = pd.DataFrame(columns=['Subject', 'Comment'])
    list = len(data['threads'])

    for i in range(0, list): 
        try:
            comment = data['threads'][i]['posts'][0]['com']
            subject = data['threads'][i]['posts'][0]['sub']
        except KeyError:
            subject = 'No subject'
        print(subject)
        print(comment + ' ,')
        dataframe = dataframe.append({'Subject':subject, 'Comment':comment}, ignore_index=True)
    return

# %%
update_dataframe()


