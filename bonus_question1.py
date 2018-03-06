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
c=[list1,list2,list3]
data=sum(c,[])

#function for removing links, tags in the text of the tweets
def clean_text(text):
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

#function to analyze given text it return 1 if sentence is +ve otherwise return 0
def analyze_sentiment(text):
   
    analysis = TextBlob(clean_text(text))
    if analysis.sentiment.polarity > 0:
        return 1
    else:
        return 0


#storing words which are positive in nature in a list
positive_things=["Good","good","very good","Very Good","Nice","nice"]

#variable to check references in text of the tweet belongs to Donald Trump
ref="@realDonaldTrump"

x=0;
count=0

#iteration in the list 
for i in data:
    x=0
    if ref in i[4]:
        #cleaning the text 
        cleaned_text=clean_text(i[4])
        #checking any positive word present in cleaned_text
        for k in positive_things:
            if k in cleaned_text:
                #if positive word is present check the polarity of text
                x=analyze_sentiment(cleaned_text)
                #if polarity is 1 increase count by 1
                if(x==1):
                    count=count+1


#calculating percentage of positive tweet references to Donald Trump
a=(float(count)/float(len(ref)))*100

print("Total "+str(a)+"% of tweets that are positive in nature ")


