
# Background Subtraction-Based Object Detection System

This Python script utilizes the OpenCV library to perform motion detection using the K-Nearest Neighbors (KNN) background subtraction method. The script reads frames from a video file or camera feed, subtracts the background to detect moving objects, and outlines them in rectangles.


## Acknowledgements

 - [BackgroundSubtractorKNN Class Reference](https://docs.opencv.org/4.x/db/d88/classcv_1_1BackgroundSubtractorKNN.html)
 - [opencv article ](https://learnopencv.com/moving-object-detection-with-opencv/#:~:text=The%20first%20step%20of%20moving,moving%20objects%20in%20the%20scene)

## Requirements

- Python 3.11
- OpenCV (cv2) library

##  How It Work

### 1.Background Subtraction Setup:
 The script first initializes a KNN (K-Nearest Neighbors) background subtractor using OpenCV's createBackgroundSubtractorKNN function. This subtractor is capable of identifying foreground objects while attempting to filter out background elements, even in the presence of shadows.

### 2.Video Capture:
It captures video frames from the default camera (or the camera specified by the index 0). If the camera fails to open, an error message is displayed, and the program exits.

### 3.Main Loop:
- Within the loop, each frame of the video is read using camera.read().

- Background subtraction is performed on the frame to identify potential foreground objects, resulting in a binary mask representing the foreground.
- A thresholding operation is applied to the foreground mask to segment out relevant foreground regions based on a predefined threshold value.

- dilation are conducted to refine the binary mask, improving the accuracy of object detection.
- Contours of objects in the binary mask are identified using cv2.findContours.

- For each contour, if its area exceeds a specified threshold (50 in this case), a bounding rectangle is drawn around it on the original frame.

- The processed frames, along with the foreground mask and thresholded image, are displayed 


### 4.Termination Condition:
 The loop continues until the user presses the 'Esc' key (27 in ASCII), upon which the program exits the loop and releases the camera resources.

 ### 5.Resource Cleanup:
  Once the loop terminates, the camera object is released using camera.release(), and all OpenCV windows are destroyed with cv2.destroyAllWindows().
## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```
and run the program
