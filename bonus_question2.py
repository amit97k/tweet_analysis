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

#concating list1, list2, list3
list_final=[list1,list2,list3]
flag=sum(list_final,[])


#function remove link, tags from text
def cleaner(text):
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())


#function to analyze given text it return 1 if sentence is +ve otherwise return 0
def sentiment_analysis(text):
   
    temp = TextBlob(cleaner(text))
    if temp.sentiment.polarity > 0:
        return 1
    else:
        return 0


# empty list for storing user_id and score
ref1=[]
ref2=[]

ref="@realDonaldTrump"
count=0
 
for i in flag:
    x=0
    if ref in i[4]:  
        final_text=cleaner(i[4]) 
        #storing the polarity of given text in x
        x=sentiment_analysis(final_text)
        #checking if x is 1 then increasing the % of positive tweet by 1
        if(x==1):
            count=count+1
        ref1.append(i[6])
        ref2.append(x)
        
df = pd.DataFrame({'user_id':ref1,'score':ref2})

# mean of score grouped by user_id
mean=df.groupby(['user_id']).mean()


#finding the number of row in mean_df
length_mean=len(mean)

count=0
for i in range(0,length_mean):
    #checking the mean of score o for each account if it is greater than 50% or not
    if(int(mean.iloc[i,0:1])>0.5):
        count=count+1

#percentage calculation
ans=(float(count)/float(length_mean))*100
print("Total "+str(ans)+ "% of accounts tweets positive about Donald Trump.")

