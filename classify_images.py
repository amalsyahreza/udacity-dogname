#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Amal Syahreza
# DATE CREATED: 2024-01-09
# REVISED DATE: 2024-01-09
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function
#             and as in_arg.dir for function call within main.
#            -The results dictionary as results_dic within classify_images
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#
import os

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Classifies images using the classifier function and compares pet labels
    with classifier labels, updating the results dictionary with classifier
    labels and comparison results.

    Parameters:
      images_dir - The full path to the folder of images to be classified (string)
      results_dic - Dictionary with 'key' as image filename and 'value' as a List:
                    Index 0 = pet image label (string)
                    NEW - Index 1 = classifier label (string)
                    NEW - Index 2 = 1/0 (int), where 1 = match between pet image
                             and classifier labels, 0 = no match
      model - CNN model architecture used for classification, values must be:
              'resnet', 'alexnet', or 'vgg' (string)

    Returns:
      None - The results_dic is mutable, so no return is needed.
    """
    for filename, data in results_dic.items():
        # Get the classifier label and format it
        image_path = os.path.join(images_dir, filename)
        classifier_label = classifier(image_path, model).strip().lower()

        # Append the classifier label to the results dictionary
        data.append(classifier_label)

        # Check if the pet image label is in the classifier label
        pet_label = data[0].strip().lower()
        is_match = int(pet_label in classifier_label)

        # Append the match result (1 or 0) to the results dictionary
        data.append(is_match)
