import streamlit as st
st.set_page_config(page_title='food')        
st.header("My Favourite Food")     
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Fried Rice")  
  st.image(image="https://yellowchilis.com/wp-content/uploads/2020/12/indian-vegetable-egg-masala-fried-rice-500x375.jpg", caption="Fried Rice", width=300, use_column_width=True, )
with col2:
  st.subheader("Chicken")
  st.image(image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Tandoori_chicken_laccha_piyaz1_%2836886283595%29.jpg/1200px-Tandoori_chicken_laccha_piyaz1_%2836886283595%29.jpg", caption="Chicken", width=300, use_column_width=True, )
with col3:
  st.subheader("Noodles")
  st.image(image="https://imgmedia.lbb.in/media/2018/07/5b4db705f7dd8e7a514d1b87_1531819781327.jpg", caption="Chicken", width=300, use_column_width=True, )

st.header("My Favourite Places") 
co1,co2,co3=st.columns(3)
with co1:
  st.subheader("Vijayawada")  
  st.image(image="https://i.ytimg.com/vi/mzLOJf2RdyA/sddefault.jpg", caption="Vijayawada", width=300, use_column_width=True, )
with co2:
  st.subheader("Vizag")
  st.image(image="https://i.ytimg.com/vi/eb37MOTOtuY/hqdefault.jpg", caption="vizag", width=300, use_column_width=True, )
with co2:
  st.subheader("Araku")
  st.image(image="https://www.inditales.com/wp-content/uploads/2023/09/araku-view-point-clouds-passing.jpg", caption="araku", width=300, use_column_width=True, )

