from levenshtein_base import levenshtein
from levenshtein_cli import create_parser, main, tokenize




def test_equal_weights():
    s1 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'library', 'stood', 'as', 'a', 'center', 'of', 'learning', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'of', 'the', 'past', 'to', 'those', 'who', 'listened', 'closely'] 
    s2 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'ancient', 'library', 'stood', 'as', 'a', 'beacon', 'of', 'knowledge', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'from', 'the', 'past', 'to', 'those', 'who', 'listened']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=1)
    assert distance == 5

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 33


def test_expensive_substitution():
    s1 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'library', 'stood', 'as', 'a', 'center', 'of', 'learning', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'of', 'the', 'past', 'to', 'those', 'who', 'listened', 'closely'] 
    s2 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'ancient', 'library', 'stood', 'as', 'a', 'beacon', 'of', 'knowledge', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'from', 'the', 'past', 'to', 'those', 'who', 'listened']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=12)
    assert distance == 8

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=12)
    assert distance == 40


def test_cheap_substitution():
    s1 = "Today, we're excited to launch our latest feature, designed to enhance user experience across our platform."
    s2 = "Today, we are excited to announce our latest feature, aimed at enhancing the user experience across the platform."

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=0.5)
    assert distance == 17

    s1 = ['Today', "we're", 'excited', 'to', 'launch', 'our', 'latest', 'feature', 'designed', 'to', 'enhance', 'user', 'experience', 'across', 'our', 'platform'] 
    s2 = ['Today', 'we', 'are', 'excited', 'to', 'announce', 'our', 'latest', 'feature', 'aimed', 'at', 'enhancing', 'the', 'user', 'experience', 'across', 'the', 'platform']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=0.5)
    assert distance == 5
    
def test_same_input():
    s1 = "Hello, my name is Ishana"
    s2 = "Hello, my name is Ishana"
    distance= levenshtein(s1,s2)
    assert distance == 0
    
    s1 = ["Hello", "my", "name", "is", "Ishana"]
    s2 = ["Hello", "my", "name", "is", "Ishana"]
    distance= levenshtein(s1,s2)
    assert distance == 0
    

def test_empty_input():
    s1 = ""
    s2 = ""
    distance= levenshtein(s1,s2)
    assert distance == 0
    
    s1 = []
    s2 = []
    distance= levenshtein(s1,s2)
    assert distance == 0
    

def test_token_level():
    s1 = "How are you?"
    s2 = "How you are?"
    distance = levenshtein(s1, s2,insertion_cost=1,
                           deletion_cost=1, substitution_cost=1, --tokenize)
    assert distance == 1

    
def test_case_sensitivity():
    s1 = "Hello"
    s2 = "hello"
    distance = levenshtein(s1, s2)
    assert distance ==1
    
def test_unicode_strings():
    s1 = "😀🌍🌟"
    s2 = "😃🌍✨"
    distance = levenshtein(s1, s2)
    assert distance == 2
    
def test_one_empty_string():
    s1 = "abc"
    s2 = ""
    distance = levenshtein(s1, s2)
    assert distance == 3
    
def test_tokenize_function():
    text = "This is a test string for tokenization. It includes punctuations!"
    expected = ["This", "is", "a", "test", "string", "for", "tokenization", "It", "includes", "punctuations"]
    assert tokenize(text) == expected

def test_error_handling():
    pass



"""
# was not able to finish writing tests for the cli 
def test_cli():
    argv = [
        '--file1', 'samples/library_1.txt',
        '--file2', 'samples/library_2.txt',
        '--insertion', '1',
        '--deletion', '1',
        '--substitution', '1'
    ]
    args = create_parser().parse_args(argv)
    assert args.file1 == 'samples/library_1.txt'
    assert args.file2 == 'samples/library_2.txt'
    assert args.insertion == 1
    assert args.deletion == 1
    assert args.substitution == 1
    assert args.tokenize == False
"""
     