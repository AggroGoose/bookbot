def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        
        print(f"{len(words)} words found in the document")

        no_blanks = "".join(words).lower()
        char_dict = {}

        for c in no_blanks:
            if c.isalpha():
                if c not in char_dict:
                    char_dict[c] = 1
                else:
                    char_dict[c] += 1

        letter_array = []

        for key in char_dict:
            new_dict = {
                "letter": key,
                "count": char_dict[key]
            }
            letter_array.append(new_dict)

        def sort_on(dict):
            return dict["count"]

        letter_array.sort(reverse=True, key=sort_on)

        for letter in letter_array:
            print("The '" + letter['letter'] + "' " + f"character was found {letter['count']} times")


main()