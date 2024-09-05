import pandas as pd 
from dataprep.eda import create_report
import re

filed=pd.read_csv('gpt.csv')
#prof_rep=create_report(filed )
#prof_rep.save('index.html')
from textblob import TextBlob 
print(filed.head())
cols_list= [x for x in filed.columns]
appendable_List=[]


for j in range(len(filed)): 
    textt=re.sub(r'[^\w\s]', '', filed['Comment'][j])
          
      
    text_blob = TextBlob(textt)
    sentiment_ = text_blob.sentiment

    if sentiment_.polarity < -0.5:
        actual_sentiment = "Very Negative"
    elif -0.5 <= sentiment_.polarity < -0.1:
        actual_sentiment = "Negative"
    elif -0.1 <= sentiment_.polarity <= 0.1:
        actual_sentiment = "Neutral"
    elif 0.1 < sentiment_.polarity <= 0.5:
        actual_sentiment = "Positive"
    else:
        actual_sentiment = "Very Positive"

    if sentiment_.subjectivity == 0:
        actualuality = "Objective"
    elif 0 < sentiment_.subjectivity <= 0.5:
        actualuality = "Mixed"
    else:
        actualuality = "Subjective"


    appendable_List.append([actual_sentiment,actualuality, sentiment_.polarity, sentiment_.subjectivity])
    if j%1000==0: print(j/len(filed), end=" ")
    
print('Sentiments Analyzed')    
df1=pd.DataFrame(filed)
df2=pd.DataFrame(appendable_List)
finaldf=pd.concat([df1,df2],axis=1)
print('Created DS')
finaldf.to_csv('Pipelined.csv')                   
print('Exported')
     