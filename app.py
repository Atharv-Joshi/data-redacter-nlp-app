import streamlit as st
import os


# NLP PKG

import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")


def sanitize_names(text):
    docx = nlp(text)
    redacted_sentences = []
    #for ent in docx.ents:
    #    ent.merge()
    for token in docx:
        if token.ent_type == 'PERSON':
            redacted_sentences.append("[REDACTED NAME]")
        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences)







def main():

    st.title("Document Redaction App")
    
    st.text("-Built with streamlit and spacy")

    activities = ["Redaction" , "Download" , "About"]

    choice = st.sidebar.selectbox("Select task" , activities)

    if choice == "Redaction" :
        st.subheader("Redaction of Task")
        rawtext = st.text_area("Enter Text")
        redaction_item = ['names' , 'places' , 'org' , 'dates']
        redaction_choice  = st.selectbox('Select Term to Censor' , redaction_item)
        save_option = st.radio("Save To File" , ('Yes' , 'No'))
        if st.button('Submit'):
            st.write(sanitize_names(rawtext))

    elif choice == "Download":
        st.subheader("Download List")
    elif choice == "About":
        st.subheader("About")        




if __name__ == "__main__":
    main()    