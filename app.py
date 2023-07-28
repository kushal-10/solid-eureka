# Application file for Gradio App

import gradio as gr
import time
import random
from hay.pipeline import rs_pipeline

with gr.Blocks() as chat:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def respond(message, chat_history):
        question = str(message)
        answer = rs_pipeline(question)
        bot_message = answer
        chat_history.append((message, bot_message))
        time.sleep(2)
        return " ", chat_history
    
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

def application():
    chat.launch()

