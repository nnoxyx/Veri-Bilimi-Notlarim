
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
file_path = "Titanic-Dataset.csv"

df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "yasserh/titanic-dataset",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print(df.columns)


df = df.drop(columns=["PassengerId","Name","Ticket"])

print(df.columns)
print(df.head())


df['Sex'] = df['Sex'].replace('male','0',)
df['Sex'] = df['Sex'].replace('female','1',)
print(df.head())

Age_mean= df['Age'].sum() / (df['Age'].size - df['Age'].isnull().sum())

print(Age_mean)

df['Age'] = df['Age'].fillna(Age_mean)
print(df.head(20))

df['Family Size'] = df['SibSp'] + df['Parch']
print(df.head(20))

df['Kabin_Var_Mi'] = df['Cabin'].notna().astype(int)
df['Embarked'] = df['Embarked'].replace('S','0')
df['Embarked'] = df['Embarked'].replace('C','1')
df['Embarked'] = df['Embarked'].replace('Q','2')
print(df.head(20))

df = df.drop(columns=["Cabin"])

print(df[df['Embarked'].isna()])
df['Embarked'].dropna()






df_cleaned = pd.DataFrame(df)

file_path = 'titanic_temizlenmis_veri.csv'
df_cleaned.to_csv(file_path, index=False, encoding='utf-8-sig')
print(f"File saved to {file_path}")
