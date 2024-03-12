# Create a program that is responsible of calculating the aspect ratio of an
# image from an url.
# - Example url:
#   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# - By ratio we refer, for example, to the "16:9" of a 1920*1080px image.

import requests  # Make HTTP request.
from PIL import Image  # Manage images.
from io import BytesIO  # Handle bytes.

def calc_aspect_ratio(url_image):
    try:
        response = requests.get(url_image)

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))  # Create or download the image.
            width, height = image.size  # Get image resolution.
            
            width_ar, height_ar = simplify_fraction(width, height)
            print(f"Aspect ratio: {width_ar}:{height_ar}")
        else:
            print("Error to calculating the aspect ratio.")
    except Exception as error:
        print(f"Error: {error}")

def simplify_fraction(numerator, denomitator):
    number = 2

    while number <= 7:
        if (numerator % number == 0) and (denomitator % number == 0):
            numerator /= number
            denomitator /= number
        else:
            number += 1
    
    return int(numerator), int(denomitator)


calc_aspect_ratio("https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?cs=srgb&dl=pexels-pixabay-36717.jpg&fm=jpg")
