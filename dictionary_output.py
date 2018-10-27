import json
from dictionary import create_dictionary


def output_json(directory):
    """This function outputs a json file from "metrics" dictionary.

    The function creates a json file under the same name as the input file,
    determined through the directory (string). It get the string value
    between the last occurring '/' and the first occurring '.', and appends
    ".json" after the returned string, creating the file name. It then
    writes the json data into that file and formats the data in a readable
    way (prettifying the dictionary, basically). Can be used as __main__.

    Args:
        directory(string): Path to the file in a string format.

    Returns:
        .json: A json file containing all dictionary data.
    """
    metrics = create_dictionary(directory)
    beats_list = list(metrics["beats"])
    metrics["beats"] = beats_list
    file_name = directory.split('/')[-1].split('.')[0]
    # print(file_name)
    with open(file_name+".json", "w") as output_file:
        json.dump(metrics, output_file, indent=4)


# if __name__ == '__main__':
#     output_json("insert directory here")
