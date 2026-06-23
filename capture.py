import cv2
import time
import os
from datetime import datetime


def capture(target_index, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(target_index, cv2.CAP_DSHOW)
    img_count = 0
    if not cap.isOpened():
        print("Could not initialize the USB hardware.")
    else:
        print("Success!")
        try:
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    print("Error: Could not read frame from camera.")
                    break
                    
                # cv2.imshow("USB Camera Live Feed", frame)
                img_count += 1
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(save_dir, f"img_{img_count}_{timestamp}.jpg")

                cv2.imwrite(filename, frame)
                print(f"Saved {filename}")
                


                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
            
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopped")

        cap.release()
        cv2.destroyAllWindows()
        print("Camera feed closed safely.")

if __name__ == "__main__":
    capture(1, "media")