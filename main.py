import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("fire_store_key.json")

title = st.text_input("post title")
content = st.text_input("content")
submit = st.button("submit new post")

if title and content and submit:
    doc_ref = db.collection("post").document(title)
    doc_ref.set({
        "title": title,
        "content": content
    })

post_ref = db.collection("post")

for doc in post_ref.stream():
    post = doc.to_dict()
    title = post["title"]
    content = post["content"]

    st.subheader(f"post: {title}")
    st.write(f"content: {content}")