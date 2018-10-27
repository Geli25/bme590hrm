# Heart Rate Monitor

[![Build Status](https://travis-ci.org/Geli25/bme590hrm.svg?branch=master)](https://travis-ci.org/Geli25/bme590hrm)

By Angelina Liu

BME590

***To run this project, change the dictionary_output.py into main, uncomment the last few lines,
and input the file directory as a string. (Takes one file at a time, no iteration(yet))***

### Files for this project:

- **read_data.py**: Imports the data into a pandas dataframe.

- **validate_data.py**: Removes invalid data rows from dataframe and 
converts all data into floats format instead of strings. 

- **find_min_max.py**: Finds the extreme voltages by passing in the dataframe.
Outputs a tuple: first number min, second number max.

- **get_duration.py**: Finds the duration of the ECG strip by getting the last
recorded time in the dataframe as well as the first and calculate the difference.

- **find_peaks.py**: Finds the peak in the voltage data of the ECG strip
using scipy.find_peak(), returns an array of peak voltages as well as the number of peaks detected. Not accurate at all. Scipy.find_peaks() also causes import
problems on my local device (not on travis or anywhere else).

- **get_beat_times.py**: Finds the beat time using the peak voltages from **find_peaks.py**. Returns a
numpy array with all peak times.

- **calculate_mean_bpm.py**: Calculates the mean bpm in a time frame specified by user, has default values.

- **dictionary.py**: Executes all calculations (all function files written above
 are imported and run within this function) and returns a dictionary "metrics" with required
 key value pairs. Therefore the argument passed in is the directory in string format.
 
 - **dictionary_output.py**: Runs **dictionary.py** and outputs a .json file under the same
 name as the input file. Since I need to get the file name from the directory (which is from using **read_data.py**)
, I would need to run **dictionary.py** to ensure that the file path is correct so that we would know
the file name is also correct. Dictionary data is written onto that .json file. Since all functions are included
in this file, simply change the file name to main and uncomment the last few lines.

- **test_hrm.py**: All unit tests for all of the above files are on here.
    * *test_import_data, test_validate_data* : Checks the functionality of the test by
    counting rows within the dataframe.
    * *test_find_min_max* : Checks the value of the returned tuple.
    * *test_find_peak*: Checks the number of peaks (second returned value) only.
    * *test_get_duration*: Checks the value of the duration.
    * *test_get_beat_time*: Checks the first and last value of the numpy array.
    * *test_calculate_mean_bpm*:  Checks the returned bpm while specifiying time frame in parametrize.
    * *test_dictionary*: Checks the bpm value and min_max value. (Since all other values are used to calculate the bpm, if those values are not correct
    then the bpm value should also be wrong, therefore causing the test to fail regardless, so no need to check for those values.)
    * *test_dictionary_output*: Checks if the .json file exists in the directory via a boolean.
    
### Personal Thoughts/Comments:
* I really messed up on the first couple of branches: forgetting to commit to certain branches, pushes to master directly, merging 
when I should have been pulling. But after that I got a better sence of how it worked.

* I need to incorporate more error throwing for invalid user input. Right now I
am only using if statements. Will update by Sunday.

* I really hate PEP8 but I guess it's necessary for unify formats.

* Sphinx is really glitchy.

* May also be good to implement iteration and run the program for all files in a folder.