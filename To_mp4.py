import cv2 
import os

image_folder = 'temp_images'
# mp4 currently pulls up an error.
# I need to change duration of page. Looking up cv2.VideoWriter
# video_name = 'video.mp4'  
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()