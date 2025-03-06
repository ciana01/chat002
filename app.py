{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "add5b9a6-8926-483b-b6d5-0ded39f1308a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports\n",
    "\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "from openai import OpenAI\n",
    "import gradio as gr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c808f8a6-2bb9-4703-8317-cfd04d979f30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OpenAI API Key exists and begins sk-yCyNd\n",
      "Anthropic API Key not set\n",
      "Google API Key not set\n"
     ]
    }
   ],
   "source": [
    "# Load environment variables in a file called .env\n",
    "# Print the key prefixes to help with any debugging\n",
    "\n",
    "load_dotenv(override=True)\n",
    "openai_api_key = os.getenv('OPENAI_API_KEY')\n",
    "anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')\n",
    "google_api_key = os.getenv('GOOGLE_API_KEY')\n",
    "\n",
    "if openai_api_key:\n",
    "    print(f\"OpenAI API Key exists and begins {openai_api_key[:8]}\")\n",
    "else:\n",
    "    print(\"OpenAI API Key not set\")\n",
    "    \n",
    "if anthropic_api_key:\n",
    "    print(f\"Anthropic API Key exists and begins {anthropic_api_key[:7]}\")\n",
    "else:\n",
    "    print(\"Anthropic API Key not set\")\n",
    "\n",
    "if google_api_key:\n",
    "    print(f\"Google API Key exists and begins {google_api_key[:8]}\")\n",
    "else:\n",
    "    print(\"Google API Key not set\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5542de79-77ad-45aa-91b6-21efb2764ca5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize\n",
    "\n",
    "openai = OpenAI()\n",
    "MODEL = 'gpt-4o-mini'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "71d01450-9a78-4b75-88c3-710588e90a80",
   "metadata": {},
   "outputs": [],
   "source": [
    "system_message = \"You are a helpful assistant\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4ed41b0b-01cd-4455-9b41-70219516329d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# This function looks rather simpler than the one from my video, because we're taking advantage of the latest Gradio updates\n",
    "\n",
    "def chat(message, history):\n",
    "    messages = [{\"role\": \"system\", \"content\": system_message}] + history + [{\"role\": \"user\", \"content\": message}]\n",
    "    response = openai.chat.completions.create(model=MODEL, messages=messages)\n",
    "    return response.choices[0].message.content\n",
    "\n",
    "gr.ChatInterface(fn=chat, type=\"messages\").launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6998f4e4-74eb-4900-b0f1-0e0b8bbce224",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
