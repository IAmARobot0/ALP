import gradio as gr
from huggingface_hub.inference_api import InferenceApi
import os

inference = InferenceApi(repo_id="gpt2-large", token="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")


def greet(input_string, max_length):
    
    topP = {"max_length": max_length, "top_p":0.5, "do_sample": True}
    result = inference(input_string, topP)
    greeting1 = f"{input_string}, {result}"

    topK = {"max_length": max_length, "top_p": 1.5, "do_sample": True}
    result2 = inference(input_string, topK)
    greeting2 = f"{input_string}, {result2}"

    ConS = {'max_length': max_length, 'top_p': 4, 'do_sample': True}
    result3 = inference(input_string, topK)
    greeting3 = f"{input_string}, {result3}"

    return greeting1, greeting2, greeting3


demo = gr.Interface(
    fn=greet,
    inputs=["text", gr.Slider(0, 200)],
    outputs=["text", "text", "text"],
)
demo.launch()