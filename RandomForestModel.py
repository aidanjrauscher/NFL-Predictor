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

y = train_data["Won"] #have Win for team A = 1 Loss for team A = 0
features = ["PassYardsA", "PassYardsB", "YardsPerAttemptA", "YardsPerAttemptB"]#Add more! 
x = pd.get_dummies(train_data[features])
x_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)#Actually chance, probably more depth and estimators
model.fit(x, y)
predictions = model.predict(x_test)

output = pd.DataFrame({'Team': test_data.PassengerId, 'Won': predictions})

#TODO Have output put into specific folder 
