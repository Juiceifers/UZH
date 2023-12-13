"""
PCL 1 Fall Semester 2023 - Course Project
Part 0: Book Selection (Pride & Prejudice, The Count of Monte Cristo, Alice in Wonderland)
Students: Ishana Rana, Sofia Benitez Navarro
"""

# --- Imports ---
import os
import re
import json
# --- Don't add other imports here ---


def json_conversion(data):
    """
    Create a function to convert the data to a json string here"""
    return json.dumps(data, indent =4) #formats the JSON with an indentation of four spaces.

def write_as_json(data, file_path):
    """
    Create a function to write your json string to a file here.
    Think about a naming convention for the output files.
    """
    with open(file_path, "w") as f:
        f.write(json_conversion(data))
        
def json_maker(text_files, output_dir):
    """
    processes the text files in the given directory (if it exists) and generates corresponding json files in the output directory
    """
    #directory creation (if needed)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
        
    #file filtering
    for f in os.listdir(text_files):
        if f.endswith("_ner.txt") or f.endswith("_sent.txt") :
            file_path = os.path.join(text_files, f)
            file_name = os.path.basename(file_path).replace(".txt", "") #extracts the name of the file woithout ".txt"
            output_path = os.path.join(output_dir, file_name+".json") #constructs the full path for the json file in output directory
            
            data = name_extraction(file_path)
            write_as_json(data, output_path)


def name_extraction(file_path):
    """
    extracts the named entities
    """
    with open(file_path, "r", encoding ="utf-8") as f:
        text = f.read()
        partition = text.split("Sentiment Expressions:")
        
        named_entities = partition[0].split("Named Entities:")[1]
        named_entities.strip()
        named_entities.split("\n")
    names = []
    for entity in named_entities: 
        entity = entity.strip()
        if entity:
            part = entity.split(" ", 1) #splitting the number from the name
            if len(part)==2 and part[0].isdigit(): #if it exists in this format, add it to the names list as a tuple
                names.append((part[0], part[1].strip()))
    
    return{"Named Enities": names}

def sentiment_extraction(file_path):
    """
    basically same built as name_extraction() but for sentiments
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        partition = text.split("Sentiment Expressions:")
        
        sentiments = partition[1].strip().split("\n")   
        sentiments_list = []
        for expr in sentiments:
            expr = expr.strip()
            if expr:
                part = expr.split(" ", 1)
                if len(expr)==2 and expr[0].isdigit():
                    sentiments_list.append(([part[0], part[1].strip()]))
                    
    return{"Sentiments Expressions": sentiments_list}

def main():
    text_files_sentiments = [r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Alice_in_WOnderland",
                            r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Pride_and_Prejudice",
                            r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\The_Count_of_Monte_Cristo"]
    
    output_dir_sentiments = [r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Alice_in_WOnderland\results",
                            r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Pride_and_Prejudice",
                            r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\The_Count_of_Monte_Cristo"]
    
    text_files_NER = [r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Alice_in_WOnderland",
                      r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Pride_and_Prejudice",
                      r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\The_Count_of_Monte_Cristo"]
    
    output_dir_NER = [r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Alice_in_WOnderland",
                      r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\Pride_and_Prejudice",
                      r"C:\Users\babus\OneDrive\Documents\uni uzh\compling\pcl\pcl1-course-project-master\The_Count_of_Monte_Cristo"]
    
    # Here you may add the neccessary code to call your functions, and all the steps before, in between, and after calling them.
    for i in range(len(text_files_sentiments)):
        json_maker(text_files_sentiments[i], output_dir_sentiments[i])
        json_maker(text_files_NER[i], output_dir_NER[i])
    print("all done!")

# This is the standard boilerplate that calls the main() function when the program is executed.
if __name__ == '__main__':
    main()
