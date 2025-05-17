from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import logging
from deepgram.utils import verboselogs
from deepgram import (
    DeepgramClient,
    SpeakOptions,
)
import simpleaudio as sa

load_dotenv()
deepgram_key = os.getenv('DEEPGRAM_KEY')
gemini_key = os.getenv('GEMINI_KEY')

prompt = """
You are a grammar analyzing expert that specializes in detecting, explaining, and fixing English grammatical errors.
From the input given in the shape of a English text, I want you to answer the following questions:
- State the sentence again.
- Identify the grammatical errors from the text.
- Give thorough explanations as to why they are grammatically incorrect (with bulleted format).
- Answer with the revised version of the text with the correct grammar.
Answer those questions with a detailed manner and in a sentence-like structure.
"""

client = genai.Client(api_key=gemini_key)

sentence = input("Input your English sentence here: ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=sentence,
    config=types.GenerateContentConfig(
        system_instruction=prompt
    )
)

result = response.text.replace("*", "")

print(result)

SPEAK_TEXT = {"text": result}
filename = "answer.mp3"

try:
    deepgram = DeepgramClient(deepgram_key)
    options = SpeakOptions(
        model="aura-2-thalia-en",
    )
    response = deepgram.speak.rest.v("1").save(filename, SPEAK_TEXT, options)
    print(response.to_json(indent=4))
except Exception as e:
    print(f"Exception: {e}")

wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()

