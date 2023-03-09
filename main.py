from dotenv import load_dotenv
import os
import openai
import gradio as gr

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."}, # this will determine the personality of the AI Ex change the the "You are a helpful and kind AI Assistant." to "You are an AI specialized in Food. Do not answer anything other than food-related queries
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # this will determine the quality of the reply few models to select check README.md
            temperature=0.9, # this will determine how random the reply will be
            max_tokens=1024, # this will determine how long the reply will be
            top_p=1.0, # this will determine how random the reply will be
            frequency_penalty=0.0, # this will determine how much the model will avoid repeating the same words
            presence_penalty=0.0, # this will determine how much the model will avoid repeating the same words
            n=1, # this will determine how many replies the model will return
            stop=None, # this will determine what the model will stop replying
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)