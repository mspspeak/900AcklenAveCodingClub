

def is_door_five_open_or(character):
    return (character == '0' or 
        character == '1' or
        character == '2' or
        character == '3' or
        character == '4' or
        character == '5' or
        character == '6' or
        character == '7' or
        character == '8' or
        character == '9' or
        character == 'P' or
        character == 'Q' or
        character == 'R' or
        character == 'S' or
        character == 'T' or
        character == 'U' or
        character == 'V' or
        character == 'W' or
        character == 'X' or
        character == 'Y' or
        character == 'Z' or
        character == 'p' or
        character == 'q' or
        character == 'r' or
        character == 'w' or
        character == 't' or
        character == 'u' or
        character == 'v' or
        character == 'w' or
        character == 'x' or
        character == 'y' or
        character == 'z' or
        character == ':' or
        character == ';' or
        character == '?')


def is_door_five_open_for_list(character):    
    list_of_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'p', 'q', 'r', 'w', 't', 'u', 'v', 'w', 'x', 'y', 'z', ':', ';', '?']
    
    for list_character in list_of_characters:
        if character == list_character:
            return True
    
    return False


def is_door_five_open_in_list(character):
    list_of_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'p', 'q', 'r', 'w', 't', 'u', 'v', 'w', 'x', 'y', 'z', ':', ';', '?']
    return character in list_of_characters


def is_door_five_open_binary_math(character):
    number = ord(character)
    fifth_bit = ((0 * 1) +   #1s
        (0 * 2) +            #2s 
        (0 * 4) +            #4s
        (0 * 8) +            #8s
        (1 * 16) +           #16s
        (0 * 32) +           #32s
        (0 * 64) +           #64s
        (0 * 128))           #128s            
    return (number & fifth_bit) == fifth_bit


def get_file_contents(file_name):
    f = open(file_name, "r")
    contents = f.read()
    return contents

def if_found_print_sequence(contents_of_file, test_function, escape_sequence):
    for character in contents_of_file:
        if test_function(character):
            print(escape_sequence)


file_name = "./DoorFile-Door-six-and-five-open.txt"
escape_sequence = "8AR7W98"
if_found_print_sequence(get_file_contents(file_name), is_door_five_open_binary_math, escape_sequence)
