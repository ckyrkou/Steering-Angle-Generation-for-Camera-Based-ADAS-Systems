#High-level interface for joystick-like devices. This includes analogue and digital joysticks, gamepads, game
# controllers, and possibly even steering wheels and other input devices. There is unfortunately no way to distinguish
# between these different device types.

# It is assumed that the joystic axis take values from [-1,1]
# Steering angles are notmalized accordingly for left and right steering orientation
# Throttle is normalized between [0,1]

# Pyglet documentaion:
# http://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/api/pyglet/input/pyglet.input.Joystick.html

import os
import cv2
import numpy as np
import pyglet


cv2.namedWindow("Video", 0)

angle = 0
throttle = 0
breaks = 0

joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]
joystick.open()
print(joystick.device)

@joystick.event
def on_joyaxis_motion(joystick, axis, value):
    global angle,breaks,throttle
    if(axis == "x"):
        angle=value

    if (axis == "y"):
        throttle = (value + 1) / 2



def joyplay():
    angle.append(joystick.x)

def exiter(dt):
    pyglet.app.exit()

pyglet.clock.schedule_interval(exiter,0.5)

dir_name = 'images'
directory = './' + dir_name + '/'
file_angles  = open("steering_commands_"+dir_name+".txt", "w")
file_throttle  = open("throttle_commands_"+dir_name+".txt", "w")

i = 0
steering_angle = []

extension = '.jpg'
delay_between_frames = 200

seq = os.listdir(directory)

s=0

for ind in range(s,len(seq)):

        file = seq[ind]
        file_index.write(file+'\n')

        frame = cv2.imread(directory+file)

        frameSize = np.shape(frame)
        ar = frameSize[0]/frameSize[1]

        radius = int(frameSize[0]*0.2)
        x_i = 0
        y_i = radius

        pyglet.app.run()

        #Save Steering Wheel Normalized value [-1,1]
        steering_angle.append(-angle)

        #Rotating Steering Wheel on Image
        A = (steering_angle[ind-s]) * np.pi / 2 - np.pi / 2
        x_new = int(x_i * np.cos(A) - np.sin(A) * y_i)
        y_new = int(x_i * np.sin(A) + np.cos(A) * y_i)
        cv2.line(frame, (int(frameSize[1]/2)-1, frameSize[0]-1), (int(frameSize[1]/2)-1 - y_new, frameSize[0] -1 - x_new), (0, 0, 255), 20)
        cv2.circle(frame, (int(frameSize[1]/2)-1, frameSize[0]-1), radius, (0, 0, 255), 20)
        cv2.rectangle(frame, (int(frameSize[1]/4)-1, frameSize[0]-1), (int(frameSize[1]/4-frameSize[1]*0.1)-1, frameSize[0]-1-int(radius*throttle)), (255, 0, 0), -1)

        file_angles.write(str(steering_angle[ind-s]) + "\n")
        file_throttle.write(str(throttle) + "\n")

        for i in range(ind + 1, min(ind + 1 + 10, len(seq))):
            fileSeq = seq[i]
            imSeq = cv2.imread(directory + fileSeq)
            imSeq = cv2.resize(imSeq, (int(imSeq.shape[1] / 4), int(imSeq.shape[0] / 4)))
            frame[0:int(frame.shape[0] / 4), 0:int(frame.shape[1] / 4), :] = imSeq

        cv2.imshow('Video', frame)
        k = cv2.waitKey(delay_between_frames)

        if k & 0xFF == ord('q'):
            break

print('Captured '+str(ind)+' Steering Angles')
cv2.destroyWindow("video")
file_throttle.close()
file_angles.close()
