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

def dict_to_txt(dictionary):
    with open("output.txt", "w") as text_file:
        for key, value in dictionary.items():
            text_file.write(str(key) + ": " + str(value) + "\n")
    print("SUCCESS: Word counts saved to output.txt")


if __name__ == "__main__":
    filename = "example.pdf"
    words_to_check = ("frodo", "samwise", "gandalf", "aragorn", "legolas", "gimli", "boromir", "pippin", "merry",
                      "elrond", "galadriel", "arwen", "eomer", "eowyn", "theoden", "saruman", "sauron", "gollum",
                      "treebeard", "faramir", "denethor", "bilbo", "shadowfax", "shelob", "grima")
    text = pdf_to_string(filename)
    words = get_string_words(text)
    frequencies = get_freq_words(words, words_to_check)
    dict_to_txt(frequencies)



