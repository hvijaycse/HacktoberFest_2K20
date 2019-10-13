# DNN-based-Face-Detection
> Deep Neural Net based face detection project, detetcting the faces in the images, videos, 
> or using webcam with a greater accuracy, as compared to my previous project on face detection.
> It is based on Single-Shot-Multibox detector and uses ResNet-10 Architecture as backbone. 
> The model was trained using images available from the web, but the source is not disclosed. 
> OpenCV provides 2 models for this face detector:
> 1. Floating point 16 version of the original caffe implementation.
> 2. 8 bit quantized version using Tensorflow.

This is CAFFEMODEL based implementation of the project.

# Pre-requisites
* Python 3.6+
* OpenCV (version 3.x or higher)
* Caffemodel file, used for detection(provided in the uploaded files)
* Deploy.prototxt file(provided in the uploaded files)

# Installation
1. Here I have not used anaconda python distribution for the environment and hence I had to build the OpenCV package from the 
source for the implementation of this project. Also, keep in mind creating a virtual environment for the installing the package separartely, which is rather prefferd over installing it directly on your system. Refer to the link mentioned below to build the package from the source:

[Building OpenCV package from the source](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/)

Once OpenCV and other dependencies are installed, you're good to go!

2. Clone the project and put all the files in a separate folder/directory.
3. Open up the terminal on your Ubuntu machine, move to the directory in which your files are saved, and run the following commands:
 
* For face_detction_images file(Detecting faces in an image)

```
$python face_detection_images.py --image IMAGE_NAME.jpg --prototxt deploy.prototxt \--model dnn_model.caffemodel
```
> Make sure the images are of format 'jpg'(any other format, even jpeg, will throw errors).
> Also, make sure not to give any unnecesssary spaces in this command, as it may also throw some errors.

* For face_detection_videos.py

```
$python face_detection_videos.py --prototxt deploy.prototxt \--model dnn_model.caffemodel
```

> To stop detection process, hit 'x' key on your keyboard.

4. Voila! You just created a face detection model.

# Results

![](https://github.com/kgautam01/DNN-based-Face-Detection/blob/master/ss1.png)

![](https://github.com/kgautam01/DNN-based-Face-Detection/blob/master/ss3.png)

![](https://github.com/kgautam01/DNN-based-Face-Detection/blob/master/ss4.png)
