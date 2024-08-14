#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Amal Syahreza
# DATE CREATED: 2024-01-07
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

from logger import Logger


def extract_breed_name(name):
    """A small function to extract the breed name based on the splitter '_'
    """
    splitter = "_"
    split_position = name.rfind(splitter)

    return name[:split_position].replace('_', ' ').lower()


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Initialize logger
    logger = Logger().get_logger()

    # Creates list of files in directory
    in_files = listdir(image_dir)

    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    for filename in in_files:

        # Skips file if starts with '.' (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if filename.startswith('.'):
            continue

        # Creates temporary label variable to hold pet label name extracted
        pet_label = extract_breed_name(filename)

        # If filename doesn't already exist in dictionary add it and it's
        # pet label - otherwise print an error message because indicates
        # duplicate files (filenames)

        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            logger.warning(f"Duplicate files exist in directory: {filename}")

    return results_dic
