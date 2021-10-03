# Import packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import time

# Load Model
global model
model = load_model("mask_detector.model")

def predict(face):
	
	face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
	face = cv2.resize(face, (224, 224))
	face = img_to_array(face)
	face=np.expand_dims(face, axis=0)
	face = np.vstack([face])
	face = preprocess_input(face)
	preds = model.predict(face)
	
	return preds

# Read video from camera
vid = cv2.VideoCapture(0)

prev_frame_time ,new_frame_time = 0,0

while True:

	istrue,frame = vid.read() # obtaining frames from video

	if not istrue:		
		break
	
	new_frame_time = time.time()


	pred = predict(frame)

	mask, noMask = pred[0][0],pred[0][1]

	if mask > noMask:
		ans='mask Found'
	else:
		ans='No mask Found'
		

	fps = 1/(new_frame_time-prev_frame_time)
	prev_frame_time = new_frame_time

	fps=str(int(fps))

	fps_string='FPS: '+fps

	cv2.putText(frame, ans, (10, 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,0,0), 2)
	cv2.putText(frame, fps_string, (10, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,0,0), 2)
	
	

	cv2.imshow("Frame", frame)


	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


cv2.destroyAllWindows()
