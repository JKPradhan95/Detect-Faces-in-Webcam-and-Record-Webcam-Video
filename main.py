import cv2

video = cv2.VideoCapture(1)

if not video.isOpened():
    print("Error: Could not open video stream from the camera.")
    exit()

success, frame = video.read()

if not success:
    print("Error: Could not read frame from the camera.")
    exit()

height, width = frame.shape[:2]

face_cascade = cv2.CascadeClassifier('face.xml')

if face_cascade.empty():
    print("Error: Could not load face cascade classifier.")
    exit()

output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

if not output.isOpened():
    print("Error: Could not open video writer.")
    exit()

count = 0
while success:

  faces = face_cascade.detectMultiScale(frame, 1.1, 4)

  for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)

  output.write(frame)

    success, frame = video.read()
    count += 1
    print(f'Processed frame {count}')

output.release()
video.release()

print("Processing complete.")
