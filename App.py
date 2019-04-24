from appJar import gui
import cv2

imageFileLabelTitle = "Image file: "
headingLabelTitle = "title"
detectButtonTitle = "Detect"
showOriginalButtonTitle = "Show original"
quitButtonTitle = "Quit"
tableTitle = "table"

app = gui("Object detection in images (mini project)", "640x480")
app.setResizable(False)
app.setBg("purple")
app.setFont(size=18, family="Consolas", slant="italic")

app.addLabel(headingLabelTitle, "Mini Project: Object Detection in Images")
app.setLabelBg(headingLabelTitle, "red")
app.setLabelFg(headingLabelTitle, "white")
app.setLabelHeight(headingLabelTitle, 5)

app.addLabelEntry(imageFileLabelTitle)
app.setLabelFg(imageFileLabelTitle, "white")
app.setEntry(imageFileLabelTitle, "image.jpg")


def press(button):
	if button == detectButtonTitle:
		detect(app.getEntry(imageFileLabelTitle))

	elif button == showOriginalButtonTitle:
		imgName = app.getEntry(imageFileLabelTitle)
		img = cv2.imread(imgName)
		cv2.imshow("Original", img)
		cv2.waitKey(1)

	elif button == quitButtonTitle:
		app.stop()


def detect(infile):
	from MyObjectDetection import MyObjectDetection

	objectDetector = MyObjectDetection(infile)

	objectDetector.run()
	objectDetector.show()

	imgName = app.getEntry(imageFileLabelTitle)

	winName = "Original"
	cv2.namedWindow(winName)
	cv2.moveWindow(winName, 0, 0)

	img = cv2.imread(imgName)
	img = cv2.resize(img, (640, 480))
	cv2.imshow(winName, img)
	cv2.waitKey(1)

	app.startSubWindow("table")
	detections = objectDetector.getTable()
	app.addTable(tableTitle, [["Name", "Percentage probability"]])
	for eachObject in detections:
		row = [eachObject["name"], eachObject["percentage_probability"]]
		app.addTableRow(tableTitle, row)
	app.stopSubWindow()

	app.showSubWindow("table")


app.addButtons([detectButtonTitle, showOriginalButtonTitle, quitButtonTitle], press)

app.go()



