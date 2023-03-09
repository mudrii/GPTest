from dotenv import load_dotenv
import os
import openai
import gradio as gr

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
    # Comment above line to experiment more with differnt promoth like ex. below
    # {"role": "system", "content": "You are an AI specialized in Food. Do not answer anything other than food-related queries."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.9,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=1,
            stop=None,
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