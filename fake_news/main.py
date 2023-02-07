import pandas as pd
df = pd.read_csv('/kaggle/input/fake-news/train.csv')
df.head()

df.isna().sum()

df = df.fillna('Not Available')
df['news'] = df['title'] +'\n '+ df['text']
print(df['news'][0])


from nltk.corpus import stopwords
sw = stopwords.words("english")
len(sw)

import re
lines = []
for i in df.title:
    words = ""
    Q = i.lower()
    Q = re.sub("[^a-z ]","",Q)
    Q = Q.split(" ")
    #print(Q)
    for j in Q:      
        if(j not in sw):
            words = words + " " + j
    lines.append(words)
    
    
    
    from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
es = EarlyStopping(patience=10)
nn = Sequential()
nn.add(Dense(512,input_dim=22870,activation='relu'))
nn.add(Dropout(0.3))
nn.add(Dense(512,activation='relu'))
nn.add(Dropout(0.3))
nn.add(Dense(512,activation='relu'))
nn.add(Dropout(0.3))
nn.add(Dense(1,activation='sigmoid'))
nn.compile(loss='binary_crossentropy',metrics='accuracy',optimizer='adam')
model = nn.fit(xtrain,ytrain, validation_data=(xtest,ytest),callbacks=es,epochs=100)
