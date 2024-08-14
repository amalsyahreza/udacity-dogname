#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Amal Syahreza
# DATE CREATED: 2024-01-09
# REVISED DATE: 2024-01-10
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function.
#       Notice that this function doesn't to return anything because it
#       prints a summary of the results using results_dic and results_stats_dic
#

def print_results(
        results_dic,
        results_stats_dic,
        model,
        print_incorrect_dogs=False,
        print_incorrect_breed=False):
    """
    Prints summary results on the classification and then optionally prints incorrectly
    classified dogs and dog breeds based on user preference.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a List:
                    idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and classifier labels,
                                        0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog,
                                        0 = pet image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 'as-a' dog,
                                        0 = Classifier classifies image 'as-NOT-a' dog.
      results_stats_dic - Dictionary containing results statistics (either a percentage or a count),
                          with keys representing the statistic's name and values being the statistic's value.
      model - Indicates the CNN model architecture used to classify the pet images.
              Values must be one of: 'resnet', 'alexnet', 'vgg' (string)
      print_incorrect_dogs - If True, prints incorrectly classified dog images; otherwise, prints nothing (bool)
      print_incorrect_breed - If True, prints incorrectly classified dog breeds; otherwise, prints nothing (bool)

    Returns:
      None - simply a function to prints the results.
    """

    # Prints summary statistics over the run
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    print(f"{'N Images':20}: {results_stats_dic['n_images']:3d}")
    print(f"{'N Dog Images':20}: {results_stats_dic['n_dogs_img']:3d}")
    print(f"{'N Not-Dog Images':20}: {results_stats_dic['n_notdogs_img']:3d}")

    print("\nModel Performance (Percentages):")

    # Print all percentage statistics
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):
            print(f"{key:20}: {value:.3f}%")

    # Print incorrectly classified dogs when requested
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']:
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key, value in results_dic.items():
            if (value[3] == 1 and value[4] == 0) or (value[3] == 0 and value[4] == 1):
                print(f"{value[0]:>26}  -  {value[1]:>30}")

    # Print incorrectly classified breeds if requested
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nINCORRECT Dog Breed Assignment:")
        for key, value in results_dic.items():
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print(f"Real: {value[0]:>26}   Classifier: {value[1]:>30}")
