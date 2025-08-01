# Home
import streamlit as st
from PIL import Image
from backend import get_player_statistics
from image_to_base64_converter import convert_image_to_base64

icon = Image.open("images/logo.png")

st.set_page_config(
    page_title="Bonn Cricket Club",
    page_icon=icon,
    layout='wide',
)

image_base64 = convert_image_to_base64()

left_co, cent_co, right_co = st.columns([1, 2, 1])
with cent_co:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" width="120">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<h1 style='text-align: center;'>Player Statistics</h1>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    option_team = st.selectbox("Select the team", ("All", "Bonn CC Blue", "Bonn CC Yellow"))

with col2:
    option_stat = st.selectbox("Select Statistics", ("Player Ranking", "Batting Records", "Bowling Records"))

with col3:
    option_flavor = st.selectbox('Select match type', ('T20', 'ODI'))

try:
    result_dataframe = get_player_statistics(option_team, option_stat, option_flavor)

    # Adjust height based on number of rows
    # Assume approx 35px per row (tweak as needed)
    row_height = 35
    max_rows_displayed = 20  # Cap height if too large

    num_rows = len(result_dataframe)
    visible_rows = min(num_rows, max_rows_displayed)
    height = row_height * visible_rows + 35  # Add padding for header

    if not result_dataframe.empty:
        df_reset = result_dataframe.reset_index(drop=True)
        df_reset.index = df_reset.index + 1
        st.dataframe(df_reset, use_container_width=True, height=height)

    else:
        st.markdown(
            "<h3 style='text-align: center;'>No records to display, please try another filter</h3>",
            unsafe_allow_html=True
        )

except ValueError:
    st.error("Please contact Chandu...")
except Exception as e:
    st.error(f"{e} Please Contact Chandu")

