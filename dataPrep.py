import pandas as pd
# set > 100 year olds' birthdate as 0
def clear_birth_year(by):
    if by <= 1919:
        return 0
    else: 
        return by

#Data found at: https://s3.amazonaws.com/tripdata/index.html
print('Data prep, \n data found at https://s3.amazonaws.com/tripdata/index.html')
print('Required files:')
print('201702-citibike-tripdata.csv')
print('201802-citibike-tripdata.csv')
print('201808-citibike-tripdata.csv')
print('201902-citibike-tripdata.csv')

print('February 2017 data from file 201702-citibike-tripdata.csv...')
print('Change column names')
feb_2017=pd.read_csv('201702-citibike-tripdata.csv')
feb_2017.columns=['tripduration','starttime','stoptime','start station id','start station name','start station latitude','start station longitude','end station id','end station name','end station latitude','end station longitude','bikeid','usertype','birth year','gender']         
print('Set birth years over 100 to 0')
feb_2017['birth year'] = feb_2017['birth year'].apply(clear_birth_year)
feb_2017['birth year'].fillna(0)
print('Save to file: feb2017.csv')
#feb_2017.head()
feb_2017.to_csv('feb2017.csv')

print('February 2018 data from file 201802-citibike-tripdata.csv...')
feb_2018=pd.read_csv('201802-citibike-tripdata.csv')
print('Set birth years over 100 to 0')
feb_2018['birth year'] = feb_2018['birth year'].apply(clear_birth_year)
print('Save to file: feb2018.csv')
feb_2018.to_csv('feb2018.csv')

print('August 2018 data from file 201808-citibike-tripdata.csv...')
aug_2018=pd.read_csv('201808-citibike-tripdata.csv')
print('Set birth years over 100 to 0')
aug_2018['birth year'] = aug_2018['birth year'].apply(clear_birth_year)
print('Save to file: aug2018.csv')
aug_2018.to_csv('aug2018.csv')

print('February 2019 data from file 201902-citibike-tripdata.csv...')
feb_2019=pd.read_csv('201902-citibike-tripdata.csv')
print('Set birth years over 100 to 0')
feb_2019['birth year'] = feb_2019['birth year'].apply(clear_birth_year)
print('Save to file: feb2019.csv')
feb_2019.to_csv('feb2019.csv')