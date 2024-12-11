import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://raw.github.com/tim9810/gis_final_exam/blob/main/%E5%8F%B0%E5%8D%97%E6%B6%88%E9%98%B2%E5%B1%80wgs84%E5%BA%A7%E6%A8%99utf.csv"
        regions = "https://raw.github.com/tim9810/gis_final_exam/blob/main/tainung/tainung.geojson"

        m.add_geojson(regions, layer_name="tw Regions")
        m.add_points_from_xy(
            cities,
            x="经度",
            y="纬度",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
