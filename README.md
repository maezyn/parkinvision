<p align="center">
  <img src="https://github.com/mmore21/parkinvision/blob/master/static/img/logo.png" width="300" />
</p>

<p align="center">
  Hand-drawn spiral prediction for Parkinson's disease.
</p>
<p align="center">
  <a href="https://devpost.com/software/parkinvision-79jpa8">Devpost</a>
</p>

## About

This project was created for UC Irvine's [HackUCI](https://www.hackuci.com/) 2020 hackathon. It started as a solo project created in 32 hours. For more detailed information on the project, please refer to the Devpost link above.

## Technologies

* Python
* Tensorflow 2.0 / Keras
* scikit-learn
* OpenCV
* Flask
* Twilio API

## Machine Learning and Deep Learning Approach

Two different models were trained for this task (as a learning experience). Ultimately, the machine learning approach was chosen as the lack of data stunted the deep learning model's performance.

* The machine learning approach trained a Random Forest classifier using the scikit-learn and OpenCV libraries.
* The deep learning approach trained a standard Convolutional Neural Network using a Tensorflow 2.0 / Keras model with data augmentation.

## Acknowledgements

The data folder was downloaded from an article on [pyimagesearch](https://www.pyimagesearch.com/2019/04/29/detecting-parkinsons-disease-with-opencv-computer-vision-and-the-spiral-wave-test/) which provides the author's own approach to machine learning on this data set. Some of the computer vision techniques were derived from his post. Additionally, he mentioned the source of the data set, Adriano de Oliveira Andrade and Joao Paulo Folado from the NIATS of Federal University of Uberlândia. 
