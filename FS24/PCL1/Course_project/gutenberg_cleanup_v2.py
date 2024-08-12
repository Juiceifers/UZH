##############################################################################################################
##############################################################################################################
##### DO NOT MODIFY THIS CODE #####
# This code is to be used as is.

import os
import sys
import re

# Markers for the start and end of Project Gutenberg headers/footers
TEXT_START_MARKERS = frozenset((
    "*END*THE SMALL PRINT",
    "*** START OF THE PROJECT GUTENBERG",
    "*** START OF THIS PROJECT GUTENBERG",
    "This etext was prepared by",
    "E-text prepared by",
    "Produced by",
    "Distributed Proofreading Team",
    "Proofreading Team at http://www.pgdp.net",
    "http://gallica.bnf.fr)",
    "      http://archive.org/details/",
    "http://www.pgdp.net",
    "by The Internet Archive)",
    "by The Internet Archive/Canadian Libraries",
    "by The Internet Archive/American Libraries",
    "public domain material from the Internet Archive",
    "Internet Archive)",
    "Internet Archive/Canadian Libraries",
    "Internet Archive/American Libraries",
    "material from the Google Print project",
    "*END THE SMALL PRINT",
    "***START OF THE PROJECT GUTENBERG",
    "This etext was produced by",
    "*** START OF THE COPYRIGHTED",
    "The Project Gutenberg",
    "http://gutenberg.spiegel.de/ erreichbar.",
    "Project Runeberg publishes",
    "Beginning of this Project Gutenberg",
    "Project Gutenberg Online Distributed",
    "Gutenberg Online Distributed",
    "the Project Gutenberg Online Distributed",
    "Project Gutenberg TEI",
    "This eBook was prepared by",
    "http://gutenberg2000.de erreichbar.",
    "This Etext was prepared by",
    "This Project Gutenberg Etext was prepared by",
    "Gutenberg Distributed Proofreaders",
    "Project Gutenberg Distributed Proofreaders",
    "the Project Gutenberg Online Distributed Proofreading Team",
    "**The Project Gutenberg",
    "*SMALL PRINT!",
    "More information about this book is at the top of this file.",
    "tells you about restrictions in how the file may be used.",
    "l'authorization à les utilizer pour preparer ce texte.",
    "of the etext through OCR.",
    "*****These eBooks Were Prepared By Thousands of Volunteers!*****",
    "We need your donations more than ever!",
    " *** START OF THIS PROJECT GUTENBERG",
    "****     SMALL PRINT!",
    '["Small Print" V.',
    '      (http://www.ibiblio.org/gutenberg/',
    'and the Project Gutenberg Online Distributed Proofreading Team',
    'Mary Meehan, and the Project Gutenberg Online Distributed Proofreading',
    '                this Project Gutenberg edition.',
))


TEXT_END_MARKERS = frozenset((
    "*** END OF THE PROJECT GUTENBERG",
    "*** END OF THIS PROJECT GUTENBERG",
    "***END OF THE PROJECT GUTENBERG",
    "End of the Project Gutenberg",
    "End of The Project Gutenberg",
    "Ende dieses Project Gutenberg",
    "by Project Gutenberg",
    "End of Project Gutenberg",
    "End of this Project Gutenberg",
    "Ende dieses Projekt Gutenberg",
    "        ***END OF THE PROJECT GUTENBERG",
    "*** END OF THE COPYRIGHTED",
    "End of this is COPYRIGHTED",
    "Ende dieses Etextes ",
    "Ende dieses Project Gutenber",
    "Ende diese Project Gutenberg",
    "**This is a COPYRIGHTED Project Gutenberg Etext, Details Above**",
    "Fin de Project Gutenberg",
    "The Project Gutenberg Etext of ",
    "Ce document fut presente en lecture",
    "Ce document fut présenté en lecture",
    "More information about this book is at the top of this file.",
    "We need your donations more than ever!",
    "END OF PROJECT GUTENBERG",
    " End of the Project Gutenberg",
    " *** END OF THIS PROJECT GUTENBERG",
))


LEGALESE_START_MARKERS = frozenset(("<<THIS ELECTRONIC VERSION OF",))


LEGALESE_END_MARKERS = frozenset(("SERVICE THAT CHARGES FOR DOWNLOAD",))

def strip_headers(text):
    """Remove lines that are part of the Project Gutenberg header or footer."""
    lines = text.splitlines()
    sep = str(os.linesep)

    out = []
    i = 0
    footer_found = False
    ignore_section = False

    for line in lines:
        reset = False

        # Header removal
        if i <= 600 and any(line.startswith(token) for token in TEXT_START_MARKERS):
            reset = True

        if reset:
            out = []
            continue

        # Footer detection
        if i >= 100 and any(line.startswith(token) for token in TEXT_END_MARKERS):
            footer_found = True

        if footer_found:
            break

        # Legalese removal
        if any(line.startswith(token) for token in LEGALESE_START_MARKERS):
            ignore_section = True
            continue
        elif any(line.startswith(token) for token in LEGALESE_END_MARKERS):
            ignore_section = False
            continue

        if not ignore_section:
            out.append(line.rstrip(sep))
            i += 1

    return sep.join(out)

##############################################################################################################
##############################################################################################################

#### MODIFY HERE ####

def split_book_by_chapter(cleaned_text, book_title):
    """
    Implement a function that splits the book into chapters and saves 
    each chapter in a separate file in a folder named after the book title.
    """
    # Add your code here to split the cleaned_text into chapters
    # and save each chapter in a separate file
    chapters = cleaned_text.split("CHAPTER")  # Assuming chapters are marked by "CHAPTER"
    
    # Create a folder for the chapters
    chapters_folder = os.path.join(book_title, 'chapters')
    os.makedirs(chapters_folder, exist_ok=True)

    # Save each chapter in a separate file
    for i, chapter in enumerate(chapters):
        chapter_title = f"Chapter_{i + 1}.txt"
        chapter_path = os.path.join(chapters_folder, chapter_title)
        with open(chapter_path, 'w', encoding='utf-8') as chapter_file:
            chapter_file.write(chapter.strip())
    print("done splitting!")


def main():
    # 1) check correct input
    if len(sys.argv) != 2: #2 because argv[0] is the call to programm and argv[1] is the file path
        print("Incorrect input!")
        print("Usage: python gutenberg_cleanup.py <name of book file inlc. .txt> (.txt has to be in the same folder as the python script)")
        exit(1) #1 to indicate that the program did not execute sucessfully
        

    # 2) extract information
    file_path = os.path.abspath(sys.argv[1])
    book_title = os.path.basename(file_path).replace('.txt', '') 
    directory = os.path.join(os.path.dirname(file_path), book_title)
    directory_clean = os.path.join(directory, book_title+"_cleaned.txt") 
    
    # 3) Read the text file
    with open(file_path, "r", encoding = "utf-8") as f:
        text = f.read()

    # 4) Clean the text
        text_cleaned = strip_headers(text)

    # 5) Save the cleaned text in the book title folder
        # make folders 
        os.makedirs(directory, exist_ok=True) #folder with the book title
        #os.makedirs(os.path.join(directory, "Chapters"))
        text_cleaned_path = os.path.join(directory, f'{book_title}_cleaned.txt')
        #with open(directory_clean, "w") as dir:
            #dir.write(text_cleaned)
        with open(text_cleaned_path, 'w', encoding='utf-8') as f:
            f.write(text_cleaned)

    # 6) Split the text into chapters and save them in the book title folder under a subfolder named 'chapters'
    split_book_by_chapter(text_cleaned, directory)

if __name__ == '__main__':
    main()
    
