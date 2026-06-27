import pandas as pd
import numpy as np


#Data 
"""
numbers =[20,30,40,50]
letters=['a','b','c',50]
scalar = 5
dict = {"a" : 10 ,'b' : 20}
random_numbers = np.random.randint(10,100,5)

pandas_series1 = pd.Series(5, np.arange(0,10,2))
pandas_series2 = pd.Series(0, np.arange(1,10,2))
pandas_series = pd.Series(random_numbers, np.arange(1,20,4))

pandas_series = pd.Series([20,30,40,50,'NaN'],['a','b','c','d','e'])
pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])

# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series['a']
# result = pandas_series['d']
# result = pandas_series[['a','c','e']]
result = pandas_series >=50

print(pandas_series)
print(result)
 print(pandas_series[result])
""" 
# pandas_series3 = pandas_series1 + pandas_series2


# print(pandas_series1)
# print(pandas_series2)
# print(pandas_series3)

# DataFrames
"""
ögrenciler = ['ahmet','ayşe','hakan','mehmet']
notlar = [50,20,100,80]
columns = ['isim','notu','a','b']
dict = {"name": ['ahmet','ayşe','hakan','mehmet'],
        "grade": [50,None,100,80]}

df = pd.DataFrame(dict)
df = df.fillna(0)
print(df)
"""

"""
from numpy.random import randn


df = pd.DataFrame(randn(3,3), index=['a','b','c'],columns=['columns1','columns2','columns3'])

result = type(df.loc['a'][['columns1','columns2']])
result = df.iloc[2,2]

df['columns4'] = pd.Series(randn(3),index=['a','b','c'])
df['columns5'] = df['columns1'] + df['columns3']

result= df.drop('columns3',axis=1,inplace=True )
 
print(df)
print(result)
"""

# Filtreleme

"""
data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data,columns=['column1','column2','column3','column4','column5'])

result= df
result= df.columns
result= df.head() 
result= df.head(10)
result= df.head(-5)
result= df.tail()
result= df['column1'].head()
result= df[['column1','column2']].head()
result= df.column1.head()
result = df.iloc[:,1:3].head()
result = df[5:15][['column1','column2']].head()


result= df[(df >= 50) & (df % 2 ==0)].dropna(how='all')

result= df[['column1','column2']][(df >= 50) & (df % 2 ==0)].dropna(how='all')
result= df[(df >= 50) & (df % 2 ==0)][['column1','column2']].dropna(how='all')
result= df[(df['column1'] >= 50) & (df['column2'] % 2 ==0)].dropna(how='all')[['column1','column2']]
result= df.query('column1 >=50 & column2 % 2 ==0')


result = df[['column1','column2']].head(10)[5:10]
"""


# Groupby

data = {
    'Çalışan': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman': ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'Bilgi İşlem'],
    'Yaş': [30, 25, 45, 50, 23, 34, 42],
    'Semt': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy', 'Tuzla', 'Maltepe'],
    'Maaş': [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}


df = pd.DataFrame(data,index=[1,2,3,4,5,6,7])


result = df.groupby('Departman').groups
result = df.groupby(['Departman','Semt']).groups


#for name, group in df.groupby('Semt'):
        #print(name)
        #print(group)  

result = df.groupby('Semt').get_group('Kadıköy')        
result = df.groupby('Departman').get_group('Muhasebe')        
result = df.groupby('Departman')['Maaş'].sum()
result = df.groupby('Semt')['Yaş'].mean()
result = df.groupby('Semt')['Çalışan'].count()
result = df.groupby('Departman')['Yaş'].max()['Muhasebe']
#result = df.groupby(str(input()))[input()].max()[input()]
#result = df.groupby('Departman')['Maaş'].agg('mean')
#result = df.groupby('Departman')['Maaş'].agg([np.sum,np.mean,np.max,np.min]).loc['Muhasebe']


# Kayır veya Eksik bilgi düzeltme
"""
data= np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])

df =df.reindex(['a','b','c','d','e','f','g','h'])

newcolumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]

df['column4']= newcolumn


result = df

result = df.drop('column1',axis = 1)
result = df.drop(['column1','column2'],axis = 1)
result = df.drop('a',axis=0)
result = df.drop(['a','b','h'],axis=0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df['column1'].isnull().sum()
result = df[df['column1'].notnull()]['column3']
result = df.dropna()
result = df.dropna(axis=1)
result = df.dropna(how = 'all')
result = df.dropna(subset = ['column1','column2'],how = 'all')
result = df.dropna(subset = ['column1','column4'],how = 'any')
result = df.dropna(thresh=3)
result = df.dropna(thresh=4)
result = df.fillna(value= 1)
result = df.fillna(value= 'no value')

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum().sum()



def ortalama(df):
        eleman_sayisi = df.size
        null_sayisi = df.isnull().sum().sum()
        elemanlar_toplami = df.sum().sum()
        null_olmayan_sayisi = eleman_sayisi - null_sayisi
        ortalama = elemanlar_toplami / null_olmayan_sayisi
        return ortalama
        

result = df.fillna(value= ortalama(df))

print(result)
"""

# Join - Merge metodları

"""
customers = {
        'CustomerId': [1,2,3,4],
        'FirstName': ['Ahmet','Ali','Hasan','Canan'],
        'LastName': ['Yılmaz','Korkmaz','Çelik','Toprak']
}

orders = {
        'OrderId': [10,11,12,13],
        'CustomerId':[1,2,5,7],
        'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}


df_customers = pd.DataFrame(customers, columns=['CustomerId','FirstName','LastName'])
df_orders = pd.DataFrame(orders,columns=['OrderId','CustomerId','OrderDate'])

df_customers


print(df_customers)
print(df_orders)


result = pd.merge(df_customers,df_orders,how='inner')
result = pd.merge(df_customers,df_orders,how='left')
#result.fillna('Bulunamadı',inplace=True)

result = pd.merge(df_customers,df_orders,how='right')
#result.fillna(value='Kullanıcı bu listede bulunamadı',inplace=True)
result = pd.merge(df_customers,df_orders,how='outer')
result.fillna('----',inplace=True)

print(result)


customersA = {
        'CustomerId': [1,2,3,4],
        'FirstName': ['Ahmet','Ali','Hasan','Canan'],
        'LastName': ['Yılmaz','Korkmaz','Çelik','Toprak']
}

customersB = {
        'CustomerId': [1,2,3,4],
        'FirstName': ['Yağmur','Çınar','Hakan','Yusuf'],
        'LastName': ['Yılmaz','Korkmaz','Çelik','Toprak']
}


df_customersA = pd.DataFrame(customersA,columns=['CustomerId','FirstName','LastName'])
df_customersB = pd.DataFrame(customersB,columns=['CustomerId','FirstName','LastName'])

result = pd.concat([df_customersA,df_customersB],axis=0)
result = pd.concat([df_customersA,df_customersB],axis=1)


print(result)

"""

# Pandas Metodları


"""
data = {
        'column1': [1,2,3,4,5],
        'column2': [10,20,30,20,25],
        'column3': ['abc','bcaa','ade','cb','dea']
}

df = pd.DataFrame(data)

def kareal(x):
        return  x * x

kareal2 = lambda x: x * x
 
result=df
result=df['column2'].unique()
result=df['column2'].nunique()
result=df['column2'].value_counts()
result = df['column1'] * 2
result = df['column1'].apply(kareal)
result = df['column1'].apply(kareal2)
result = df['column1'].apply(lambda x: x * x)

result = df['column3'].apply(len)
df['column4'] = df['column3'].apply(len)

result = len(df.columns)
result = len(df.index)
result = df.info()

result = df.sort_values('column2')
result = df.sort_values('column4')
result = df.sort_values('column3', ascending= False)

data = {
        'Ay' : ['Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan'],
        'Kategori':['Elektronik','Elektronik','Elektronik','Kitap','Kitap','Kitap','Giyim','Giyim','Giyim'],
        'Gelir': [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
print(df)
result =df.pivot_table(index='Ay',columns='Kategori',values='Gelir')


result = df.shape
result = df.describe()
print(result)

"""


data = {
    'Calisan_Id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'Isim': ['Can Yılmaz', 'Aylin Demir', 'Mert Kaya', 'Selin Öztürk', 'Burak Şahin', 
             'Ece Arslan', 'Deniz Çelik', 'Umut Yıldız', 'Gamze Aydın', 'Okan Koç',
             'Zeynep Bulut', 'Emre Kurt', 'Melis Avcı', 'Tarık Öz', 'Aslı Yalçın'],
    'Departman': ['Satış', 'Pazarlama', 'Satış', 'İK', 'Bilgi İşlem', 
                  'Satış', 'Pazarlama', 'Bilgi İşlem', 'İK', 'Satış',
                  'Pazarlama', 'Satış', 'Bilgi İşlem', 'Satış', 'Pazarlama'],
    'Yas': [28, 34, 23, 41, 29, 31, 25, 38, np.nan, 45, 22, 30, 27, 52, 26],
    'Sehir': ['İstanbul', 'Ankara', 'İzmir', 'İstanbul', 'Ankara', 
              'İstanbul', 'İzmir', 'İstanbul', 'Ankara', 'İzmir',
              'İstanbul', 'Ankara', 'İzmir', 'İstanbul', 'Ankara'],
    'Maas': [52000, 61000, 48000, 55000, 70000, 58000, np.nan, 72000, 53000, 85000, 46000, 59000, 68000, 92000, 50000],
    'Aylik_Satis': [120, 85, 150, np.nan, 90, 110, 75, 95, 60, 190, 80, 130, 100, 210, 70]
}

df = pd.DataFrame(data)

result1 = df.head(7)
result2 = df.shape
result3 = df['Maas'].mean()
result4 = df[(df['Aylik_Satis'] == df['Aylik_Satis'].max())][['Isim','Aylik_Satis']]
result5 = df[(df['Maas'] == df['Maas'].max())][['Isim','Maas']]
result6 = df[(df['Yas'] <= 32) & (df['Yas'] >= 25 )][['Isim','Departman','Maas']]
result7 = df[df['Isim'] == 'Burak Şahin']['Sehir']
result8 = df.groupby('Departman')['Maas'].mean()
result9 = df['Sehir'].unique()
result10 = df.groupby('Departman')['Isim'].apply(len)
result11_1 = df[df['Isim'].str.contains('Ar')]
result11_2 = df[df['Isim'].str.lower().str.contains('ar')]


Maas_Toplam = df['Maas'].sum()
Maas_Ort = Maas_Toplam / (df['Maas'].size - df['Maas'].isnull().sum())

Aylik_Satis_Toplam = df['Aylik_Satis'].sum()
Aylik_Satis_Ort = Aylik_Satis_Toplam / (df['Aylik_Satis'].size - df['Aylik_Satis'].isnull().sum())


# result12
df['Maas'].fillna(value=Maas_Ort,inplace=True)
df['Aylik_Satis'].fillna(value=Aylik_Satis_Ort,inplace=True)


print(f'result1 = \n{result1}')
print(f'result2 = \n{result2}')
print(f'result3 = \n{result3}')
print(f'result4 = \n{result4}')
print(f'result5 = \n{result5}')
print(f'result6 = \n{result6}')
print(f'result7 = \n{result7}')
print(f'result8 = \n{result8}')
print(f'result9 = \n{result9}')
print(f'result10 = \n{result10}')
print(f'result11_1 = \n{result11_1}')
print(f'result11_2 = \n{result11_2}')
print(df[['Isim','Maas','Aylik_Satis']])