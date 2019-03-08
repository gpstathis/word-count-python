import sys
import re 

def increment_count(dict, key):
    """Increments the associated key value in a dictionary where keys are strings 
    and values are integer counts.

    Arguments:\n
    dict -- a dictionary of string (key), count (value) pairs\n
    key -- the key whose count should be incremented\n
    """
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

def get_top_n(dict, n):
    """Returns a list of the `n` tuples with the largest values in the dictionary, 
    sorted in descending order.

    Arguments:\n
    dict -- a dictionary of string (key), count (value) pairs\n
    n -- the number of largest counts (values)\n
    """
    return sorted(dict.items(), key=lambda kv: kv[1], reverse = True)[:n]

def print_counts(items):
    """Prints the name and count of a (name,count) tuple"""
    for i in items:
        print("{} - {}".format(i[1], i[0]))

def main():
    data_file_path = 'test-data.txt'
    name_pattern = re.compile('([\w]+), ([\w]+).*')
    first_names = {}
    last_names = {}
    full_names = {}
    modified_first_names = []
    modified_last_names = []
    top_N = 10
    modified_N = 25

    if len(sys.argv) > 1:
        data_file_path = sys.argv[1]

    if len(sys.argv) > 2:
        top_N = int(sys.argv[2])

    if len(sys.argv) > 3:
        modified_N = int(sys.argv[3])

    with open(data_file_path) as f:
        for line in f:
            m = name_pattern.match(line)
            if m != None:
                if (len(modified_first_names) < modified_N and
                    m.group(2) not in first_names and
                    m.group(1) not in last_names
                    ):
                    modified_first_names.append(m.group(2))
                    modified_last_names.append(m.group(1))
                increment_count(first_names, m.group(2))
                increment_count(last_names, m.group(1))
                increment_count(full_names, "{0} {1}".format(m.group(1), m.group(2)))

    print("Unique first names: {}".format(len(first_names)))
    print("Unique last names: {}".format(len(last_names)))
    print("Unique full names: {}".format(len(full_names)))
    print("\n")
    print("Top {} first names:".format(top_N))
    print_counts(get_top_n(first_names, top_N))
    print("\n")
    print("Top {} last names:".format(top_N))
    print_counts(get_top_n(last_names, top_N))
    print("\n")
    print("Pre-modified name list:")
    for first, last in zip(modified_first_names, modified_last_names):
        print("{} {}".format(first, last))
    print("\n")
    print("Modified name list:")
    for first, last in zip(modified_first_names, reversed(modified_last_names)):
        print("{} {}".format(first, last))

    return 0

if __name__ == '__main__':
    sys.exit(main())    