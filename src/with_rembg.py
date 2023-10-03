import rembg
from PIL import Image
import os

def remove_background(image_path,output_path):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Remove the background 
        output = rembg.remove(image)
        fname,fextension=os.path.splitext(output_path)
        output_path=output_path.replace(fextension,".png")
        print(fextension)
        print(fname)
        print(output_path)
        # Save the output image
        output.save(output_path,format="PNG")

        return {"message":"success","file_out_path":output_path}
    except Exception as e:
        return {"error":str(e),"message":"getting error in removing backgroung using rembg"}


