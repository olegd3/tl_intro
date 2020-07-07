from imageai.Detection import ObjectDetection
import os
import config_detection

#  SOURCE_PATH = "/home/tl/images/kholmy/200626_kholmy"

execution_path = os.getcwd()
source_images = config_detection.SOURCE_PATH
print(source_images)
files = os.listdir(source_images)
print(f'Execution_path is  {execution_path}')
print(f'Test image is {files[300]}')
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image='/home/tl/tl_intro/tl/358905.jpeg', 
                                             output_image_path='/home/tl/tl_intro/tl/imagenew.jpeg', 
                                             minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")