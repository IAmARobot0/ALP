import gradio as gr
from huggingface_hub.inference_api import InferenceApi
import openai

openai.api_key = "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"

def nothingimg(imgresults):
  for j in range(6):
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
  

def dosomething(action, text_input, checkboxes, length, image_input, number_of_photos, size):

  results = []
  if "text gen" in action: #text gen
    if "mild" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=text_input, max_tokens=length, temperature=0, frequency_penalty=0, presence_penalty=0)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "medium" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=text_input, max_tokens=length, temperature=0.5, frequency_penalty=0.5, presence_penalty=0.5)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "spicy" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=text_input, max_tokens=length, temperature=0.75, frequency_penalty=0.75, presence_penalty=0.75)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "extra hot" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=text_input, max_tokens=length, temperature=1, frequency_penalty=1, presence_penalty=1)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "fiery hot" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt=text_input, max_tokens=length, temperature=1.5, frequency_penalty=1.5, presence_penalty=1.5)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")



  elif "text sum" in action: #text sum
    if "mild" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + text_input, max_tokens=length, temperature=0, frequency_penalty=0, presence_penalty=0)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "medium" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + text_input, max_tokens=length, temperature=0.5, frequency_penalty=0.5, presence_penalty=0.5)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "spicy" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + text_input, max_tokens=length, temperature=0.75, frequency_penalty=0.75, presence_penalty=0.75)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "extra hot" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + text_input, max_tokens=length, temperature=1, frequency_penalty=1, presence_penalty=1)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
    if "fiery hot" in checkboxes:
      response = openai.Completion.create(model="text-davinci-003", prompt="Summarize the following in half the number of sentences:" + text_input, max_tokens=length, temperature=1.5, frequency_penalty=1.5, presence_penalty=1.5)
      answer = text_input + (response.choices[0]['text'].strip('\"'))
      results.append(answer)
    else:
      results.append("Not selected")
  else:
    for i in range(5):
      results.append("Not selected")


  
  imgresults = []
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

  return results[0], results[1], results[2], results[3],  results[4], imgresults[0], imgresults[1], imgresults[2], imgresults[3], imgresults[4], imgresults[5]


demo = gr.Interface(
    fn=dosomething,
    inputs=[gr.Radio(["text gen", "text sum"], label="Action"), #action
            
    "text", gr.CheckboxGroup(["mild", "medium", "spicy", "extra hot", "fiery hot"], label=" Variety"), #text gen input and spice
    gr.Slider(0, 500, label="Length", step=1), #text gen length slider

    "text", gr.Slider(0, 6, label="Number of Images", step=1), #img gen
    gr.Radio(["256x256", "512x512", "1024x1024"], label="Image size"),], #img gen
    
    
    outputs=["text", "text", "text", "text", "text",#text output
             "image", "image", "image", "image", "image","image"]) #img output
demo.launch()
