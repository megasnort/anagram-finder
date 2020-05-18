import csv
import sys
import unidecode

def compare_string(string):
    string = unidecode.unidecode(string)

    remove_these_chars = ['\'', '"', ' ', '-', '.']
    string = ''.join(sorted(string.lower()))

    for c in remove_these_chars:
        string = string.replace(c, '')

    return string

def main():
    try:
        input_path = sys.argv[1]
    except (IndexError, IOError):
        print('Give a valid path to an input file.')
        exit(1)

    try:
        output_path = sys.argv[2]
    except (IndexError, IOError):
        print('Give a valid path to an output file.')
        exit(1)

    try:
        limit = int(sys.argv[3])
    except (IndexError, IOError):
        limit = 0

    streets = []
    
    with open(input_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if limit != 0 and line_count > limit:
                break
            else:
                if line_count == 0:
                    line_count += 1
                else:
                    streets.append((row[0], compare_string(row[0])))
                    line_count += 1


    anagrams = []

    with open(output_path, "w+") as fp:
        while len(streets) > 0:
            search = streets.pop(0)

            found_items = [street for street in streets if street[1] == search[1]]

            if len(found_items) > 0:
                found = [search, ] + found_items

                found_strings = [item[0] for item in found]

                write_string = str(len(found_strings)) + ' - ' + ', '.join(found_strings)

                print(write_string)
                
                fp.write(write_string + '\n')
                
                for found_item in found_items:
                    streets.remove(found_item)



    

if __name__ == '__main__':
    main()
