import pymupdf, string

def pdf_to_string(pdf_path):
    document = pymupdf.open(pdf_path)
    # Create string output
    all_text = ""
    for page in document:
        all_text += page.get_text("text")
    return all_text

def get_string_words(inp_string):
    # First remove punctuation
    for char in string.punctuation:
        clean_string = inp_string.replace(char, "")
    # Remove newlines
    clean_string = clean_string.replace("\n", "")
    # Now split into words
    words = clean_string.split(" ")
    return words


text = pdf_to_string("example.pdf")
get_string_words(text)


