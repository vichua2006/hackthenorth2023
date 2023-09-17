from gpt import generate_slides_from_script
from searching import search_img
import json

script = '''[Slide 1: Introduction]
Good [morning/afternoon/evening], ladies and gentlemen. Today, we embark on a culinary journey that challenges conventional wisdom. We are going to explore the topic of whether hotdogs can be considered sandwiches. This may seem like a lighthearted debate, but it delves into the very essence of what defines a sandwich. Let's begin.

[Slide 2: The Anatomy of a Sandwich]
Before we delve into hotdogs, let's briefly examine the structural and content elements that define a sandwich:

A sandwich typically consists   of two or more slices of bread.
It contains a filling, which can include various ingredients like meat, vegetables, cheese, or condiments.
The bread serves as both a container and a means of holding the filling together.
[Slide 3: Deconstructing a Hotdog]
Now, let's deconstruct a hotdog to see how it aligns with these structural and content elements:

A hotdog consists of a single piece of bread, often a roll or bun.
It contains a filling, usually a cooked sausage, which is a form of meat.
The bread serves as both a container and a means of holding the sausage and additional toppings together.
[Slide 4: The Case for Hotdogs as Sandwiches - Structural]
So, here's where the debate begins. Consider the structural elements:

Hotdogs use bread just like traditional sandwiches.
The bread still functions as both a container and a vessel for the filling.
It's just that the bread in hotdogs is typically shaped differently, but it still fulfills the essential role of holding everything together.
[Slide 5: The Case for Hotdogs as Sandwiches - Content]
Now, let's look at the content:

Hotdogs contain meat, which is a key ingredient in many sandwiches.
They can also have various toppings like onions, sauerkraut, pickles, and condiments, similar to what you'd find in a sandwich.
In essence, hotdogs possess the same diversity of ingredients that you'd encounter in a traditional sandwich.
[Slide 6: Historical Perspective]
To further support our argument, it's interesting to note that hotdogs have a historical connection to sandwiches. The concept of placing sausages within rolls or bread goes back centuries. It's a sandwich evolution, if you will.

[Slide 7: The Counterarguments]
Of course, no debate is complete without considering counterarguments. Some may argue that hotdogs don't qualify as sandwiches because they use a single piece of bread. However, it's worth noting that other sandwiches like open-faced sandwiches also use only one slice of bread.

[Slide 8: Conclusion]
In conclusion, the structural and content elements of hotdogs align remarkably well with those of sandwiches. While the debate over whether hotdogs are sandwiches may never truly be resolved, it's evident that the boundaries of the sandwich world are more flexible than we might think. Whether you personally choose to classify hotdogs as sandwiches or not, one thing is clear: hotdogs are a beloved and iconic part of culinary culture that deserve recognition and respect.

[Slide 9: Thank You]
Thank you for joining us on this thought-provoking journey into the world of hotdogs and sandwiches. We encourage you to keep an open mind and embrace the rich diversity of culinary creations that continue to inspire and challenge our perceptions. If you have any questions or comments, please feel free to share them now.'''

# print(json.dumps(generate_slides_from_script(script=script), 2))

print(search_img("coffee"))