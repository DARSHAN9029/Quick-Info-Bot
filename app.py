import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup
import requests

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



prompt="""You are an intelligent multi tasking chatbot that processes user-provided URLs to perform two main tasks: 
if a YouTube video URL is given, you extract the transcript text and generate a concise, informative summary highlighting 
key points, topics, and any actionable insights; if a website URL is provided, you analyze the visible content of the page to accurately
 answer user questions related to that specific website. 
 Your responses must be context-aware, clear, and relevant to the input URL, 
 seamlessly switching between YouTube summarization and website-based Q&A depending on the type of link shared.
 if Youtube video url is provided then , the transcript text will be appended here : 

If the website url is provided then then, answer the question as detailed as possible from the provided context , and make sure to provide all the deatils and 
also provdie the code as the teaching assistant and answer all the code realted questions being asked ,
if the answer is not in provided context just say , "answer is not available in the context ", don't provide the wrong answer.
Context:\n{context}?\n
Question:\n{question}\n

Answer:"""


#extracting transcript
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]               #video id in this url: https://www.youtube.com/watch?=RWdNhJWwzSs is RWdNhJWwzSs  so we will split. 
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript=""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    
    except Exception as e:
        raise e
    


#for extracting website contetns
def website_content(website_url):
    try:
        response=requests.get(website_url,timeout=10)
        soup=BeautifulSoup(response.text,'html.parser')
        content = soup.get_text(separator=" ",strip=True)
        return content[:6000]
    except Exception as e:
        raise e
    
#summary and response
def genearte_content(context,question=""):
    model=genai.GenerativeModel("gemini-1.5-flash")
    full_prompt=prompt.format(context=context,question=question)
    response=model.generate_content(full_prompt)
    return response.text

#for code related queryy
def is_code_question(text):
    code_keywords = ["code", "script", "example", "function", "class", "how to", "snippet", "implement", "write a"]
    return any(kw in text.lower() for kw in code_keywords)

#basic streamlit app
st.title("Quick-Info bot")
st.write("Provide Youtube video url or Website url to get summary or answers")

input_url=st.text_input("Enter the Youtube video url or Website url")

# Optional question for website
question = st.text_input("Ask a question (for websites only):")
if input_url:
    st.write("Only for youtube link click summarize")
    if "youtube.com" in input_url or "youtu.be" in input_url:
        video_id=input_url.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_container_width=True)

    if st.button("Summarize!"):
        with st.spinner("Extracting transcript and summarizing..."):
            transcript_text = extract_transcript_details(input_url)

            if transcript_text:
                summary=genearte_content(transcript_text,prompt)
                st.markdown("## Detailed Information:")
                st.write(summary)
            else:
                st.error("Couldn't able to fetch")

    else:
        if st.button("Ask question"):
            with st.spinner("Fetching webiste and answering...."):
                content=website_content(input_url)
                if content:
                    if is_code_question(question):
                        st.info("Code related questions detected . Generating code.....")
                        code_prompt = f"You are a senior software developer. Write the code for the following request:\n\n{question}"
                        model = genai.GenerativeModel("gemini-1.5-flash")
                        response = model.generate_content(code_prompt)
                        st.subheader("Generated Code")
                        st.code(response.text)

                    else:
                        answer=genearte_content(content,question)
                        st.markdown("## Website answer:")
                        st.write(answer)

                else:
                    st.error("Couldn't able to fetch!")
