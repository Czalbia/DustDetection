import os

import argparse



parser = argparse.ArgumentParser(description="The file name of your image")

parser.add_argument('--name', type=str, default='test')

args = parser.parse_args()

os.system(f'''/home/nvidia/jetson-inference/build/aarch64/bin/imagenet.py --model=models/solar2/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=data/solar2/labels.txt {args.name} RESULTS__{args.name}''')