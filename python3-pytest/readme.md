This directory shows a minimalist example of grading Python 3 code using Gradescope with pytest instead of the builtin unittest. 
Important ideas to pay attention to beyond the basic Gradescope scripting are:
1. One of the test cases uses pylint for PEP 8 code quality compliance.
2. The file **test_icm.py** conatins the actual test cases for this script.
3. JSON output from pytest depends on the Python module pytest-json. If you want to use another module, then you will likely have to change **pytest2gs.py** as well.

## Using pytest
Using pytest instead of unittest was pretty straightforward as far as making it work. The major changes required are:
1. importing pytest
2. supplying pytest unit test code in place of unittest test file(s)
3. changing the run_autograder script to call pytest with appropriate parameters.

## File pytest2gs
The file **pytest2gs.py** is a script I written to translate pytest-json JSON output to Gradescope-compliant JSON. 
It is a minimal example, and may not have all the items someone might want. However, it is key to integrating with Gradescope nicely.

pytest2gs takes file **report.json** as input and produces the target **results.json** file that is required for a compliant run_autograder script.
