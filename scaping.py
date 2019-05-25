import pandas as pd
import requests
import bs4
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer,sent_tokenize
def write_text(st):
    with open('scraping.txt','w') as file_obj:
        file_obj.write(str(st.encode('utf-8')))
    
def apply_nlp():
    with open('scraping.txt','r') as file_obj:
        read_st=file_obj.read()
    
    sent=sent_tokenize(read_st)
    return sent
    
def copy_csv(st,sent):
    data={}
    df=pd.DataFrame(data)
    df['text']=sent #TEXT COLUMN HAS ALL SENTENCES IN DIFFERENT ROWS
    df['tokens']=df['text'].apply(lambda x : word_filter(x)) #  SAME AS DF[].APPLY(F) WHERE F=LAMBDA X:WORDFILTER()
    df.to_csv('scraping.csv')
    
def word_filter(sent):
     x=stopwords.words('english')
     i=re.sub('[\[\]\(\)\{\}\\\/]','',sent) #REMOVING ALL TYPES OF BRACKETS
     tokens=RegexpTokenizer('[A-z]+') #TOKENIZING WORDS ONLY
     tokens=tokens.tokenize(i)
     li=[i for i in tokens if i not in x]
     s=','.join(li) # STRING HAVING WORDS OF SENTENCE SEPARATED BY COMMAS
     return s
    
res=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup=bs4.BeautifulSoup(res.text,'html.parser')

li=soup.select('p') #SELECTING ALL PARA FROM WEBSITE

str_list=[]
for i in li:
    item=i.get_text() #REMOVES ALL TAGS TO GET TEXT
    str_list.append(item)

st="".join(str_list) #COMBINING ALL PARA INTO 1 STRING



#CALLING ALL FUNCTIONS

write_text(st)
sent=apply_nlp()
copy_csv(st,sent)

