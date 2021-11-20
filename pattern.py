#!/bin/python3


import string
import argparse


MAX_LEN = 20280     # 26upper_alphabets * 26lower_alphabets * 10digits * 3length_of_every_pattern_unit


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", dest="action", help="generate or search")
    parser.add_argument("-p", "--parameter", dest="parameter", help="Pattern Length to Generate or Pattern String to Search.")
    arguments = parser.parse_args()
    if not arguments.action:
        parser.error("[-] Please specify Action to Generate or Search a Pattern.")
    elif not arguments.parameter:
        parser.error("[-] Please specify Parameter as Length to Generate or String to Search.")
    else:
        return arguments


def pattern_generate(length):
    if length > MAX_LEN:
        return f"[-] Length cannot be more than {MAX_LEN}."
    else:
        pattern = ""
        for upper in string.ascii_uppercase:
            for lower in string.ascii_lowercase:
                for digit in string.digits:
                    if len(pattern) < length:
                        pattern += upper + lower + digit
                    else:
                        pattern = pattern[:length]
                        return pattern


def pattern_search(search_string):
    search_length = len(search_string)
    index = 0
    pattern = ""
    for upper in string.ascii_uppercase:
        for lower in string.ascii_lowercase:
            for digit in string.digits:
                pattern += upper + lower + digit
                index = pattern.find(search_string)
                if index != -1:
                    return f"[+] Pattern found at Index = {index}"
    return "[-] Pattern not found."


arguments = get_arguments()

if arguments.action.lower() == "generate":
    length = int(arguments.parameter)
    pattern = pattern_generate(length)
    print(pattern)
elif arguments.action.lower() == "search" and type(search_string := arguments.parameter) == str:
    index = pattern_search(search_string)
    print(index)
else:
    print("[-] Please check the entered 'Action' or 'Parameter'")

