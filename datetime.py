
from os import name
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    Return name of selected column
    """
    name_col = serie[col_name].name
    return name_col

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    num_unique = serie[col_name].nunique()
    return num_unique

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    num_missing = serie[col_name].isnull().sum()
    return num_missing

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    num_weekend = (serie[col_name].dt.day_name().isin(['Saturday', 'Sunday'])).sum()
    return num_weekend

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    num_weekday = (~serie[col_name].dt.day_name().isin(['Saturday', 'Sunday'])).sum()
    return num_weekday

  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    today = pd.to_datetime("today")
    num_futureday = (serie[col_name] > today).sum()
    return num_futureday

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    year_1900 = pd.to_datetime("1900-01-01")
    num_1990 = (serie[col_name] == year_1900).sum()
    return num_1990

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    year_1970 = pd.to_datetime("1970-01-01")
    num_1970 = (serie[col_name] == year_1970).sum()
    return num_1970

  def get_min(self):
    """
    Return the minimum date
    """
    date_min = min(serie[col_name])
    return date_min

  def get_max(self):
    """
    Return the maximum date 
    """
    date_max = max(serie[col_name])
    return date_max

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    bar_chart = st.bar_chart(serie[col_name].value_counts())
    return bar_chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    percent = (serie[col_name].value_counts()/serie[col_name].count())*100  
    occurence = serie[col_name].value_counts()
    top_20 = pd.concat([occurence, percent],axis=1).head(20)
    top_20.reset_index(inplace=True)
    top_20.columns.values[0] = "Value"
    top_20.columns.values[1] = "Occurence"
    top_20.columns.values[2] = "Frequency"
    return top_20
