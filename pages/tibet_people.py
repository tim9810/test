import streamlit as st
import leafmap.foliumap as leafmap
import rasterio
import numpy as np
import folium
from streamlit_folium import st_folium

st.title("選擇不同的 GeoTIFF 影像進行顯示")

# **四個獨立的 GeoTIFF 檔案路徑**
tif_files = {
    "地震模型 1": "data/model_1.tif",
    "地震模型 2": "data/model_2.tif",
    "地震模型 3": "data/model_3.tif",
    "地震模型 4": "data/model_4.tif",
}

# **選擇要顯示的 TIF 影像**
selected_tif = st.selectbox("選擇要顯示的影像", list(tif_files.keys()))

# **讀取 TIF 影像**
def read_tif(file_path):
    with rasterio.open(file_path) as src:
        image = src.read(1)  # 讀取第一個 band
        transform = src.transform  # 取得座標轉換資訊
        bounds = src.bounds  # 取得影像範圍
    return image, transform, bounds

# **根據選擇的影像讀取對應的 GeoTIFF 檔案**
tif_path = tif_files[selected_tif]  # 取得選擇的檔案路徑
image, transform, bounds = read_tif(tif_path)  # 讀取影像

# **建立 Leafmap 地圖**
m = leafmap.Map(
    center=[(bounds.top + bounds.bottom) / 2, (bounds.left + bounds.right) / 2], 
    zoom=9
)
m.add_raster(tif_path, colormap="viridis", opacity=0.7)  # 可改 "viridis", "jet", "plasma" 等顏色條

# **顯示互動式地圖**
st_folium(m, width=700, height=500)

