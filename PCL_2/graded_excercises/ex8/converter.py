# Student Name: Ishana Rana
# Matriculation Number: 21-727-078

import ijson
import argparse
from lxml import etree as ET
from datetime import datetime
import random
import logging
from typing import Iterable
from os import sys
from memory_profiler import profile  


# ANSI color codes for text formatting in the main function
MAGENTA = "\033[35m"
RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[96m"

# Configure the logging system
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logger = logging.getLogger()

def create_parser():
    parser = argparse.ArgumentParser(prog='converter.py', description="Convert JSON reviews to XML by processing it sequentially")
    parser.add_argument('--json_file', type=str, help="JSON file name with the reviews", required=True)
    parser.add_argument('--xml_train', type=str, help="Output file for the train set in XML format.", required=True)
    parser.add_argument('--xml_test', type=str, help="Output file for the test set in XML format", required=True)
    parser.add_argument('-n', type=int, help="Reservoir size for the test set. These are the reviews that will be written to --xml_test", required=True)
    return parser.parse_args()

def check_weekend(date: str) -> bool:
    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date_obj.weekday() in (5, 6)

def convert_to_xml(review: dict) -> ET.Element:
    """Creates an XML representation of the input, which is a single review"""
    review_element = ET.Element("review")
    ET.SubElement(review_element, "review_id").text = review["review_id"]
    ET.SubElement(review_element, "user_id").text = review["user_id"]
    ET.SubElement(review_element, "business_id").text = review["business_id"]

    ratings = ET.SubElement(review_element, "ratings")
    ratings.set("stars", str(review["stars"]))
    ratings.set("useful", str(review["useful"]))
    ratings.set("funny", str(review["funny"]))
    ratings.set("cool", str(review["cool"]))

    ET.SubElement(review_element, "text").text = review["text"]

    date = datetime.strptime(review["date"], "%Y-%m-%d %H:%M:%S")
    date_element = ET.SubElement(review_element, "date")
    date_element.set("year", str(date.year))
    date_element.set("month", str(date.month))
    date_element.set("day", str(date.day))
    date_element.set("weekday", date.strftime("%A"))

    return review_element

def make_tree(xml_review, json_count, n, test_set, root_test, root_train):
    test_count = 0
    train_count = 0

    #reservoir sampling:
    if len(test_set) < n:
        test_set.append(xml_review)
        test_count += 1
    else:
        random_num = random.randint(0, json_count - 1)
        if random_num < n:
            root_train.append(test_set[random_num])
            test_set[random_num] = xml_review
        else:
            root_train.append(xml_review)
        train_count += 1
    
    return test_count, train_count

@profile
def convert(json_file: str, xml_test: str, xml_train: str, n: int) -> int:
    """Extracts the reviews that were made on the weekend and separates them into reservoir (test) and training sets and immediately adds the converted review (xml) to the corresponding xml tree."""
    json_count = 0
    test_count = 0
    train_count = 0
    root_test = ET.Element("root")
    root_train = ET.Element("root")
    test_set = []

    with open(json_file) as json, open(xml_test, "wb") as test, open(xml_train, "wb") as train:
        # parse the json file
        for x in ijson.items(json, "item"):
            json_count += 1
            if check_weekend(x["date"]):
                # convert valid json review to xml, do reservoir sampling and add that review to the corresponding root
                xml_review = convert_to_xml(x)
                t_count, tr_count = make_tree(xml_review, json_count, n, test_set, root_test, root_train)
                test_count += t_count
                train_count += tr_count

        # appending the remaining test_set to root_test outside the loop so there are no reoccurring elements
        for review in test_set:
            root_test.append(review)

        # build the tree
        tree_test = ET.ElementTree(root_test)
        tree_train = ET.ElementTree(root_train)

        # write the tree to the corresponding xml file
        tree_test.write(test, pretty_print=True, xml_declaration=True, encoding="utf-8")
        tree_train.write(train, pretty_print=True, xml_declaration=True, encoding="utf-8")
        
    return json_count, test_count, train_count

def main():
    args = create_parser()

    print("")
    print("INPUTS OVERVIEW:")
    print(f"Python Script Name: {GREEN}{sys.argv[0]}{RESET}")
    print(f"JSON File: {GREEN}{args.json_file}{RESET}")
    print(f"XML Train Output File Name: {GREEN}{args.xml_train}{RESET}")
    print(f"XML Test Output File Name: {GREEN}{args.xml_test}{RESET}")
    print(f"Reservoir Size: {GREEN}{args.n}{RESET}")
    print("")

    json_count, xml_test_count, xml_train_count = convert(args.json_file, args.xml_train, args.xml_test, args.n)
    
    print("OUTPUT OVERVIEW:")
    logging.info(f"{CYAN}Processed {json_count} reviews from file {args.json_file}{RESET}")
    logging.info(f"{CYAN}Written {xml_train_count} reviews to {args.xml_train}{RESET}")
    logging.info(f"{CYAN}Written {xml_test_count} reviews to {args.xml_test}{RESET}")
    print("\n")

if __name__ == '__main__':
    main()


