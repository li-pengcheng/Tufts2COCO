import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
from tqdm import tqdm

# ROOT_DIR = 'train'
# IMAGE_DIR = os.path.join(ROOT_DIR, "shapes_train2018")
# ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations")



INFO = {
    "description": "Example Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "waspinator",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': '1',
        'supercategory': 'tooth',
    },
    {
        'id': 2,
        'name': '2',
        'supercategory': 'tooth',
    },
    {
        'id': 3,
        'name': '3',
        'supercategory': 'tooth',
    },
    {
        'id': 4,
        'name': '4',
        'supercategory': 'tooth',
    },
    {
        'id': 5,
        'name': '5',
        'supercategory': 'tooth',
    },
    {
        'id': 6,
        'name': '6',
        'supercategory': 'tooth',
    },
    {
        'id': 7,
        'name': '7',
        'supercategory': 'tooth',
    },
    {
        'id': 8,
        'name': '8',
        'supercategory': 'tooth',
    },
    {
        'id': 9,
        'name': '9',
        'supercategory': 'tooth',
    },
    {
        'id': 10,
        'name': '10',
        'supercategory': 'tooth',
    },
    {
        'id': 11,
        'name': '11',
        'supercategory': 'tooth',
    },
    {
        'id': 12,
        'name': '12',
        'supercategory': 'tooth',
    },
    {
        'id': 13,
        'name': '13',
        'supercategory': 'tooth',
    },
    {
        'id': 14,
        'name': '14',
        'supercategory': 'tooth',
    },
    {
        'id': 15,
        'name': '15',
        'supercategory': 'tooth',
    },
    {
        'id': 16,
        'name': '16',
        'supercategory': 'tooth',
    },
    {
        'id': 17,
        'name': '17',
        'supercategory': 'tooth',
    },
    {
        'id': 18,
        'name': '18',
        'supercategory': 'tooth',
    },
    {
        'id': 19,
        'name': '19',
        'supercategory': 'tooth',
    },
    {
        'id': 20,
        'name': '20',
        'supercategory': 'tooth',
    },
    {
        'id': 21,
        'name': '21',
        'supercategory': 'tooth',
    },
    {
        'id': 22,
        'name': '22',
        'supercategory': 'tooth',
    },
    {
        'id': 23,
        'name': '23',
        'supercategory': 'tooth',
    },
    {
        'id': 24,
        'name': '24',
        'supercategory': 'tooth',
    },
    {
        'id': 25,
        'name': '25',
        'supercategory': 'tooth',
    },
    {
        'id': 26,
        'name': '26',
        'supercategory': 'tooth',
    },
    {
        'id': 27,
        'name': '27',
        'supercategory': 'tooth',
    },
    {
        'id': 28,
        'name': '28',
        'supercategory': 'tooth',
    },
    {
        'id': 29,
        'name': '29',
        'supercategory': 'tooth',
    },
    {
        'id': 30,
        'name': '30',
        'supercategory': 'tooth',
    },
    {
        'id': 31,
        'name': '31',
        'supercategory': 'tooth',
    },
    {
        'id': 32,
        'name': '32',
        'supercategory': 'tooth',
    },
    {
        'id': 33,
        'name': 'A',
        'supercategory': 'tooth',
    },
    {
        'id': 34,
        'name': 'B',
        'supercategory': 'tooth',
    },
    {
        'id': 35,
        'name': 'C',
        'supercategory': 'tooth',
    },
    {
        'id': 36,
        'name': 'D',
        'supercategory': 'tooth',
    },
    {
        'id': 37,
        'name': 'E',
        'supercategory': 'tooth',
    },
    {
        'id': 38,
        'name': 'F',
        'supercategory': 'tooth',
    },
    {
        'id': 39,
        'name': 'G',
        'supercategory': 'tooth',
    },
    {
        'id': 40,
        'name': 'H',
        'supercategory': 'tooth',
    },
    {
        'id': 41,
        'name': 'I',
        'supercategory': 'tooth',
    },
    {
        'id': 42,
        'name': 'J',
        'supercategory': 'tooth',
    },
    {
        'id': 43,
        'name': 'K',
        'supercategory': 'tooth',
    },
    {
        'id': 44,
        'name': 'L',
        'supercategory': 'tooth',
    },
    {
        'id': 45,
        'name': 'M',
        'supercategory': 'tooth',
    },
    {
        'id': 46,
        'name': 'N',
        'supercategory': 'tooth',
    },
    {
        'id': 47,
        'name': 'O',
        'supercategory': 'tooth',
    },
    {
        'id': 48,
        'name': 'P',
        'supercategory': 'tooth',
    },
    {
        'id': 49,
        'name': 'Q',
        'supercategory': 'tooth',
    },
    {
        'id': 50,
        'name': 'R',
        'supercategory': 'tooth',
    },
    {
        'id': 51,
        'name': 'S',
        'supercategory': 'tooth',
    },
    {
        'id': 52,
        'name': 'T',
        'supercategory': 'tooth',
    },
]



def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg', '*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]

    return files


def filter_for_annotations(root, files, image_filename):
    file_types = ['*.jpg']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]

    return files


def main():
    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }

    image_id = 1
    segmentation_id = 1

    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)

        # go through each image/
        for image_filename in tqdm(image_files):
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)

            # filter for associated png annotations
            for root, _, files in os.walk(ANNOTATION_DIR):
                annotation_files = filter_for_annotations(root, files, image_filename)

                # go through each associated annotation
                for annotation_filename in annotation_files:

                    # print(annotation_filename)
                    class_id = [x['id'] for x in CATEGORIES if x['name'] in annotation_filename][0]

                    category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}
                    binary_mask = np.asarray(Image.open(annotation_filename)
                                             .convert('1')).astype(np.uint8)

                    annotation_info = pycococreatortools.create_annotation_info(
                        segmentation_id, image_id, category_info, binary_mask,
                        image.size, tolerance=2)

                    if annotation_info is not None:
                        coco_output["annotations"].append(annotation_info)

                    segmentation_id = segmentation_id + 1

            image_id = image_id + 1

    with open('{}/instances_test2017.json'.format(ROOT_DIR), 'w') as output_json_file:
    # with open('{}/instances_test2017_16class.json'.format(ROOT_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)


if __name__ == "__main__":
    ROOT_DIR = r'E:\Datasets\xray\Tufts_Dental_Dataset\test\\'
    IMAGE_DIR = os.path.join(ROOT_DIR, "image")
    ANNOTATION_DIR = os.path.join(ROOT_DIR, "instmask")
    main()