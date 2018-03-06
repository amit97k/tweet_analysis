import pandas as pd
import json


#Solution for Joining of datasets

#twitter data on date 01/11/2017 to 03/11/2017 as df1,df2 and df3 respectively
df1=pd.read_json('2017-11-01.json')

df2=pd.read_json('2017-11-02.json')

df3=pd.read_json('2017-11-03.json')


#joining of dataframe from 01/11/2017 to 03/11/2017 into a single dataframe
df_final = [df1, df2, df3]
df = pd.concat(df_final)
print(df)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("\n\n\n")


#**************************************************************************************************

# Solution for references to Donald Trump:

ref = df[df['text'].str.contains("@realDonaldTrump")]


#All references to Donald Trump
print("The account referencing to Donald Trump are:\n")
print(ref)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("\n\n\n")



#*************************************************************************************************


# Solution for % of accounts that tweets about Donald Trump


total_accounts=df.groupby('user_id').size().shape


# ref_donald_account means account that references Donald Trump's Account
ref_donald_account = ref.groupby('user_id').size().shape

x=ref_donald_account[0]
y=total_accounts[0]

percentage=(float(x)/float(y))*100
result=str(percentage)
print("Total "+result+"% of people references to Donald Trump.")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("\n\n\n")


#*************************************************************************************************


# Solution for frequency of tweets about Donald Trump

freq=ref.groupby(['user_id','screen_name'])['text'].count()
#sorting user'id based on the count in descending order
accounts = freq.nlargest(ref_donald_account[0])
print("The frequency of accounts that tweets about Donald Trump in descending order:")
print(accounts)
