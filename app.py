import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from st_pages import Page, show_pages, add_page_title

show_pages([
    Page("app.py", "Home", "🏠"),
    Page("pages/tab.py", "Tab Layout", "📖"),
    Page("pages/map.py", "Map Layout", "🗺️"),
])

add_page_title()
# st.set_page_config(layout='wide')

st.markdown('สวัสดี! **Streamlit**')
st.title('Layout and Decoration')
st.write("""
เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

owners = st.sidebar.multiselect(
    "Tree Owner Filter",
    trees_df['caretaker'].unique()
)

if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1, col2, col3 = st.columns(3)
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

st.title('แปลผล')
st.write("""
ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศูนย์กลาง 3' (2721 ต้น)
""")

st.divider()

# trees_df = pd.read_csv('trees.csv')
# df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']
#
# col1, col2, col3 = st.tabs(['line chart', 'bar chart', 'area chart'])
# with col1:
#     st.line_chart(df_dbh_grouped)
# with col2:
#     st.bar_chart(df_dbh_grouped)
# with col3:
#     st.area_chart(df_dbh_grouped)

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)