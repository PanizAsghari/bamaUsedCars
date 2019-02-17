import urllib.request
import csv
import http

def write_to_csv(atts_list):
    with open("details.csv", 'wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(atts_list)


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")




def open_page(web_url):
    try:
        with urllib.request.urlopen(web_url) as url:
            content = url.read()
        return content
    except http.client.IncompleteRead:
        print("http exception")
        return "Exception occured"

def write_list_to_csv(list):
    with open("car_details.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        try:
            wr.writerow(list)
        except UnicodeEncodeError:
            print("unicode error. there was a problem with your set encoding")
            list[9]=17
            print(list)
            wr.writerow(list)
            return



