# Detection-from-live-video-feed-
A python application that processes the video data stream 
captured by a DJI drone located at almost 50(fifty meters) altitude above the ground, and sent via wifi internet network to an rtmp server to be processed by a python script called through the windows terminal in order to detect people. 
The detections are made in boxes of different colors.
I used the hog descriptor from the computer vision library opencv,  respectively I configured an Nginx server to support RTMP connections.
