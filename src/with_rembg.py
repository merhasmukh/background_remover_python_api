import rembg
from PIL import Image


def remove_background(image_path,output_path):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Remove the background 
        output = rembg.remove(image)

        # Save the output image
        output.save(output_path)

        return True
    except Exception as e:
        return {"error":str(e),"message":"getting error in removing backgroung using rembg"}


