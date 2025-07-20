import streamlit as st
import requests

st.title("rhyming words finder")

word=st.text_input("enter a word",placeholder="eg.donkey")
is_clicked=st.button("generate",type="primary")

if is_clicked:
   
    endpoint = f"https://api.datamuse.com/words?sp={word}"
    response = requests.get(endpoint)
 
    data = response.json()
  
    if response.status_code == 200:
        for item in data:
            st.write(item.get('word'))
    
    else:
        st.toast("something went wrong")































# import requests

# st.title("Rhyming word finder")

# word=st.text_input("enter a word",placeholder="eg. monkey")

# is_clicked=st.button("generate",type="primary")

# # print(is_clicked)

# # st.write(is_clicked)

 
 
# if is_clicked:
#     word = input('Enter a word:')
#     endpoint = f"https://api.datamuse.com/words?sp={word}"
 
#     response = requests.get(endpoint)
 
# data= response.json()
  
# if response.status_code == 200:
#     for item in data:
#         st.write(item.get('word'))
#     else:
#         st.toast("word connot be empty")
# else:
#     st.toast("word cannot be empty")
    
        