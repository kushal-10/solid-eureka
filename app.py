# Application file for Gradio App

import gradio as gr


def greet(name):
    return "Hello " + name + "!"

def application():
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()
