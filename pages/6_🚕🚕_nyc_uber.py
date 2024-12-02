import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("衛星影像分割展示")
st.sidebar.info(
    """
    - 分析兩個衛星影像，進行分割展示
    - 檔案來源: GitHub 儲存庫
    """
)

st.title("Split-panel Map for Satellite Imagery")

# 衛星影像文件 URL
url1 = "https://raw.githubusercontent.com/tim9810/data2/main/LC09_117043_20230826.tif"
url2 = "https://raw.githubusercontent.com/tim9810/data2/main/LC09_117043_20230911.tif"

st.sidebar.info(
    f"""
    左圖: {url1.split('/')[-1]}  
    右圖: {url2.split('/')[-1]}
    """
)

# 創建地圖對象
m = leafmap.Map()
m.split_map(left_layer=url1, right_layer=url2)

# 顯示地圖
m.to_streamlit(height=700)



