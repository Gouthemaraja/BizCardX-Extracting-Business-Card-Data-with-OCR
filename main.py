import streamlit as st
import imageio as io
import extraction as ex
import numpy as np
import cv2
import pandas as pd
import upload as up

#page cinfiguration 
st.set_page_config(
    page_title="BizcardX",
    page_icon = "VC icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)



#title
st.title("Extracting Business Card Data with OCR")

uploaded_file = st.file_uploader("",type= ['png', 'jpg'])
if uploaded_file:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    text = ex.extract_text(image)
    details = ex.details(text)
    st.image(image,width=800)
    df = pd.DataFrame(list(details.items()), columns=['Field', 'Value'])
    st.dataframe(df)

    upload = st.button("Click here to upload in database")

    if upload:
        up.creating_dim_tables()
        ret = up.upload(df)
        if ret==1:
            st.success("Uploaded")
        else:
            st.error("already uploaded")
view  = st.button("Click here to view database")
if view:
    rdf = up.retrival()
    st.table(rdf)














