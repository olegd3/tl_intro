from imageai.Detection import ObjectDetection
import os
import config_detection

# SOURCE_PATH = "/home/tl/images/kholmy/200626_kholmy"

execution_path = os.getcwd()
source_images = config_detection.SOURCE_PATH
model_name = "resnet50_coco_best_v2.0.1.h5"
files = os.listdir(source_images)
print(source_images)

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path , model_name))
detector.loadModel()
print(f'model --> {model_name} was loaded')
# detections = detector.detectObjectsFromImage(input_image=os.path.join(source_images, files[302]), 
#                                              output_image_path='/home/tl/tl_intro/tl/imagenew5.jpeg', 
#                                              minimum_percentage_probability=50)

returned_image, detections = detector.detectObjectsFromImage(input_image=os.path.join(source_images, files[302]), 
                                             output_type="array", 
                                             minimum_percentage_probability=50)

# detector.detectObjectsFromImage(input_image=”image.jpg”, output_type=”array”, minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
