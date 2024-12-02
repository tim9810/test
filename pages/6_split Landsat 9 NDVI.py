import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Landsat 9 NDVI分割展示")
st.sidebar.info(
    """
    - Landsat 9 NDVI影像，進行分割展示
    - 檔案來源: GEE檔案放入GitHub 
    """
)

st.title("Landsat 9 NDVI分割展示 以半個台灣為例")

# 衛星影像文件 URL
url1 = "https://raw.githubusercontent.com/tim9810/data2/main/LC09_117043_20230826.tif"
url2 = "https://raw.githubusercontent.com/tim9810/data2/main/LC09_117043_20230911.tif"

st.sidebar.info(
    f"""
    左圖: {url1.split('/')[-1]}  
    右圖: {url2.split('/')[-1]}
    """
)
# 添加 NDVI 數值的顏色範圍圖例
m.add_colorbar(
    title="NDVI",
    colors=["blue", "white", "green"],  # 設定顏色範圍
    vmin=-1,  # 最小值
    vmax=1,   # 最大值
)

# 創建地圖對象
m = leafmap.Map()
m.split_map(left_layer=url1, right_layer=url2)

# 顯示地圖
m.to_streamlit(height=700)



