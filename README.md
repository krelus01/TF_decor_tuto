Hello!
This repository contains full tutorial from google - TensorFlow For Poets 2 (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets) 
with custom dataset of kind of east-europe traditional decor patterns gathered and published by Olga Belitskaya 
(https://www.kaggle.com/olgabelitskaya/preprocessing-of-pattern-images/data)

Created model in initial commit was trained once, with default hyperparameters and got verification accuracy value of 0.73.

Second training I started with changned learning rate (from default 0.01 to 0.0055) and increased training steps to 4000. Result was 0.83 at the end of the process. Final test accuracy was 80%

In third training I changed batch for train to 5, as well as learning rate to 0.0071. As expected, due to reduced batch size for training, final accuracy dropped to 62%.

