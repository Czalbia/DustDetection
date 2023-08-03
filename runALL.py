import os

import argparse



parser = argparse.ArgumentParser(description="The file name of your image")

parser.add_argument('--name', type=str, default='test', help='--name <path to the image you want to use>')

parser.add_argument('--model', type=str, default='solar', help='--model <the path to the model that you want to use>')

args = parser.parse_args()

os.system(f'''/home/nvidia/jetson-inference/build/aarch64/bin/imagenet.py --model=models/{args.model}/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=data/{args.model}/labels.txt {args.name} RESULTS__{args.name}''')
