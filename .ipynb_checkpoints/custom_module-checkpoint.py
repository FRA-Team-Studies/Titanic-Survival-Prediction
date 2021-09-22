import pandas as pd

def femaleOrSurvived(row):
    if (row['female'] == 1) or (row['Survived'] == 1):
        val = 1
    else:
        val = 0
    return val

def femaleAndSurvived(row):
    if (row['female'] == 1) and (row['Survived'] == 1):
        val = 1
    else:
        val = 0
    return val

def maleOrSurvived(row):
    if (row['male'] == 1) or (row['Survived'] == 1):
        val = 1
    else:
        val = 0
    return val

def maleAndSurvived(row):
    if (row['male'] == 1) and (row['Survived'] == 1):
        val = 1
    else:
        val = 0
    return val

def changeColumnNames(df):
    df = df.rename(columns={'Pclass': 'TICKET_CLASS'})
    df = df.rename(columns={'SibSp': 'SIBLING_SPOUSE_ON_BOARD'})
    df = df.rename(columns={'Parch': 'PARENT_CHILDREN_ON_BOARD'})
    df = df.rename(columns={'Sex': 'SEX'})
    df = df.rename(columns={'Embarked': 'EMBARKED'})
    df = df.rename(columns={'Name': 'NAME'})
    df = df.rename(columns={'Ticket': 'TICKET'})
    df = df.rename(columns={'Cabin': 'CABIN'})
    df = df.rename(columns={'Age': 'AGE'})
    df = df.rename(columns={'Fare': 'FARE'})
    df = df.rename(columns={'Survived': 'SURVIVED'})
    df = df.rename(columns={'PassengerId': 'PASSENGER_ID'})
    
    return df

def process(df):
    df = df.dropna()
    
    dummies = []
    cols = ['TICKET_CLASS','SEX','EMBARKED']
    for col in cols:
     dummies.append(pd.get_dummies(df[col] ,prefix = col + '_'))
    
    titanic_dummies = pd.concat(dummies, axis = 1)
    df = pd.concat((df,titanic_dummies), axis = 1)
    df = df.drop(['TICKET_CLASS','SEX','EMBARKED'], axis = 1)
    df['AGE'] = df['AGE'].interpolate()
    
    return df