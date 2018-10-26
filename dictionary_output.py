
import json
from dictionary import create_dictionary


def output_json(directory):
    metrics = create_dictionary(directory)
    beats_list = list(metrics["beats"])
    metrics["beats"] = beats_list
    file_name = directory.split('/')[-1].split('.')[0]
    # print(file_name)
    with open(file_name+".json", "w") as output_file:
        json.dump(metrics, output_file, indent=4)


# if __name__ == '__main__':
#     output_json("insert directory here")
