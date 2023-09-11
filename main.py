import cv2



def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)
    
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    while True:
        success, img = cap.read()

        results = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=2)
        
        for (x, y, w, h) in results:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
        
        cv2.imshow('Webcam', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()