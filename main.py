import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
# Authenticate to Firestore with the JSON account key.

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit_project_1")

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