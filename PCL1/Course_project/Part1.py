"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection
Students: <person 1>, <person 2>
"""
# --- Imports ---
import os
import re
import nltk
import spacy
import json

# --- You may add other imports here ---
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


def perform_NER(doc):
    '''Function that finds all the names and aliases of the characters in the book'''
    names_dict = {}
    for ent in doc.ents:
        if ent.label_ == 'PERSON': #check if tag is PERSON
            name = ent.text
            #check if the name has aliases
            aliases = [alias.text for alias in ent.ents if alias.label_ == 'PERSON' and alias.text != name]
            #add the name and aliases to the dictionary
            names_dict[name] = [name] + aliases 
    return names_dict

def cluster(names_dict):
    # Convert names and aliases into numerical format
    all_names = sum(names_dict.values(), [])  # Flatten the list of names and aliases
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(all_names)

    # Apply K-Means clustering
    num_clusters = 35  # 
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)

    #assign cluster labels to names and aliases
    cluster_labels = kmeans.labels_
    clustered_characters = {i: [] for i in range(num_clusters)}
    cluster_counts = {i: 0 for i in range(num_clusters)}  #initialize cluster counts

    for (name, aliases), cluster_label in zip(names_dict.items(), cluster_labels):
        clustered_characters[cluster_label].extend([name] + aliases)
        cluster_counts[cluster_label] += 1  #increment the count for the current cluster
    
    return cluster_counts, clustered_characters

def identify_main_characters(cluster_counts, threshold=30):
    main_characters = [char for char, count in cluster_counts.items() if count > threshold]

    return main_characters


def extract_entity_info(clustered_characters, book):
    '''creates a dictionary with all the character names and their aliases'''
    observations = {"main_characters": []}
    for c in clustered_characters:
        main_characters = {}
        all_names = clustered_characters[c]
        main_characters["name"] = all_names[0]
        main_characters["aliases"] = all_names[1:]
        
        occurrences = []
        for every_name in all_names:
            sentence_chapter_position = {}
            pattern = re.compile(r'((?:^|.*?[.!?])\s*(.*?(' + '|'.join(re.escape(every_name) for every_name in all_names) + r').*?[.!?]))')
            matches = [match.group(1) for match in pattern.finditer(book.text)]
            
            if matches:
                sentence_chapter_position["sentence"] = matches
                
            occurrences.append(sentence_chapter_position)
        
        main_characters["occurrences"] = occurrences
        observations["main_characters"].append(main_characters)
    
    return observations


def save_to_json(data, file_name):
    output_file_folder = os.getcwd()
    output_file_path = os.path.join(output_file_folder, file_name+"_NER.json")
    with open(output_file_path, "w", encoding ="utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent=4)
    print(f"Output saved to: {output_file_path}")


def main():
    #1) Load the book txt file
    folder_path = os.getcwd()
    file_name = input("Enter the file name (incl. .txt): ")
    file_path = os.path.join(folder_path, file_name)
    #r'C:\Users\babus\Documents\uni\HS23\PCL1\pcl1-course-project-master\Pride_and_Prejudice.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        book = file.read()
    doc = nlp(book)
    print("Starting the process! This will take a lot of time...(per our experience up to 10min)")

    #2) Perform NER and cluster in order to get a list of the main characters
    names_dict = perform_NER(doc)
    cluster_counts, clustered_characters = cluster(names_dict)
    main_characters = identify_main_characters(cluster_counts)
    print("main characters have been extracted...onto extracting more information about them")

    #3) Extract information from each character:
    observations = extract_entity_info(clustered_characters, doc)
    print("saving results in a json file now...")

    #4) Save results to a JSON file:
    save_to_json(observations, file_name.replace(".txt", ""))
    print("done!")




# Run the main function
if __name__ == "__main__":
    main()
