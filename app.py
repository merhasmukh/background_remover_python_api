from fastapi import FastAPI,UploadFile, File
import uvicorn
import os 
from datetime import datetime
from src import with_rembg

app = FastAPI()

@app.get("/")
def hello():
    return {"API":"API is working fine"}

@app.post("/image_backgroung_remove")
async def upload_image(img_file:UploadFile =File(...)):
    today_date=str(datetime.now().date())
  
    current_time=str(datetime.now().strftime("%H_%M_%S"))


    #image extension validation
    if '.jpg' in img_file.filename or '.jpeg' in img_file.filename or '.png' in img_file.filename:

        #give input and output file names
        file_save_path="./images/"+today_date+"/"+current_time+"_"+img_file.filename
        file_output_path="./removed_bg/"+today_date+"/"+current_time+"_removed_bg_"+img_file.filename
        
        #check images directory exists or not, if not then create.
        if os.path.exists("./images/"+today_date+"/") == False:
            os.makedirs("./images/"+today_date+"/")

        #check removed_bg directory exists or not, if not then create.

        if os.path.exists("./removed_bg/"+today_date+"/") == False:
            os.makedirs("./removed_bg/"+today_date+"/")

        #save uploaded file into the directory
        with open(file_save_path, "wb") as f:
            f.write(img_file.file.read())

        #Check File is successfully saved and exists on the given path or not
        if os.path.exists(file_save_path):
            result=with_rembg.remove_background(file_save_path,file_output_path)
            if result == True:
                return {"image_path":file_save_path,"message": f"Image saved at {file_output_path} successfully"}
        else:
            return {"error":"Image Not saved !!!"}
    else:
        return {"error": "File Type is not valid please upload only jpg,jpeg and png"}


if __name__=="__main__":
    uvicorn.run(app)