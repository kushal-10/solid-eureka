# Application file for Gradio App

import gradio as gr
import time
from hay.pipeline import rs_pipeline

d='data'
# d='data2'

title = """<h1 align="center">Chat Literature</h1>"""
description = """<br><br><h3 align="center">This is a literature chat model, which can currently answer questions to regulation/two-sided markets topic in Supply chain mangement.</h3>"""

def user(user_message, history):
    return "", history + [[user_message, None]]

def respond(message, chat_history):
    question = str(message)
    answer = rs_pipeline(question, d)
    bot_message = answer
    chat_history.append((message, bot_message))
    time.sleep(2)
    return " ", chat_history

with gr.Blocks(theme=gr.themes.Soft(primary_hue="emerald", neutral_hue="slate")) as chat:
    gr.HTML(title)
    chatbot = gr.Chatbot().style(height=750)
    msg = gr.Textbox(label="Send a message", placeholder="Send a message",
                             show_label=False).style(container=False)
    # with gr.Row():
    #     with gr.Column():
    #         msg = gr.Textbox(label="Send a message", placeholder="Send a message",
    #                          show_label=False).style(container=False)
    #     with gr.Column():
    #         with gr.Row():
                # submit = gr.Button("Submit")
                # stop = gr.Button("Stop")
                # clear = gr.Button("Clear")


    msg.submit(respond, [msg, chatbot], [msg, chatbot])


    if d=='data':
        gr.Examples([
            ["How to reduce carbon emissions?"],
            ["What are the main topics in these papers?"],
            ["What are the major math models in PI."]
        ], inputs=msg, label= "Click on any example to copy in the chatbox"
        )
    
    else:
        gr.Examples([
            ["Who are the main users (participants) in the two-sided market?"],
            ["What are the decisions made in the two-sided market? And who makes this decision?"],
            ["What are the main effects in the two-sided market"]
        ], inputs=msg, label= "Click on any example to copy in the chatbox"
        )

    gr.HTML(description)

def application():
    return None

chat.queue()
chat.launch()

