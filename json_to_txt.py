import json
import os

with open("result_yolov3.json") as json_file:
    results = json.load(json_file)

    for image in results:
        image_name = image["filename"].split("/")[-1]
        save_path = os.path.join("../data/detections_yolov3/", image_name.replace(".png", ".txt"))
        
        with open(save_path, "w") as f:
            for detection in image["objects"]:
                box = detection["relative_coordinates"]
                center_x = box["center_x"]
                center_y = box["center_y"]
                width = box["width"]
                height = box["height"]
                conf = detection["confidence"]
                cl = detection["class_id"]
                f.write("{} {} {} {} {} {}\n".format(cl, conf, center_x, center_y, width, height))