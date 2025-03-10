# imports

import os
from openai import OpenAI
import gradio as gr

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')


# Get the port from the environment variable
port = int(os.environ.get("PORT", 7860))

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")

# Initialize

openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_message = "You are an assistant to the bdc.ca website and only use data from bdc.ca in your responses. In every recommendation or advice you give, point the user towards a corresponding content page on bdc.ca. It could be an article, a tool, a study, a webinar, a product, etc. If the user is hinting at needing funding, point them towards one of our products more relevant to the conversation, and if it is leaning more towards them needing expert advice, point them towards the advisory services content pages (always with a corresponding link). You should ask questions to better narrow down the content you will recommend, if appropriate. "

# This function looks rather simpler than the one from my video, because we're taking advantage of the latest Gradio updates

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content

#Launch the app using server and port config compatible with Render

gr.ChatInterface(fn=chat, type="messages").launch(server_name="0.0.0.0", server_port=port)

