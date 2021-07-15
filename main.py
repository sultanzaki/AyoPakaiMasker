import cv2
import time

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
noseCascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouthCascade = cv2.CascadeClassifier('mouth.xml')
video_capture = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

width  = video_capture.get(3)  # float `width`
height = video_capture.get(4)  # float `height`

while True:
    ret, frame = video_capture.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    nose = noseCascade.detectMultiScale(gray, 1.18, 35,)
    mouth = mouthCascade.detectMultiScale(gray, 1.7, 11)

    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    fps = str(fps)
    cv2.putText(frame, f"FPS: {fps}", (0, 20), font, 0.5, (255, 255, 255), 2)

    muka = len(faces)
    cv2.putText(frame, f"Jumlah wajah: {str(muka)}", (500,465), font, 0.5, (0, 255, 0), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

        if len(nose) > 0:
            status_nose = False
        else:
            status_nose = True

        if len(mouth) > 0:
            status_mouth = False
        else:
            status_mouth = True

        if status_nose and status_mouth:
            cv2.putText(frame, 'Hore! Kamu lagi pakai masker', (x, y-10), font, 0.5, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif status_nose or status_mouth:
            cv2.putText(frame, 'Pakai masker yang benar dong', (x, y-10), font, 0.5, (0, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        else:
            cv2.putText(frame, 'Ayo pakai maskermu', (x, y-10), font, 0.5, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Ayo Pakai Masker!', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
