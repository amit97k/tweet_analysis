from textblob import TextBlob
import re
import json
import pandas as pd

df1=pd.read_json('2017-11-01.json')

df2=pd.read_json('2017-11-02.json')

df3=pd.read_json('2017-11-03.json')

list1=df1.values.tolist()

list2=df2.values.tolist()

list3=df3.values.tolist()

#concatenation lists 1, 2 and 3
final_list=[list1,list2,list3]
flag=sum(final_list,[])

#function for removing links, tags in the text of the tweets
def cleaner(text):
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

#function to analyze given text it return 1 if sentence is +ve otherwise return 0
def sentiment_analysis(text):
   
    temp= TextBlob(cleaner(text))
    if temp.sentiment.polarity > 0:
        return 1
    else:
        return 0
    

#storing words which are positive in nature in a list
search_words=["Good","good","very good","Very Good","Nice","nice"]

#variable to check references in text of the tweet belongs to Donald Trump
ref="@realDonaldTrump"

x=0;
count=0

 
for i in flag:
    x=0
    if ref in i[4]:
        final_text=cleaner(i[4])
        for k in search_words:
            if k in final_text:
                x=sentiment_analysis(final_text)
                if(x==1):
                    count=count+1


#percentage calculation
result=(float(count)/float(len(ref)))*100

print("Total "+str(result)+"% of tweets that are positive in nature ")
