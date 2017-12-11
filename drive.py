import os
import cv2
import numpy as np



cv2.namedWindow("Video", 0)


i = 0
steering_angle = []
extension = '.jpg'
delay_between_frames = 200

dir_name = 'images'
directory = './' + dir_name + '/'
file_angles  = open("steering_commands_"+dir_name+".txt", "r")
file_throttle  = open("throttle_commands_"+dir_name+".txt", "r")




for file in os.listdir(directory):
    if file.endswith(extension):

        frame = cv2.imread(directory+file)

        frameSize = np.shape(frame)
        ar = frameSize[0]/frameSize[1]

        radius = int(frameSize[0]*0.2)
        x_i = 0
        y_i = radius

        line = file_angles.readline()
        line2 = file_throttle.readline()

        if len(line.strip()) == 0 :
            cv2.destroyWindow("video")
            break

        angle = -float(line)
        throttle = float(line2)


        A = (-angle) * np.pi / 2 - np.pi / 2
        x_new = int(x_i * np.cos(A) - np.sin(A) * y_i)
        y_new = int(x_i * np.sin(A) + np.cos(A) * y_i)
        cv2.line(frame, (int(frameSize[1] / 2) - 1, frameSize[0] - 1), (int(frameSize[1] / 2) - 1 - y_new, frameSize[0] - 1 - x_new), (0, 0, 255), 20)
        cv2.circle(frame, (int(frameSize[1] / 2) - 1, frameSize[0] - 1), radius, (0, 0, 255), 20)
        cv2.rectangle(frame, (int(frameSize[1] / 4) - 1, frameSize[0] - 1),
                      (int(frameSize[1] / 4 - frameSize[1] * 0.1) - 1, frameSize[0] - 1 - int(radius * throttle)),
                      (255, 0, 0), -1)
        i += 1
        cv2.imshow('Video', frame)

        k = cv2.waitKey(delay_between_frames)

        if k & 0xFF == ord('q'):
            file_angles.close()
            file_throttle.close()
            cv2.destroyWindow("video")
            break



