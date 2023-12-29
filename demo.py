import streamlit as st
st.set_page_config(page_title='food')        
st.header("My Favourite Food")     
col1,col2=st.columns(2)
with col1:
  st.subheader("Fried Rice")  
  st.image(image="https://yellowchilis.com/wp-content/uploads/2020/12/indian-vegetable-egg-masala-fried-rice-500x375.jpg", caption="Fried Rice", width=300, use_column_width=True, )
with col2:
  st.subheader("Chicken")
  st.image(image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Tandoori_chicken_laccha_piyaz1_%2836886283595%29.jpg/1200px-Tandoori_chicken_laccha_piyaz1_%2836886283595%29.jpg", caption="Chicken", width=300, use_column_width=True, )

