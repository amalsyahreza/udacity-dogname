#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.
# PROGRAMMER: Amal Syahreza
# DATE CREATED: 2024-01-07
# REVISED DATE: 2024-01-09
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

from time import time

from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from classify_images import classify_images
# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from logger import Logger
# Imports print functions that check the lab
from print_functions_for_lab_checks import *
from print_results import print_results


# Main program function defined below
def main():
    # Initialize logger
    logger = Logger().get_logger()

    # Measures total program runtime by collecting start time
    start_time = time()
    logger.info(f"Application started at {start_time}")

    # Retrieves and parse input
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Checks Pet Images in the results Dictionary using results
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int(tot_time % 60)

    logger.info(f"Total Elapsed Runtime: {hours:02}:{minutes:02}:{seconds:02}")


# Call to main function to run the program
if __name__ == "__main__":
    main()
