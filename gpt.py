import os
import openai
from searching import search_img

openai.api_key = os.getenv("OPENAI_KEY")

def generate_response(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )

    return response

def generate_slides_from_script(script):
    points_resp = generate_response("summarize each slide section in 2 or 3 short bullet points (no more than 7 words per point, do not repeat information, do not use colons): " + script)
    image_descriptions_resp = generate_response("generate a suitable image description for each slide section (in less than 8 words): " + script)
    # image_descriptions_resp = generate_response("generate an one word image description for each slide section:" + script)
    
    points_list = points_resp["choices"][0]["message"]["content"].split('\n')
    image_descriptions_list = image_descriptions_resp["choices"][0]["message"]["content"].split('\n')


    points = []
    image_descriptions = []
    img_links = []

    for point in points_list:
        if "Slide " in point and ":" in point:
            points.append({"title": point.split(":")[1], "points": []})
        else:
            print(points, "RN")
            points[-1]["points"].append(point)

    for point in image_descriptions_list:
        if "Slide " in point and ":" in point:
            image_descriptions.append({"title": point.split(":")[1], "points": []})
        else:
            image_descriptions[-1]["points"].append(point)

    for pair in image_descriptions:
        desc = pair["title"]
        img_links.append(search_img(desc))

        
    slides = points
    return slides, img_links

    
