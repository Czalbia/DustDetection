# Dust Detect AI

Hi, this is a Dust Detector Neural Network. Solar panels are getting more and more popular; however, many people don't know that when solar panels aren't cleaned they can lose up to 35% of their effectiveness.
To help people pay less for electricity bills and contribute to the elimination of climate change I created this project. 

![Clean Solar Panel](https://github.com/Czalbia/DustDetection/assets/58823176/0fa91e9b-97d0-4ab7-a36d-42f483761ead)

## The Algorithm

THe first step was downloading a [database](https://www.kaggle.com/datasets/hemanthsai7/solar-panel-dust-detection) which has images of both dirty and clean solar panels. Next step was to split it to TRAIN/TEST/VAL directories in order to train a model based on them. After spliting I deleted some images that were advertisements of solar panels. After spliting and removing the ads I started coding the main part of this project. To make my project more usefull and better instead of creating my own neural network I used a pretrained RESNET-18. I trained it for 40 epochs and increased the batch size to 12, instead of default 8. The model has around 72% accuracy and is the best one I could train. In the future I will try to make it more accurate and code my own neural network from scratch. 

## Running this project

1. Make sure you downloaded `jetson-inference` library and built it succesfully
2. Download the folder of model `Solar2` or any model in models folder
3. Download modified version of `imagenet.py` file
4. Remove imagenet from `jetson_inference/build/aarch64/bin/` and place the new one in it
5. Place your image `jetson-inference/python/training/classification` directory
6. Download `runALL.py` file
7. Run `runALL.py --name --model ` command with the file name of the image and the model you downloaded 
8. Your result will be a `<name>__RESULT.jpg`


[View a video explanation here](video link)
