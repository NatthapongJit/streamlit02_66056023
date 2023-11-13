import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 01
# https://docs.streamlit.io/library/api-reference/write-magic
st.markdown('สวัสดี! **Streamlit**')
st.title('Layout and Decoration')
st.write("""
เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1, col2, col3 = st.columns(3)
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

# trees_df = pd.read_csv('trees.csv')
# df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']
# st.line_chart(df_dbh_grouped)

st.title('แปลผล')
st.write("""
ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศูนย์กลาง 3' (2721 ต้น)
""")
# st.bar_chart(df_dbh_grouped)
# st.area_chart(df_dbh_grouped)

# st.write('จากโค้ด', '`st.markdown("สวัสดี!")`')
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# }))
# st.divider()