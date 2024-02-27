import cv2



KNN_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)


bg_subtractor = KNN_subtractor

camera = cv2.VideoCapture("desktop\\data.mp3")

while True:
    ret, frame = camera.read()


    foreground_mask = bg_subtractor.apply(frame)


    ret, treshold = cv2.threshold(foreground_mask.copy(), 120, 255, cv2.THRESH_BINARY)


    dilated = cv2.dilate(treshold, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)


    contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:

        if cv2.contourArea(contour) > 50:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Subtractor", foreground_mask)
    cv2.imshow("threshold", treshold)
    cv2.imshow("detection", frame)

    if cv2.waitKey(30) & 0xff == 27:
        break

camera.release()
cv2.destroyAllWindows()
