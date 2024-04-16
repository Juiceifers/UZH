from levenshtein_base import levenshtein
import argparse
import spacy
nlp = spacy.load('en_core_web_sm')


# Student Name: Ishana Rana
# Matriculation Number: 21-727-078

#Task 1
def create_parser():
    parser = argparse.ArgumentParser(prog='Levenshtein_cli.py', description="To calculate Levenshtein distance between two files.")
    
    # Required arguments
    parser.add_argument('--file1', type=str, help="Path to the first file.", required=True)
    parser.add_argument('--file2', type=str, help="Path to the second file.", required=True)
    # Optional arguments
    parser.add_argument('--insertion', type=int, help="Weight of the insertion operation. Default is 1.", default=1)
    parser.add_argument('--deletion', type=int, help="Weight of the deletion operation. Default is 1.", default=1)
    parser.add_argument('--substitution', type=int, help="Weight of the substitution operation. Default is 1.", default=1)
    # Flag
    parser.add_argument('--tokenize', action='store_true', help="If called with this flag the Levenshtein distance will be calculated on a token level, instead of character.")
    
    return parser.parse_args()

def tokenize(text:str)->list:
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_punct or token.text == "'"]
    return tokens

def main():
    args = create_parser()
    print("")
    print("INPUTS OVERVIEW:")
    print(f"\t File 1: {args.file1}")
    print(f"\t File 2: {args.file2}")
    print(f"\t Insertion Weight: {args.insertion}")
    print(f"\t Deletion Weight: {args.deletion}")
    print(f"\t Substitution Weight: {args.substitution}")
    print(f"\t Tokenize: {args.tokenize}")
    print("")
    
    print("OUTPUT:")
    # 1) save the content from files
    with open(args.file1, 'r') as f1:
        s1 = f1.read()
    with open(args.file2, 'r') as f2:
        s2 = f2.read()
        
    # 2) differentiate btw tokenwise/characterwise    
    if not args.tokenize: 
        distance = levenshtein(s1, s2, args.insertion, args.deletion, args.substitution)
    else:
        s1 = tokenize(s1)
        s2 = tokenize(s2) 
        distance = levenshtein(s1, s2, args.insertion, args.deletion, args.substitution)

    # 3) Print result
    print(f"\t The levenshtein distance is = {distance}")
    print("")
    
    
    

if __name__ == "__main__":
    main()
    
# usage example (for windows):
# python levenshtein_cli.py --file1 samples/library_1.txt --file2 samples/library_2.txt --insertion 1 --deletion 1 --substitution 1
# python levenshtein_cli.py --file1 samples/text_1.txt --file2 samples/text_2.txt --insertion 1 --deletion 1 --substitution 1

