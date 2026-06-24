import cv2

def play_video(speed=0.5):
    cap = cv2.VideoCapture("C:/Users/Surendhar Reddy/Downloads/WhatsApp Video 2026-06-19 at 1.14.33 PM.mp4")

    if not cap.isOpened():
        print("Error: Could not open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        delay = int(1000 / (fps * speed))

        if cv2.waitKey(delay) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

play_video(speed=0.5)
