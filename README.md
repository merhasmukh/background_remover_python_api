## Background Removal API Using AI/ML 

- Here i am creating a FastAPI for removes the Background of an Images usinf Python And AI/ML libraries
    which accepts images with .jpg and .png extension.

### Steps That I follow to develope this task.

- There is a one python library or we can say a project that can help us to remove background of an image files
- https://github.com/danielgatis/rembg

- It is use

### Download the model
- https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx


### How to run the code

1. Create a python virtual environment : 
- - python3 -m venv venv

2. install all the required libraries using requirements.txt
- - pip install -r requirements.txt

3. run the API
- - python3 app.py

4. open url in the browser
- - http://127.0.0.1:8000/docs

5. upload the image (.jpg, .jpeg , .png)

6. we get the output image as .png 




## For the demo pupose i create a Streamlit App

### How to run the app

- go to the path where streamlit_app_demo.py is located and run the below command
- streamlit run streamlit_app_demo.py


