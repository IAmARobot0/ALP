import gradio as gr
from huggingface_hub.inference_api import InferenceApi
import openai

openai.api_key = "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"

def nothingimg(imgresults):
  for k in range(5):
    imgresults.append("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")
  return imgresults

def appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults):
  imgresults.append(image_url)
  imgresults.append(image_url1)
  imgresults.append(image_url2)
  imgresults.append(image_url3)
  imgresults.append(image_url4)
  imgresults.append(image_url5)
  return imgresults
  

def dosomething(action, gen_text_input, gen_checkboxes, gen_length, sum_text_input, sum_checkboxes, sum_length, image_input, number_of_photos, size):

  genresults = []
  if "text gen" in action: #text gen
    if "mild" in gen_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=gen_text_input, max_tokens=gen_length, temperature=0, frequency_penalty=0, presence_penalty=0)
      answer = gen_text_input + (response.choices[0]['text'].strip('\"'))
      genresults.append(answer)
    else:
      genresults.append("Not selected")
    if "medium" in gen_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=gen_text_input, max_tokens=gen_length, temperature=0.5, frequency_penalty=0.5, presence_penalty=0.5)
      answer = gen_text_input + (response.choices[0]['text'].strip('\"'))
      genresults.append(answer)
    else:
      genresults.append("Not selected")
    if "spicy" in gen_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=gen_text_input, max_tokens=gen_length, temperature=0.75, frequency_penalty=0.75, presence_penalty=0.75)
      answer = gen_text_input + (response.choices[0]['text'].strip('\"'))
      genresults.append(answer)
    else:
      genresults.append("Not selected")
    if "extra hot" in gen_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=gen_text_input, max_tokens=gen_length, temperature=1, frequency_penalty=1, presence_penalty=1)
      answer = gen_text_input + (response.choices[0]['text'].strip('\"'))
      genresults.append(answer)
    else:
      genresults.append("Not selected")
    if "fiery hot" in gen_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=gen_text_input, max_tokens=gen_length, temperature=1.5, frequency_penalty=1.5, presence_penalty=1.5)
      answer = gen_text_input + (response.choices[0]['text'].strip('\"'))
      genresults.append(answer)
    else:
      genresults.append("Not selected")
  else:
    for i in range(5):
      genresults.append("Not selected")


  sumresults = []
  if "text sum" in action: #text sum
    if "mild" in sum_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + sum_text_input, max_tokens=sum_length, temperature=0, frequency_penalty=0, presence_penalty=0)
      answer = sum_text_input + (response.choices[0]['text'].strip('\"'))
      sumresults.append(answer)
    else:
      sumresults.append("Not selected")
    if "medium" in sum_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + sum_text_input, max_tokens=sum_length, temperature=0.5, frequency_penalty=0.5, presence_penalty=0.5)
      answer = sum_text_input + (response.choices[0]['text'].strip('\"'))
      sumresults.append(answer)
    else:
      sumresults.append("Not selected")
    if "spicy" in sum_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + sum_text_input, max_tokens=sum_length, temperature=0.75, frequency_penalty=0.75, presence_penalty=0.75)
      answer = sum_text_input + (response.choices[0]['text'].strip('\"'))
      sumresults.append(answer)
    else:
      sumresults.append("Not selected")
    if "extra hot" in sum_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + sum_text_input, max_tokens=sum_length, temperature=1, frequency_penalty=1, presence_penalty=1)
      answer = sum_text_input + (response.choices[0]['text'].strip('\"'))
      sumresults.append(answer)
    else:
      sumresults.append("Not selected")
    if "fiery hot" in sum_checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + sum_text_input, max_tokens=sum_length, temperature=1.5, frequency_penalty=1.5, presence_penalty=1.5)
      answer = sum_text_input + (response.choices[0]['text'].strip('\"'))
      sumresults.append(answer)
    else:
      sumresults.append("Not selected")
  else:
    for j in range(5):
      sumresults.append("Not selected")


  
  imgresults = []
  if "img gen" in action: #img gen
    if number_of_photos == 0:
      imgresults = nothingimg(imgresults)
    else:
      image = openai.Image.create(prompt=image_input, n=number_of_photos, size = size)
      if number_of_photos == 1:
        image_url = image['data'][0]['url']
        image_url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      elif number_of_photos == 2:
        image_url = image['data'][0]['url']
        image_url1 = image['data'][1]['url']
        image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      elif number_of_photos == 3:
        image_url = image['data'][0]['url']
        image_url1 = image['data'][1]['url']
        image_url2 = image['data'][2]['url']
        image_url3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      elif number_of_photos == 4:
        image_url = image['data'][0]['url']
        image_url1 = image['data'][1]['url']
        image_url2 = image['data'][2]['url']
        image_url3 = image['data'][3]['url']
        image_url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      elif number_of_photos == 5:
        image_url = image['data'][0]['url']
        image_url1 = image['data'][1]['url']
        image_url2 = image['data'][2]['url']
        image_url3 = image['data'][3]['url']
        image_url4 = image['data'][4]['url']
        image_url5 = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      elif number_of_photos == 6:
        image_url = image['data'][0]['url']
        image_url1 = image['data'][1]['url']
        image_url2 = image['data'][2]['url']
        image_url3 = image['data'][3]['url']
        image_url4 = image['data'][4]['url']
        image_url5 = image['data'][5]['url']
        appendimg(image_url, image_url1, image_url2, image_url3, image_url4, image_url5, imgresults)
      else:
        imgresults = nothingimg(imgresults)
  else:
      imgresults = nothingimg(imgresults)

  return genresults[0], genresults[1], genresults[2], genresults[3],  genresults[4], sumresults[0], sumresults[1], sumresults[2], sumresults[3], sumresults[4], imgresults #imgresults[0], imgresults[1], imgresults[2], imgresults[3], imgresults[4], imgresults[5]


demo = gr.Interface(
    fn=dosomething,
    inputs=[gr.CheckboxGroup(["text gen", "text sum", "img gen"], label="Action"), #action
            
    "text", gr.CheckboxGroup(["mild", "medium", "spicy", "extra hot", "fiery hot"], label="Generate Variety"), #text gen input and spice
    gr.Slider(0, 500, label="Text Length", step=1), #text gen length slider

    "text", gr.CheckboxGroup(["mild", "medium", "spicy", "extra hot", "fiery hot"], label="Summarize Variety"), #text sum input and spice
    gr.Slider(0, 500, label="Text Length", step=1), #text sum length slider

    "text", gr.Slider(0, 6, label="number of photos", step=1), #img gen
    gr.Radio(["256x256", "512x512", "1024x1024"], label="Image size"),], #img gen
    
    
    outputs=["text", "text", "text", "text", "text",#text gen
             "text", "text", "text", "text", "text", #text sum
            gr.Gallery(label="Generated images").style(columns=[2], rows=[3],object_fit="contain", height="auto")
            ]) #img gen
demo.launch()
