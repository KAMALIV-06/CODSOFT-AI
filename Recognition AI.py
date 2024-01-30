import cv2
import face_recognition

# Load a pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load images with known faces and their names
known_face_names = ["Person1", "Person2"]
known_face_images = [face_recognition.load_image_file("person1.jpg"), face_recognition.load_image_file("person2.jpg")]

# Encode the known faces
known_face_encodings = [face_recognition.face_encodings(img)[0] for img in known_face_images]

# Function to detect and recognize faces in an image
def detect_and_recognize_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces using Haar Cascade
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Extract face region
        face_roi = image[y:y+h, x:x+w]

        # Encode the detected face
        face_encoding = face_recognition.face_encodings(face_roi)

        # Compare with known faces
        for i, known_encoding in enumerate(known_face_encodings):
            # Check if the detected face matches a known face
            matches = face_recognition.compare_faces([known_encoding], face_encoding[0])

            name = "Unknown"
            if True in matches:
                name = known_face_names[i]

            # Draw rectangle around the face and display the name
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Face Detection and Recognition', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path_to_process = "test_image.jpg"
detect_and_recognize_faces(image_path_to_process)
