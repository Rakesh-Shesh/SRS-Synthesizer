import streamlit as st
import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

st.title("Document Processing and Test Generation")

# First area: Document uploader
st.header("1. Upload a Document")
uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf", "docx"])

document_text = ""
if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        document_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        from PyPDF2 import PdfReader

        reader = PdfReader(uploaded_file)
        document_text = ""
        for page in range(len(reader.pages)):
            document_text += reader.pages[page].extract_text()
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        import docx
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            document_text += para.text
messages = [
            {"role": "system", "content": "You are a document synthesizer.please synthesize this document"},
            {"role": "user", "content": document_text}
        ]

option = st.sidebar.selectbox(
    "Choose an action",
    ("Generate test cases", "Generate test scenarios", "Generate test script","Business Analyst","Test Document")
)

if option == "Generate test cases":
    if document_text:
        messages = [
            {"role": "system", "content": "You are an expert level test cases generator.Provide multiple test cases in normal as well as Gherkin format"},
            {"role": "user", "content": document_text}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please upload a document first!")

if option == "Generate test scenarios":
    if document_text:
        messages = [
            {"role": "system", "content": "You are an expert level test scenario generator.Please generate both positive and negative test scenario"},
            {"role": "user", "content": document_text}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please upload a document first!")

if option == "Generate test script":
    if document_text:
        messages = [
            {"role": "system", "content": "You are an expert level test script generator"},
            {"role": "user", "content": document_text}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please upload a document first!")

if option == "Business Analyst":
    if document_text:
        messages = [
            {"role": "system", "content": "You are an expert level business analyst.Generate user stories"},
            {"role": "user", "content": document_text}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please upload a document first!")

if option == "Test Document":
    if document_text:
        messages = [
            {"role": "system", "content": "You are an expert level test document geenrator.Provide test document"},
            {"role": "user", "content": document_text}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please upload a document first!")