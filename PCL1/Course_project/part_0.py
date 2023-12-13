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
        book_title = input("Enter the name of the book")
        try:
            input_path_sentiments = str(input(f"Enter the file path for book '{book_title}' with the folder containing the sentiment files to be transformed:  "))
            output_path_sentiments = str(input(f"Enter the file path for book '{book_title}' with the folder for the output of sentiments files:  "))
            json_maker(input_path_sentiments, output_path_sentiments)
            input_path_NER = str(input(f"Enter the file path for book '{book_title}' with the folder containing the NER files to be transformed:  "))
            output_path_NER= str(input(f"Enter the file path for book '{book_title}' with the folder for the output of NER files:  "))
            json_maker(input_path_NER, output_path_NER)
            print("all done!")
        except:
            print("Incorrect input")
            exit(1)


# This is the standard boilerplate that calls the main() function when the program is executed.
if __name__ == '__main__':
    main()
