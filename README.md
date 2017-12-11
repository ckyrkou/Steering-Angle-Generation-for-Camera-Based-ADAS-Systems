
![Angle_Throttle_Screenshot](/screenshot.jpg)


# Steering Angle and Throttle Generator for Images from Self-Driving Car 
These python files can be used to generate virtual steering angles for datasets acquired from a car mounter camera. For example in this way you can augment datasets used for detecting vehicles and pedestrian with steering angles so that you can train a car to simultaneously detect and drive.

**Dependancies:**

Python Libraries: os, cv2 (OpenCV), numpy, pyglet (Interface to game controller)

- Export images.zip to images folder. This zip containes 145 images for testing. You can download a larget set from here

https://github.com/udacity/self-driving-car/tree/master/annotations

- You need a steering wheel game pad to generate the angles. 

- Check if left pedal or right are captured for throttle
- You can adjust the time between frames in the code.
- The captured angles are normalized between []
- You can select the target directory in the python files.

**Files**

- joystick.py: Use to check if your steering wheel gamepad works correctly
- generate_steering_angles.py: Reads the images and the steering controller and records the steering angles
- drive.py: Used to playback what has been recorded. 

**Output**

- throttle_commands_<dir>.txt: Throttle command for each image in directory <dir>
- steering_commands_<dir>.txt: Steering command for each image in directory <dir>
