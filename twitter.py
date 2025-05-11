import streamlit as st

#Make list to store posts
if "Posts" not in st.session_state:
    st.session_state.posts = []

#App title
st.title("Simple twitter-style App")

#Text input box
post_content = st.text_input("Put your post here")

#Post button
if st.button("Post"):
    if post_content: #If post content is not empty
        st.success("Posted!")
        st.session_st.posts.append(post_content) #Save in list
    else: #If post content is empty
        st.warning("Please enter content to post") #Show alert

#Show posts
for post in st.session_state.posts:
    st.text_area("Posts", post_content)