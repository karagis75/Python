#Python Compare two PDF / Sort it key values and find duplicates and create an excel file with all duplicates values
#  
# downloading first PDF published data to first CSV (400 pages supported at a time)
import tabula
tabula.convert_into("First.pdf", "first.csv", output_format="csv", pages="1-400")

# downloading Second PDF published data to second CSV (400 pages supported at a time)
import tabula
tabula.convert_into("First.pdf", "second.csv", output_format="csv", pages="1-400")

import pandas as pd

firstdataframe = pd.read_csv('First.csv')
seconddataframe = pd.read_csv('Second.csv')

#sort first dataframe and Second data frame  -- Firstkey and second key column names exists in first and second csv files respectively
# Sort first 35250 records..Change this value is no of records in CSV is more th 35250..This is done to ensure performance

firstdataframe_sorted= firstdataframe[:35250].sort_values('Firstkey')
seconddataframe_sorted= seconddataframe[:35250].sort_values('Secondkey')

#Format firstkey to string so that it can be compared against second 

formatedFirstkey = firstdataframe_sorted.Firstkey.astype(str) 

#create list of only from values of formated first key value
firstList = set(formatedFirstkey)

# Create new Target Dataframe with duplicate value found in second data frame and its other column (if keys are same between first and #second)

targetDF = seconddataframe_sorted[seconddataframe_sorted.Secondkey.isin(firstList)==True]

# This clean up is required target date frame since data is pulled from PDF data in tabular format but downloadable
# removing invalid records where keyvalue is null

target2DF  =targetDF[~(targetDF.keyvalue.isnull())]

#Create an excel as a support for further analysis

target2DF.to_excel('duplicates_key_and_other_columns.xls') 