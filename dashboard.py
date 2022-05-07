from datetime import datetime
from json import load
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def load_data():
    aggregated_data = pd.read_csv('dashboard_data/Aggregated_Metrics_By_Video.csv')
    aggregated_data.columns = ['Video', 'Video title', 'Video Publish Time', 'Comments added', 'Shares', 'Dislikes', 'Likes', 'Subscribers Lost', 'Subscribers gained', 'RPM(USD)', 'CPM(USD)', 'Average % viewed', 'Average view duration', 'Views', 'Watch time(hours)', 'Subscribers', 'Average revenue(USD)', 'Impressions', 'Impression ctr']
    aggregated_data['Video Publish Time'] = pd.to_datetime(aggregated_data['Video Publish Time'])
    aggregated_data['Average view duration'] = aggregated_data['Average view duration'].apply(lambda x: datetime.strptime(x, '%H:%M:%S'))
    aggregated_data['Average_duration_sec'] = aggregated_data['Average view duration'].apply(lambda x : x.second + x.minute*60 + x.hour*3600)
    aggregated_data['Engagement ratio'] = (aggregated_data['Comments added'] + aggregated_data['Shares'] + aggregated_data['Dislikes'] + aggregated_data['Likes']) / aggregated_data['Views']
    aggregated_data['Views / sub gained'] = aggregated_data['Views'] / aggregated_data['Subscribers gained']
    aggregated_data.sort_values('Video Publish Time', ascending = False, inplace = True) 

    subscribers_aggregated_data = pd.read_csv('dashboard_data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')

    comments_data = pd.read_csv('dashboard_data/All_Comments_Final.csv')

    time_data = pd.read_csv('dashboard_data/Video_Performance_Over_Time.csv')
    time_data['Date'] = pd.to_datetime(time_data['Date'])

    return aggregated_data, subscribers_aggregated_data, comments_data, time_data 

aggregated_data, subscribers_aggregated_data, comments_data, time_data = load_data()   

aggregated_data_differential = aggregated_data.copy()
metric_date_12mo = aggregated_data_differential['Video Publish Time'].max() - pd.DateOffset(months =12)
median_agg = aggregated_data_differential[aggregated_data_differential['Video Publish Time'] >= metric_date_12mo].median()

#BUILDING THE DASHBOARD
add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics','Individual Video Analysis'))  