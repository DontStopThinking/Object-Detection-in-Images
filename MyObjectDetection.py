from imageai.Detection import ObjectDetection
import os
import cv2


class MyObjectDetection:

	def __init__(self, infile):
		self.executionPath = os.getcwd()
		self.infile = infile
		self.outfile = str(self.infile[:-4]) + "_output.jpg"

	def run(self):
		detector = ObjectDetection()
		detector.setModelTypeAsRetinaNet()
		detector.setModelPath(os.path.join(self.executionPath, "Models/resnet50_coco_best_v2.0.1.h5"))
		detector.loadModel()
		global detections
		detections = detector.detectObjectsFromImage(input_image = os.path.join(self.executionPath, self.infile),
															output_image_path = os.path.join(self.executionPath, self.outfile))

	# Returns a dictionary of the detections
	def getTable(self):
		for eachObject in detections:
	    	    print(eachObject["name"], ":", eachObject["percentage_probability"])
		return detections

	def show(self):
		winName = "Image with detected objects"
		cv2.namedWindow(winName)
		cv2.moveWindow(winName, 600, 0)

		img = cv2.imread(self.outfile)
		img = cv2.resize(img, (640, 480))
		cv2.imshow(winName, img)
		cv2.waitKey(1)

