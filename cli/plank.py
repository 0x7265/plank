from requests import post
import argparse


parser = argparse.ArgumentParser()

def show_help():
   return """
          Plank v0.1 - model testing (c) readpy 2018
	  ------------------------------------------
          
	  """


def upload_model(filename):
   payload = {"filename": open(filename, "rb")}
   res = post("http://localhost:8888/upload", files=payload)
   print(res.text)

parser.add_argument("model", help="upload and run model testing on server")
parser.add_argument("--filename", help="model name", action="store", dest="filename")

args = parser.parse_args()

if args.model:
   if args.filename:
      upload_model(args.filename)	
