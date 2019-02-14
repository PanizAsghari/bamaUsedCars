from dataExtraction.extractions import extractor

def preparation():
    file_path = r"C:\Users\parsitech\Documents\ScrapyAttempt\crawler\bama\crawled.txt"
    with open(file_path, "r") as myfile:
        for line in myfile:
            print(line)
            extractor(line)

preparation()