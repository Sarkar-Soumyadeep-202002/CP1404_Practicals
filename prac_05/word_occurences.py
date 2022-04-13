"""
Name: Soumyadeep Sarkar
Description: Program to count the occurence of each word in a String.
"""


def frequency():
    """Display the frequency of each word in the text."""
    dict_frequency = {}
    longest_word = 0
    longest_count = 0
    text = input("Text: ")
    all_words = text.split()
    unique_words = []
    for word in all_words:
        if word not in unique_words:
            unique_words.append(word)
    unique_words.sort()
    for item in unique_words:
        if len(item) > longest_word:
            longest_word = len(item)
        if all_words.count(item) > longest_count:
            longest_count = all_words.count(item)
        dict_frequency[item] = all_words.count(item)

    for k, v in dict_frequency.items():
        print("{:{}} : {:{}}".format(k, longest_word, v, longest_count))


def main():
    """Start the program"""
    frequency()


main()
