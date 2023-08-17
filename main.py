import pytest
import logging
import subprocess

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(filename='logs/test.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Run tests and capture the console output for text result
    text_result_file = open('logs/result.txt', 'w')
    text_result_code = subprocess.call(["pytest", "tests/"], stdout=text_result_file, stderr=text_result_file)
    text_result_file.close()

    # Run tests and generate HTML report
    html_result_code = subprocess.call(["pytest", "tests/", "--html=logs/report.html"])

    if text_result_code == 0 and html_result_code == 0:
        logging.info("One or more tests failed.")
    else:
        logging.info("All tests passed.")

