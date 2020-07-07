from imageai.Detection import ObjectDetection
import os
import config_detection

# SOURCE_PATH = "/home/tl/images/kholmy/200626_kholmy"

execution_path = os.getcwd()
source_images = config_detection.SOURCE_PATH
print(source_images)
files = os.listdir(source_images)
detector = ObjectDetection()

# detector.setModelTypeAsYOLOv3()
# detector.setModelPath(os.path.join(execution_path , "yolo.h5"))

detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))


detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(source_images, files[302]), 
                                             output_image_path='/home/tl/tl_intro/tl/imagenew5.jpeg', 
                                             minimum_percentage_probability=50)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")