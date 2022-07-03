diff --git a/source-code.py b/source-code.py
new file mode 100644
--- /dev/null
+++ b/source-code.py
@@ -0,0 +1,48 @@
+# Imports
+import numpy as np
+import cv2
+ 
+# Initialize the HOG descriptor/person detector
+hog = cv2.HOGDescriptor()
+hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
+
+cv2.startWindowThread()
+
+# Open camera acquisition video stream from drone over internet (using rtmp server)
+cap = cv2.VideoCapture('rtmp://192.168.43.13/live/rtmpkey:80')
+
+# The output will be written to output.avi
+out = cv2.VideoWriter(
+    'output.avi',
+    cv2.VideoWriter_fourcc(*'MJPG'),
+    15.,
+    (1920,1080))#live video streaming resolution
+
+while(True):
+    # Capture frame-by-frame
+    ret, frame = cap.read()
+   # Terminal window view
+    frame = cv2.resize(frame, (1920,1080))
+   # Using a greyscale picture, also for faster detection
+    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
+   # Detect people in the image
+   # Returns the bounding boxes for the detected objects
+    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
+    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
+    for (xA, yA, xB, yB) in boxes:
+        # Display the detected boxes in the colour picture
+        cv2.rectangle(frame, (xA, yA), (xB, yB),
+                          (255, 0, 0), 2)   
+    # Write the output video 
+    out.write(frame.astype('uint8'))
+    # Display the resulting frame
+    cv2.imshow('frame',frame)
+    if cv2.waitKey(1) & 0xFF == ord('q'):
+        break
+# When everything done, release the capture
+cap.release()
+# Release the output
+out.release()
+# Close the window
+cv2.destroyAllWindows()
+cv2.waitKey(1)
\ No newline at end of file