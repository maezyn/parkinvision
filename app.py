import os
import requests
from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from process_image import process_image
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["IMAGE_UPLOADS"] = "./static/img"

@app.route("/", methods=["GET", "POST"])
def upload_image():
   if request.method == "POST":
      if request.files:
         image = request.files["image"]

         image_url = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)

         image.save(image_url)

         print("Image saved")

         result = process_image(image_url)

         print(result)

         image_path = "static/img/" + image.filename
         return render_template("result.html", result=result, image_path=image_path)
   
   return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
   return render_template("about.html")

DOWNLOAD_DIRECTORY = "./static/img"
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

   resp = MessagingResponse()
   
   if request.values['NumMedia'] != '0':
      
      # Use the message SID as a filename.
      filename = request.values['MessageSid'] + '.png'
      with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
         image_url = request.values['MediaUrl0']
         f.write(requests.get(image_url).content)

         result = process_image('{}/{}'.format(DOWNLOAD_DIRECTORY, filename))

         print(result)
         
      if (result[0] == 0):
         resp.message("Image successfully processed. The prediction came back negative. It is unlikely that you have Parkinson's. Please note that this is not a diagnosis. If you have any questions or concerns, please consult a medical professional.")
      else:
         resp.message("Image successfully processed. The prediction came back positive. The drawing was similar to other patients that have Parkinson's disease. Please note that this is not a diagnosis. If you have any questions or concerns, please consult a medical professional.")
   else:
      resp.message("Try sending a picture message.")

   return str(resp)


if __name__ == '__main__':
    app.run(debug=True)