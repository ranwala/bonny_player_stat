import streamlit as st
from backend import get_player_statistics
from image_to_base64_converter import convert_image_to_base64

image_base64 = convert_image_to_base64()

st.set_page_config(layout='wide')

left_co, cent_co, right_co = st.columns([1, 2, 1])
with cent_co:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    "<h1 style='text-align: center;'>Player Statistics</h1>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col2:
    option_team = st.selectbox("Select the team", ("All", "Bonn CC Blue", "Bonn CC Yellow"))

with col3:
    option_stat = st.selectbox("Select Statistics", ("Player Ranking", "Batting Records", "Bowling Records"))

try:
    result_dataframe = get_player_statistics(option_team, option_stat)

    if not result_dataframe.empty:
        df_reset = result_dataframe.reset_index(drop=True)
        df_reset.index = df_reset.index + 1
        st.dataframe(df_reset, use_container_width=True)

except ValueError:
    st.error("Please contact Chandu...")
except Exception as e:
    st.error(f"{e} Please Contact Chandu")

