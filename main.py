import streamlit as st
import time

app_state_begin = 0
app_state_waiting = 1
app_state_continue = 2

if "app_state" not in st.session_state:
    st.session_state.app_state = app_state_begin 

if "conversation" not in st.session_state:
    st.session_state.conversation = [] 


def change_state_waiting():
    st.session_state.app_state = app_state_waiting

def change_state_waiting():
    st.session_state.app_state = app_state_continue

def first_click(text):
    st.session_state.conversation.append({'speaker': 'User', 'content': text})
    change_state_waiting()

def reset_to_start():
    st.session_state.app_state = app_state_begin
    st.session_state.conversation = []

def draw_conversation():
    for entry in st.session_state.conversation:
        speaker = entry["speaker"]
        content = entry["content"]
        st.write(f"{speaker}: {content}")
    ai_response = ["I", "can", "say", "anything?"]
    with st.empty():
        output = "AI: "
        for word in ai_response:
            time.sleep(0.05)
            output += " " + word
            output + "|"
        output
    return output
# st.write("Conversation:")
# st.write(st.session_state.conversation)

def followup_clicks(text):
    st.session_state.conversation.append({'speaker': 'User', 'content': text})
    change_state_waiting()

if st.session_state.app_state == app_state_begin:
    input_text = st.text_area("Welcome! Care to enter some text?", "You can say what you like!")
    st.button('Submit', on_click=first_click, args=[input_text])

if st.session_state.app_state == app_state_waiting:
    ai_response = draw_conversation()
    st.session_state.conversation.append({'speaker': 'AI', 'content': ai_response})
    st.button('Wait for the response to finish...', disabled=True)
    change_state_continue()

if st.session_state.app_state == app_state_continue:
    draw_conversation()
    continued_input_text = st.text_area("Continue your conversation")
    st.button("Submit again", on_click=followup_clicks, args = [continued_input_text])

st.button('Reset', on_click = reset_to_start)
