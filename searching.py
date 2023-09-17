from serpapi import GoogleSearch 
import os 

# api key for: https://serpapi.com/
API_KEY = os.getenv("SERPAPI_KEY")

def search_img(description):

    params = {
      "engine": "google_images",
      "q": description,
      "api_key": API_KEY
    }

    # get search results
    search = GoogleSearch(params)
    results = search.get_dict()["images_results"]

    images = results[0]["original"]

    return images
    # potentially implement a image-caption similarity checker
