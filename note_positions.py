import argparse
import sys

# Define a dictionary to map note names to positions in the chromatic scale
note_positions = {
    'A': 0, 'A#': 1, 'Bb': 1, 'B': 2, 'C': 3, 'C#': 4,
    'Db': 4, 'D': 5, 'D#': 6, 'Eb': 6, 'E': 7, 'F': 8,
    'F#': 9, 'Gb': 9, 'G': 10, 'G#': 11, 'Ab': 11
}

def get_fret(target, string):
    """
    Finds the fret that will produce a given note on a given string.

    Args:
        target (str): the note whose position is to be determined.
        string (str): the note of the open string.

    Returns:
        int: the fret that will produce the target note on the specified
        string (0 represents the open string).
    """
    target_position = note_positions[target]
    string_position = note_positions[string]
    fret = (target_position - string_position) % 12
    return fret

def get_frets(target, strings):
    """
    Given a list of strings, finds the fret on each string that will
    produce a given note.

    Args:
        target (str): the note whose position is to be determined.
        strings (list of str): a list of the notes of open strings.

    Returns:
        dict of (str: int): a dictionary whose keys are the string names
        specified in the strings parameter and whose values are fret
        positions on those strings.
    """
    frets = {}
    for string in strings:
        fret = get_fret(target, string)
        frets[string] = fret
    return frets

def parse_args(arglist):
    """
    Parses command-line arguments.

    The following required command-line arguments are defined:

    target: the note whose position the user wants to find
    strings: a list of one or more notes of open strings for which the
        user wishes to find the position of the target note

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables target and strings.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="the note whose position is to be determined")
    parser.add_argument("strings", nargs="+", help="a list of open string notes")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    frets = get_frets(args.target, args.strings)
    
    for string, fret in frets.items():
        print(f"{args.target} is fret {fret} of the {string} string")
