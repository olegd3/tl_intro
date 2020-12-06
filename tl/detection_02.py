from imageai.Detection import ObjectDetection
import os
import config_detection

source_images = config_detection.SOURCE_PATH


class BaseDetection(ObjectDetection):
    def __init__(self):
        ObjectDetection.__init__(self)

    def get_objects_list(self, input_image_list):
        self.input_image_list = input_image_list
        execution_path = os.getcwd()
        self.model_name = "resnet50_coco_best_v2.0.1.h5"
        print(self.input_image_list)
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path , self.model_name))
        detector.loadModel()
        print(f'model --> {self.model_name} was loaded')
        print(f'Image List lenght --> {len(self.input_image_list)} ')
        for f in input_image_list:
            returned_image, detections = detector.detectObjectsFromImage(f, output_type="array", minimum_percentage_probability=50)
            print(f'File name for det-n is {f}')
            print("+++++++++++++++++++++++++++++++++++++++")

            for eachObject in detections:
                print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
                print("----------------------------------------")


files = os.listdir(source_images)
files = sorted(files, reverse=True)
files_for_detection = [os.path.join(source_images, files[i]) for i in range(len(files)) if 0<i<300]
print(files_for_detection)
det = BaseDetection()
det.get_objects_list(files_for_detection)
