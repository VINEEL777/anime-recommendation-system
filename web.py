import streamlit as st
from PIL import Image
st.title ("Anime Recommendation System") 
st.write("Welcome to the Anime Recommendation System. This system will help you to find the best anime for you. Please fill the form below and click on the 'Get Recommendation' button to get the recommendation.")    
if st.checkbox('Do you have any prior experience with anime'):
    st.write('Yay you good to go🙌🪄')
    image = Image.open("download (12).jpeg")
    st.image(image, caption='Demon slayer')
    value1 = st.slider('What would  ya rate this :', 0, 100,key='slider1')
    st.write(f'Your rating : {value1}')
if st.checkbox('Show more'):
    image = Image.open("jjk.webp")
    st.image(image, caption='jjk')
    value2 = st.slider('What would  ya rate this :', 0, 100,key="slider2")
    st.write(f'Your rating: {value2}')

if st.button('Get Recommendation'):
    st.write('You would probably like')
    image = Image.open("tokyo ghoul.jpeg")
    st.image(image, caption='Tokyo Ghoul')


if st.button('do ya wanna watcha shot trailer!!! Click me👆'):
    st.video('https://www.youtube.com/watch?v=UUeqpuZobBw&pp=ygUTdG9reW8gZ2hvdWwgdHJpYWxlcg%3D%3D')


