import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--filename", help="increase output verbosity",
                    action="store", dest="filename")

parser.add_argument("model", help="upload and run model testing on the server")


args = parser.parse_args()

if args.model:
   if args.filename:
      print("uploading model {}".format(args.filename))



