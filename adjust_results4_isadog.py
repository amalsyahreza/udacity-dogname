#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: Amal Syahreza
# DATE CREATED: 2024-01-09
# REVISED DATE: 2024-01-09
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the
#          dog name (from dognames.txt) and the 'value' is one. If a label is
#          found to exist within this dictionary of dog names then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the
#           label isn't a dog.

def adjust_results4_isadog(results_dic, dogfile):
    """
    Updates results_dic to indicate whether images are classified as 'dogs'
    or 'not dogs' and whether the classifier matches this classification.

    Parameters:
      results_dic - Dictionary where:
                    - key: image filename (string)
                    - value: list containing:
                        - index 0 = pet image label (string)
                        - index 1 = classifier label (string)
                        - index 2 = 1/0 (int) where 1 = match between pet and classifier
                          labels, 0 = no match
                        - index 3 = 1/0 (int) where 1 = pet image 'is-a' dog, 0 = not
                        - index 4 = 1/0 (int) where 1 = classifier 'is-a' dog, 0 = not
      dogfile - Filename of a text file containing dog names, one per line, all in
                lowercase. Each line may contain one or multiple dog names separated
                by commas (string)

    Returns:
      None - results_dic is mutable and updated in place.
    """
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        dogname_line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by
        # processing line and adding dognames to dognames_dic with while loop
        while dogname_line != "":
            dogname_line = dogname_line.replace('\n', '')

            if dogname_line not in dognames_dic:
                dognames_dic[dogname_line] = 1
            else:
                print('Warning: duplicate entries')

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            dogname_line = infile.readline()

    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic.
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key, value in results_dic.items():
        pet_label_is_dog = value[0] in dognames_dic
        classifier_label_is_dog = value[1] in dognames_dic

        # Determine the appropriate tuple to append based on the dog status
        if pet_label_is_dog and classifier_label_is_dog:
            value.extend((1, 1))  # Both labels are dogs
        elif pet_label_is_dog and not classifier_label_is_dog:
            value.extend((1, 0))  # Pet label is a dog, classifier label is not
        elif not pet_label_is_dog and classifier_label_is_dog:
            value.extend((0, 1))  # Pet label is not a dog, classifier label is
        else:
            value.extend((0, 0))  # Neither label is a dog
