import cv2
import os

def create_timelapse(image_folder, video_name, fps=30):
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()

    if not images:
        print("No images found in the specified directory.")
        return

    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    print(f"Starting timelapse creation with {len(images)} frames...")
    
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        
        if frame.shape[0] != height or frame.shape[1] != width:
            frame = cv2.resize(frame, (width, height))
            
        video.write(frame)

    video.release()
    print(f"Timelapse video saved successfully as {video_name}")


if __name__ == "__main__":
    IMAGE_DIRECTORY = "media"  
    OUTPUT_VIDEO = "timelapse.mp4"
    FRAMES_PER_SECOND = 24
    create_timelapse(IMAGE_DIRECTORY, OUTPUT_VIDEO, fps=FRAMES_PER_SECOND)
