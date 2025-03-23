import pandas as pd
import numpy as np

# Data Preparation
data = dict(
    KEN={'COUNTY': 'Kenya', 'POP': 54.7, 'AREA': 580.4, 'GDP': 121.50, 'CONT': 'Africa', 'IND_DAY': '1963-12-02'},
    CHN={'COUNTY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96, 'GDP': 12_234.78, 'CONT': 'Asia'},
    IND={'COUNTY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26, 'GDP': 2_575.67, 'CONT': 'Asia',
         'IND_DAY': '1947-08-15'},
    USA={'COUNTY': 'US', 'POP': 329.74, 'AREA': 9_833.52, 'GDP': 19_485.39, 'CONT': 'N.America',
         'IND_DAY': '1776-07-04'},
    IDN={'COUNTY': 'Indonesia', 'POP': 268.07, 'AREA': 9_910.93, 'GDP': 1_015.54, 'CONT': 'Asia',
         'IND_DAY': '1945-08-17'},
    BRA={'COUNTY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77, 'GDP': 2_055.51, 'CONT': 'S.America',
         'IND_DAY': '1822-09-07'},
    PAK={'COUNTY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91, 'GDP': 302.14, 'CONT': 'Asia', 'IND_DAY': '1947-08-14'},
    NGA={'COUNTY': 'Nigeria', 'POP': 200.96, 'AREA': 923.77, 'GDP': 375.77, 'CONT': 'Africa', 'IND_DAY': '1960-10-01'},
    BGD={'COUNTY': 'Bangladesh', 'POP': 167.09, 'AREA': 147.57, 'GDP': 375.77, 'CONT': 'Asia', 'IND_DAY': '1971-03-26'},
    RUS={'COUNTY': 'Russia', 'POP': 146.79, 'AREA': 17_098.34, 'GDP': 1_530.75, 'IND_DAY': '1992-06-12'},
    MEX={'COUNTY': 'Mexico', 'POP': 126.58, 'AREA': 1_964.38, 'GDP': 1_158.23, 'CONT': 'N.America',
         'IND_DAY': '1810-09-16'},
    JPN={'COUNTY': 'Japan', 'POP': 126.22, 'AREA': 377.97, 'GDP': 4_872.42, 'CONT': 'Asia'},
    DEU={'COUNTY': 'Germany', 'POP': 83.02, 'AREA': 357.11, 'GDP': 3_693.20, 'CONT': 'Europe'},
    FRA={'COUNTY': 'France', 'POP': 67.02, 'AREA': 640.68, 'GDP': 2_582.49, 'CONT': 'Europe', 'IND_DAY': '1789-07-14'},
    GBR={'COUNTY': 'UK', 'POP': 66.44, 'AREA': 242.50, 'GDP': 2_631.23, 'CONT': 'Europe'},
    ITA={'COUNTY': 'Italy', 'POP': 60.36, 'AREA': 301.34, 'GDP': 1_943.48, 'CONT': 'Europe'},
    ARG={'COUNTY': 'Argentina', 'POP': 44.94, 'AREA': 2_780.40, 'GDP': 637.49, 'CONT': 'S.America',
         'IND_DAY': '1816-07-09'},
    DZA={'COUNTY': 'Algeria', 'POP': 43.38, 'AREA': 2_381.74, 'GDP': 167.56, 'CONT': 'Africa', 'IND_DAY': '1962-07-05'},
    CAN={'COUNTY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67, 'GDP': 1_408.68, 'CONT': 'Oceania'},
    AUS={'COUNTY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02, 'GDP': 1_408.68, 'CONT': 'Oceania'},
    KAZ={'COUNTY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90, 'GDP': 159.41, 'CONT': 'Asia',
         'IND_DAY': '1991-12-16'})


# Create pandas DataFrame
# Normally Pandas interpret the outerKeys of data as columns and innerKeys as row. '.T or .transpose()' method to switch to columns to rows and vise verser
countryinfo = pd.DataFrame(data=data).T
print(countryinfo)

# this modifies the Data Type of selected column
country_info = countryinfo.astype(dtype={'POP': np.float64, 'AREA': np.float64, 'GDP': np.float64})


# DataFrame Data Access >>

print('- '*38)
# to view the first 5 items of DataFrame still is possible to index the number of items '.head(7)'
print(country_info.head())

print('- '*38)
# to view the last 5 items of DataFrame still is possible to index the number of items '.tail(7)'
print(country_info.tail(7))

print('- '*38)
# simply access DataFrame columns as in dictionary
print(country_info['CONT'])

print('- '*38)
# to access last 5 list of particular columns
print(country_info[["COUNTY", "AREA", "CONT"]].tail())

print('- '*38)
# .loc uses the label to access row/s
print(country_info.loc['FRA'])
print(f"{'- '*38}\n{country_info.loc['USA':'NGA']}")

print('- '*38)
# .iloc uses the index to access row/s (is Exclusive)
print(country_info.iloc[0])
print(f"{'- '*38}\n{country_info.iloc[0:4]}")

print('- '*38)
# to get a specific value use .at or .iat
# gets the independent day of Kazakhstan
print(country_info.at['KAZ', 'IND_DAY'])
print(country_info.iat[20, 5])

# DataFrame Modification

print('- '*38)
# this modifies a specific value
country_info.iat[20, 5] = '1992-15-16'
print(country_info.iat[20, 5])

print('- '*38)
# this modifies the whole column with the same value
country_info['COUNTY'] = 'Kenya'
print(country_info['COUNTY'])

print('- '*38)
# this modifies a range of columns
country_info.loc[:'IDN', 'COUNTY'] = ['Kenya', 'China', 'India', 'US', 'Indonesia']
# this modifies a row
country_info.loc['FRA'] = ['FRANCE', 67.03, 640.78, 2582.50, 'Europe', '1789-07-14', ]
print(country_info)

print('- '*38)
# this deletes a row
country_info = country_info.drop(labels=['ITA'])
# this inserts a new row
egypt = pd.DataFrame({'COUNTY': 'Egypt', 'POP': 104.10, 'AREA': 1.02, 'GDP': 404.14, 'CONT': 'Africa', 'IND_DAY': '1922-02-28'}, index=['EGY'])
country_info = pd.concat([country_info, egypt])
print(country_info)

# Querying

# selects row that Age is greater than 34
# adult = users_info[users_info["Age"] > 34]
# print(adult)

#
# users_info["Bonus"] = users_info["Salary"]*0.10
# print(users_info)


#  DataFrame Overview >>

print('- '*38)
# returns a summary of all columns + datatype, null count & memory usage
print(country_info.info())

print('- '*38)
# returns overview of the values each column contains NB- only display numeric columns
print(country_info.describe())
print(f"{'- '*38}\n{country_info.dtypes}")

print('- '*38)
# returns a tuple (total NO. of rows, total NO. of columns)
print(country_info.shape)
