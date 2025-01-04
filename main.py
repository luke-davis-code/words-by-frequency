import pymupdf, re

def pdf_to_string(pdf_path):
    document = pymupdf.open(pdf_path)
    # Create string output
    all_text = ""
    for page in document:
        all_text += page.get_text("text")
    return all_text

def get_string_words(inp_string):
    # First remove punctuation
    clean_string = re.sub(r"[^\w\s]","",inp_string)
    # Remove newlines
    clean_string = clean_string.replace("\n", "")
    # Set all to lowercase
    clean_string = clean_string.lower()
    # Now split into words
    words = clean_string.split(" ")
    return words

def get_freq_words(words, words_to_check):
    # Get the frequency of words given
    frequencies = {}
    for w in words_to_check:
        frequency = words.count(w)
        frequencies[w] = frequency

    return frequencies

def freq_list_to_txt(list_frequencies):
    with open("output.txt", "w") as text_file:
        for key, value in list_frequencies:
            text_file.write(key + ": " + str(value) + "\n")
    print("SUCCESS: Word counts saved to output.txt")

def get_input_words(input_word_file):
    words_to_check = []
    with open(input_word_file, "r") as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            words_to_check.append(line)
    return words_to_check

def sort_dict(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    pdf_filename = "example.pdf"
    input_word_file = "input.txt"
    words_to_check = get_input_words(input_word_file)
    text = pdf_to_string(pdf_filename)
    words = get_string_words(text)
    frequencies = get_freq_words(words, words_to_check)
    frequencies_sorted = sort_dict(frequencies)
    freq_list_to_txt(frequencies_sorted)