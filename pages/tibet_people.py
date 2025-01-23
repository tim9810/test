import matplotlib.pyplot as plt
import matplotlib
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import requests

matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

st.set_page_config(layout="wide")
st.title("臺南市各行政區賑災公共設施統計資料")
st.header(":fire_engine:臺南市各行政區消防局點位")

markdown = """
以下為台南市各行政區消防局的互動選單，選擇所需要的行政區可以看出此區有多少數量的消防局(多選)。  
地圖上標記的消防局點位資料有地址和行政區，資料則為選擇的行政區資料表(表單未選擇行政區則顯示全部行政區消防局資料)。
"""
st.markdown(markdown)


polygon = 'https://github.com/liuchia515/gisappreport/raw/refs/heads/main/data/%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E7%95%8C/%E9%84%89(%E9%8E%AE%E3%80%81%E5%B8%82%E3%80%81%E5%8D%80)%E7%95%8C%E7%B7%9A(TWD97%E7%B6%93%E7%B7%AF%E5%BA%A6)1131028/TOWN_MOI_1131028.shp'
taiwan = gpd.read_file(polygon)
tainan = taiwan[taiwan['COUNTYNAME'] == '臺南市']

firestation_point_csv = 'https://raw.githubusercontent.com/tim9810/gis_final_exam/refs/heads/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv'
firestation_point = pd.read_csv(firestation_point_csv)

option_list = firestation_point["行政區"].unique().tolist()
option = st.multiselect("選擇行政區", option_list)
# 篩選資料
if option:
    filtered = firestation_point[firestation_point["行政區"].isin(option)]
else:
    filtered = firestation_point

# 創建兩個區域，左邊放地圖，右邊放表格
col1, col2 = st.columns([3, 2])  # 調整比例，左邊地圖 3，右邊表格 2

with col1:
    st.subheader("地圖")
    m = leafmap.Map(center=[23.1, 120.3], zoom=10)
    m.add_points_from_xy(
        filtered, x='經度', y='緯度',
        popup=['地址', '行政區'],
        layer_name="消防局點位",
    )
    m.to_streamlit(height=500)

with col2:
    st.subheader("資料")
    if option:
        st.markdown("### 選取的行政區消防局資料")
        st.dataframe(filtered)
    else:
        st.markdown("### 所有行政區消防局資料")
        st.dataframe(firestation_point)
