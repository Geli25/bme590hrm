import json
from dictionary import create_dictionary


def output_json(directory):
    metrics = create_dictionary(directory)
    beats_list = list(metrics["beats"])
    metrics["beats"] = beats_list
    file_name = directory[10:][:-4]
    with open(file_name+".json", "w") as output_file:
        json.dump(metrics, output_file, indent=4)
