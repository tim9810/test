import streamlit as st
import leafmap.foliumap as leafmap

# 側邊欄的資訊
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Interactive Map with GeoJSON")

# GeoJSON 資料連結 (從你的 GitHub 儲存庫提供)
geojson_url = "https://github.com/tim9810/data2/blob/main/Export_Output.geojson"

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

    # 加載 GeoJSON 資料
    m.add_geojson(
        geojson_url,
        layer_name="Taiwan Population",
        style={
            "fillColor": "#FF8F59",
            "color": "black",
            "weight": 0.5,
            "dashArray": "5, 5",
            "fillOpacity": 0.6,
        },
    )

    # 在 Streamlit 中顯示地圖
    m.to_streamlit(height=700)
