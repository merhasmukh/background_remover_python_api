import onnxruntime

# Load the U2NET ONNX model
model_path = './model/u2net.onnx'
ort_session = onnxruntime.InferenceSession(model_path)

from PIL import Image
import numpy as np

def remove_bg_u2net(image_path,output_path):
    # Load the input image
    
    input_image = Image.open(image_path)

    # Define the desired input size of the model
    input_size = (320, 320)

    # Preprocess the input image
    input_image = input_image.resize(input_size)
    input_image = np.array(input_image).astype(np.float32) / 255.0
    input_image = np.transpose(input_image, (2, 0, 1))  # Change channel order (HWC to CHW)
    input_image = np.expand_dims(input_image, axis=0)  # Add batch dimension

