import streamlit as st
import leafmap.foliumap as leafmap

st.title("Interactive Map with GeoTIFF")

# 檢查必要模組是否已安裝
try:
    import xarray
    import rioxarray
except ImportError as e:
    st.error(f"缺少必要模組: {e}. 請運行以下命令來安裝依賴: pip install xarray rioxarray rasterio")
    st.stop()

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
    try:
        m.add_raster(
            tif_url,
            layer_name="GeoTIFF Layer",
            opacity=0.7,
        )
        m.to_streamlit(height=700)
    except Exception as e:
        st.error(f"無法加載 GeoTIFF 檔案: {e}")


