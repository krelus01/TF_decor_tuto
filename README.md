Hello!
This repository contains full tutorial from google - TensorFlow For Poets 2 (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets) 
with custom dataset of traditional decor patterns gathered and published by Olga Belitskaya 
(https://www.kaggle.com/olgabelitskaya/preprocessing-of-pattern-images/data)

Also I was somehow inspired by article wrote by Radek Zaworski "DATA AUGMENTATION TECHNIQUES AND PITFALLS FOR SMALL DATASETS" (https://snow.dog/blog/data-augmentation-for-small-datasets)

What I did to get all this work together?
1. I downloaded Traditional decor patterns.
2. I had to prepare data to fit training script from tutorial:
	2.1 I analyzed Radek script from his article about data agumentation, looked at his example of dataset and .csv file to see what changes had to be made.
	2.2 I rewrote code to fit my needs, in particular, I had to change indexes of columns, in which data were stored and I added small IF statement to filter out pattern label, because it was assumption on original task - that's how split_images.py was created.
	2.3 I installed necessery library - Pillow and ran the script. As output I got directory "decor_split" with 7 subdirectories, one for every decor type, with converted .jpg files ready to feed to training script.
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
4. After bottlenecks created based on my images, training procedure started. Accuracy chart in tensorbard shows that in peak I achieved 0.9400 so 94%.
5. After training I tested few pictures with label_image script that shows probability percentages for each of my label type and as expected for training images, every test showed accuracy of model around 99%.

SUMMARY
I decided to not retrain model with changed hyperparameters, because I thought it was not really purpose of this task to get highest possible accuracy, but to show I can successfully connect given dataset and script to work together and I think I got quite high (maybe even too high? =] ) result from chosen learning rate and quantity of training steps in first run after all.