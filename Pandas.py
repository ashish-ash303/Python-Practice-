# from IPython.display import display
from numpy import row_stack
import pandas as pd

jobs = pd.read_csv('indeed.csv')
# Stores the Date in dict form means key and value
# print(jobs)
# print(jobs.head(5))
# print(type(jobs))
# print(jobs.info)
# print(jobs.describe()) Describe the date
# print(jobs.tail(3)) To get the last 3 dateS
# print(jobs.columns) Define the index
# print(jobs.shape) TO find shape of csv file means column and
# print(jobs.at[6, 'title'])  Used to find Specific Value
# jb = jobs[["title", "company", "summary"]] Used to find Specific Value
# jobs_list = jb.copy()
# print(jobs_list)
# print(jobs.loc[8])To get the specific row
#  if it not find the value it gives NaN
# print(jobs.first_valid_index()) To know from where the value Start
# print(jobs.sample(5)) To get the Sample of data
# total_jobs = jobs["title"].sum()
# Sum is used add the things NaN value will be ignored
# print(total_jobs)
# We Can Make Our own list

# pd.option_context("display.max_rows", 25):
# display(jb)
# print(jobs.drop(columns=['company'], inplace=True))
# print(js)
# print(jobs.sort_values('title', ascending=False).head(10))
# print(jobs.loc[20:25])
# TO convert into new date type pd.to
# groupby:- TO make groupsLook within range


# df_year=np.arange('2014-02-17', '2021-12-31', dtype='datetime64[Y]')
# df_year
# pd.date_range(start='2014-09-17', periods=7,freq='Y')
