#Use pip install pandas
#And pip install -U scikit-learn

import numpy as np #to use linear algebra
import pandas as pd #For data processing our CSV Files
import os



for dirname, _, filenames in os.walk(''):#Add path to input data inside ' ' 
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
train_data = pd.read_csv('')#Add path to data we want trained on 
train_data.head()

test_data = pd.read_csv('')#Add path to data we want tested on
test_data.head()


from sklearn.ensemble import RandomForestClassifier #Use RandomForestClassifier to Train

y = train_data["T1 Outcome"] 
features = ["T1 Location", "T2 Location", "T1 Avg Points", "T2 Avg Points", "T1 Avg Yards","T2 Avg Yards", "T1 NPY/A", "T2 NPY/A", "T1 NRY/A", "T2 NRY/A", "T1 Avg Points Def", "T2 Avg Points Def", "T1 Avg Yards Def", "T2 Avg Yards Def", "T1 NPY/A Def", "T2 NPY/A Def","T1 NRY/A Def", "T2 NRY/A Def", "T1 4th Def", "T2 4th Def", "T1 3rd", "T2 3rd", "T1 4th", "T2 4th", "T1 3rd Def", "T2 3rd Def"]
x = pd.get_dummies(train_data[features])
x_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)#Actually chance, probably more depth and estimators
model.fit(x, y)
predictions = model.predict(x_test)

output = pd.DataFrame({'T1': test_data.T1, 'T1 Outcome': predictions})

#TODO Have output put into specific folder 
