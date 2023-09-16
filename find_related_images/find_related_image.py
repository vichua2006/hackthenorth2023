from serpapi import GoogleSearch 
import json
import requests

# api key for: https://serpapi.com/
API_KEY = "9d7067c59ad8799a799ddada89d845948a87c6391e08799854285cc6c2458726"

params = {
  "engine": "google_images",
  "q": "Coffee",
  "api_key": API_KEY
}

# get search results
search = GoogleSearch(params)
results = search.get_dict()

images = results["images_results"]

img_data = requests.get(images[0]["original"]).content

with open(r".\find_related_images\images\test_image.jpg", "wb") as file:
    file.write(img_data)

print(images[0]["original"])