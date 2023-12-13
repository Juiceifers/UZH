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
    return json.dumps(data, indent =4)

def write_as_json(data, file_path):
    """
    Create a function to write your json string to a file here.
    Think about a naming convention for the output files.
    """
    with open(file_path, "w") as f:
        f.write(json_conversion(data))
        
def json_maker(text_files, output_dir, indicator):
    """
    processes the text files in the given directory (if it exists) and generates corresponding json files with NER info in the output directory
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
            
            if indicator == "senti": 
                data = extraction(file_path, "senti")
                write_as_json(data, output_path)
            else:
                data = extraction(file_path, "NER")
                write_as_json(data, output_path)


def extraction(file_path, indicator):
    """
    extracts the named entities or sentiments depending on the indicator
    """
    with open(file_path, "r", encoding ="utf-8") as f:
        text = f.read()
        partition = text.split("Sentiment Expressions:")
        if indicator == "NER":
            # 1) info prep for NER
            part_ner = partition[0].split("Named Entities:") #creates a list with 2 elements: 1st element = "Named Entities", 2nd element = content after "Named Entities"
            named_entities = part_ner[1] #1 bc thats the half with all the content after "Named Entities"
            named_entities.strip()
            named_entities.split("\n")
            # 2) make the list
            names = []
            for entity in named_entities: 
                entity = entity.strip()
                if entity:
                    ner = entity.split(" ", 1) #splitting the number from the name
                    if len(ner)==2 and ner[0].isdigit(): #if it exists in this format, add it to the names list as a tuple
                        names.append((ner[0], ner[1].strip()))
            return{"Named Enities": names}

        else:
            # 1) info prep for senti
            part_senti = partition[1].split("Sentiment Expressions:") #creates a list with 2 elements: 1st element = "Sentiment Expressions", 2nd element = content after "Sentiment Expressions"
            sentiments = part_senti[1].strip().split("\n")   
            sentiments_list = []
            # 2) make the list with the sentiments
            for expr in sentiments:
                expr = expr.strip()
                if expr:
                    senti = expr.split(" ", 1)
                    if len(senti)==2 and senti[0].isdigit():
                        sentiments_list.append(([senti[0], senti[1].strip()]))
                        
            return{"Sentiments Expressions": sentiments_list}

def main():
    """
    get the amount of books to make a loop to get the corresponding paths for the functions above
    """
    
    try:
        amount = int(input("Enter the amount of books to be analyzed: "))
    except:
        print("Pls enter a number!")
        exit(1)
    if amount <= 0:
        print("Please enter a positive number!")
        exit(1)
  
    for i in range(0, amount):
        book_title = input("Enter the name of the book: ")
        try:
            input_path_sentiments = str(input(f"Enter the file path for book '{book_title}' with the folder containing the sentiment files to be transformed:  "))
            output_path_sentiments = str(input(f"Enter the file path for book '{book_title}' with the folder for the output of sentiments files:  "))
            json_maker(input_path_sentiments, output_path_sentiments, "senti")
            input_path_NER = str(input(f"Enter the file path for book '{book_title}' with the folder containing the NER files to be transformed:  "))
            output_path_NER= str(input(f"Enter the file path for book '{book_title}' with the folder for the output of NER files:  "))
            json_maker(input_path_NER, output_path_NER, "NER")
            print("all done!")
        except:
            print("Incorrect input - something went wrong in the main function")
            exit(1)
    

# This is the standard boilerplate that calls the main() function when the program is executed.
if __name__ == '__main__':
    main()
