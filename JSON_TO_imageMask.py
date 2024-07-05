import numpy as np
import matplotlib.colors as mcolors
from pycocotools.mask import maskUtils
import json
import cv2
import os

def load_json_data(json_path):
    with open(json_path,'r') as file:
        data = json.load(file)
    return data


# READY ANNOTATIONS BEGIN
def draw_bbox(image,color, boundingBox):
    alpha = 0.5
    height, width, _ = image.shape
    x = int(boundingBox["x"] * width)
    y = int(boundingBox["y"] * height)
    w = int(boundingBox["w"] * width)
    h = int(boundingBox["h"] * height)
    # Draw the bounding box on the image with transparency
    overlay = image.copy()
    cv2.rectangle(overlay, (x, y), (x+w, y+h), color[:3], thickness=2)
    cv2.addWeighted(overlay, alpha, image, 1 -alpha, 0, image)

def draw_polygon(image,color, polygon_dict):
    alpha = 0.3
    height, width, _ = image.shape
    polygon_points = []
    for i in range(len(polygon_dict)):
        x = int(polygon_dict[str(i)]["x"] * width)
        y = int(polygon_dict[str(i)]["y"] * height)
        polygon_points.append((x, y))
    pts = np.array([polygon_points], dtype=np.int32)
    mask = image.copy()
    cv2.fillPoly(mask, [pts], color[:3])
    cv2.addWeighted(mask, alpha, image, 1 - alpha, 0, image)

def draw_polyline(image,color, polygon_dict):
        alpha = 0.1
        height, width, _ = image.shape
        polygon_points = []
        for i in range(len(polygon_dict)):
            x = int(polygon_dict[str(i)]["x"] * width)
            y = int(polygon_dict[str(i)]["y"] * height)
            polygon_points.append((x, y))
        cv2.polylines(image, [np.array(polygon_points)], isClosed=False, color=color, thickness=2)

def draw_bitmask(image,color, bitmask_dict):

    # Decode RLE string to binary mask
    rle = bitmask_dict["rleString"]
    mask = maskUtils.decode(rle)
    alpha = 0.9  # Transparency for the bitmask

    # Ensure the color is in the correct format (B, G, R)
    color = tuple(int(c) for c in color)

    # Create an overlay where the mask is true
    overlay = np.zeros_like(image, dtype=np.uint8)
    overlay[mask == 1] = color

    # Create a mask where the overlay is applied
    mask_indices = mask == 1

    # Blend only the overlay with the original image
    image[mask_indices] = cv2.addWeighted(overlay[mask_indices], alpha, image[mask_indices], 1 - alpha, 0)
##########################



# Pending ANNOTATIONS
def draw_Rbox(image,color, segmentation):
    1

def draw_keypoint(image,color, segmentation):
    1
###############################










# PARTIALLY COMPLETE######$%%$%#%%$#%^#$%^#%$#%^#%#^%#$^%#%$#%^$#%$#
def process_annotations(image, objects):
    # image_annotations IS A LIST CONTAINING ANNOTATIONS (in from of dictionaries)
    for labels in objects:
        # 1st dictionary is selected
        HEX_color = labels["color"]
        color = hex_to_bgr(HEX_color)
        print(color)

        if labels["shape"] == "bounding_box":
            draw_bbox(image,color,labels["boundingBox"])
        elif labels["shape"] == "bitmask":
            draw_bitmask(image,color,labels["bitmask"])
        elif labels["shape"] == "polygon":
            draw_bbox(image,color,labels["polygon"])
        elif labels["shape"] == "polyline":
            draw_bbox(image,color,labels["polyline"])


        ###### pending

        elif labels["shape"] == "keypoint":
            draw_keypoint(image,color,labels["keypoint"])
        elif labels["shape"] == "rotatable_rectangle":
            draw_bbox(image,color,labels["rotatable_rectangle"])

def hex_to_bgr(hex_code):
    rgb_color = mcolors.hex2color(hex_code)
    bgr_color = tuple(reversed([int(255 * x) for x in rgb_color]))  # Reversed order (BGR)
    return bgr_color # Returns (B,G,R) format [easy for cv2 to use]

def save_annotated_image(image, output_path):
    cv2.imwrite(output_path, image)
    print(f"Saved annotated image to {output_path}")

def annotate_images(json_path, base_image_directory, overlay_directory, Mask_directory):
    data = load_json_data(json_path)

    for dict in data:
        # DICTIONARY OF EACH IMAGE IS PASSED
        # we iterate through each dictionary (i.e. an element in the list)
        image_path = os.path.join(base_image_directory, dict['data_title'])
        image = cv2.imread(image_path)
        
        #exception handeling
        if image is None:
            print(f"Image {dict['data_title']} not found.")
            continue        
        if dict["label_status"] != "LABELLED":
            #if image is not labeled, continue to next image
            continue

        # Creating blank image
        blank_image = np.ones(image.shape, dtype=np.uint8) * 255  # White background

        for obj in dict["data_units"].values():
        # Extracting data_units{} > label{} > objects[]
        # data_units KAR K 1 KEY H JIS KI VALUE = DICTIONARY CONTAINING ALL THE ONTOLOGIES
        # VALUES OF ALL ONTOLOGIES IN IMAGE IS PASSED

            labels = obj["labels"] #this is the dict containing all the ontolgy (annotation & classification)
            
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            # LIST OF ANNOTATIONS (ONLY) IS SELECTED
            annotaion_list = labels["objects"] #ONLY FOR ANNOTATIONS (not classification)




            # for overlay annotation
            process_annotations(image,annotaion_list)
            output_path = os.path.join(overlay_directory, dict['data_title'])
            save_annotated_image(image, output_path)

            #for mask only annotation
            process_annotations(blank_image,annotaion_list)
            output_path = os.path.join(Mask_directory, dict['data_title'])
            save_annotated_image(image, output_path)



json_path = "C:/Users/EIOT/Desktop/Encord/EXPORT/sample.json"
base_images_directory = 'Input_2'  
overlay_directory = 'Output_1'
Mask_directory = 'Output_2'  

