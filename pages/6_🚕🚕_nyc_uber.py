import streamlit as st
import leafmap.foliumap as leafmap

st.title("Interactive Map with GeoTIFF")

# GeoTIFF 檔案路徑或網址
tif_url = "https://github.com/tim9810/data2/blob/main/LC09_117042_20230114.tif"

# 設定互動式地圖
col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:
    # 讓使用者選擇底圖
    basemap = st.selectbox("Select a basemap:", options, index)

with col1:
    # 創建地圖
    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)

    # 加載 GeoTIFF 檔案
    m.add_cog_layer(
        tif_url,
        name="GeoTIFF Layer",
        opacity=0.7,
        fit_bounds=True,
    )

    # 在 Streamlit 中顯示地圖
    m.to_streamlit(height=700)

