Hello! <br>
This repository contains full tutorial from google - TensorFlow For Poets 2 (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets) <br>
with custom dataset of traditional decor patterns gathered and published by Olga Belitskaya 
(https://www.kaggle.com/olgabelitskaya/preprocessing-of-pattern-images/data)

Also I was somehow inspired by article wrote by Radek Zaworski "DATA AUGMENTATION TECHNIQUES AND PITFALLS FOR SMALL DATASETS" (https://snow.dog/blog/data-augmentation-for-small-datasets)

<b>What I did to get all this work together?</b>
1. I downloaded Traditional decor patterns. <br>
2. I had to prepare data to fit training script from tutorial: <br>
	2.1. I analyzed Radek script from his article about data agumentation, looked at his example of dataset and .csv file to see what changes had to be made. <br>
	2.2. I rewrote code to fit my needs, in particular, I had to change indexes of columns, in which data were stored and I added small IF statement to filter out pattern label, because it was assumption on original task - that's how split_images.py was created. <br>
	2.3. I installed necessery library - Pillow and ran the script. As output I got directory "decor_split" with 7 subdirectories, one for every decor type, with converted .jpg files ready to feed to training script. <br>
3. Next steps were did according to Google's tutorial - I pulled scripts from git repository, deleted irrelevant files, copied "decor_split" to "tf_files" directory, started tensorboard and finally ran retrain script with following parameters:
	python -m scripts.retrain \
	  --bottleneck_dir=tf_files/bottlenecks \
	  --how_many_training_steps=8000 \
	  --model_dir=tf_files/models/ \
	  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}"/LR_0.0055_STEPS_8000 \
	  --output_graph=tf_files/retrained_graph.pb \
	  --output_labels=tf_files/retrained_labels.txt \
	  --architecture="${ARCHITECTURE}" \
	  --image_dir=tf_files/decor_split \
	  --learning_rate=0.0055
4. After bottlenecks were created based on my images, training procedure started. Accuracy chart in tensorbard shows that in peak model achieved 0.9400 so 94%.
5. After training I tested few pictures with label_image script that shows probability percentages for each of my label type and as expected for training images, every test showed accuracy of model around 99%.

<b>SUMMARY</b> <br>
I decided to not retrain model with changed hyperparameters, because I thought it was not really purpose of this task to get highest possible accuracy, but to show I can successfully connect given dataset and script to work together and I think I got quite high (maybe even too high? =] ) result from chosen learning rate and quantity of training steps in first run after all.
So, everything I did to complete task was: rewrite script that splits images to diffrent directories with names of labels and reproduces images as .jpg files, download git repository with tutorial, copy directory with images to correct place and run retraining last layer of model. Hyperparameters I used allowed model to achive maximum accuracy of <b>94%</b>. Next I tested some random pictures from dataset with testing script to ensure that my model can easly recognize decors from images.

Thanks for reading!
