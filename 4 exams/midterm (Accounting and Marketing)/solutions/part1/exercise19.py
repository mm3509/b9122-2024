import exercise9
import os

# Note: because this file handles I/O, it does not have doc-tests.
def copy_and_process_file_contents(input_filepath, output_filepath):

    if not os.path.exists(input_filepath):
        raise ValueError("Input file does not exist")

    if os.path.exists(output_filepath):
        raise ValueError("Output file already exists")

    result = []
    with open(input_filepath) as f:
        for line in f.readlines():
            stripped = line.strip()
            treated = exercise9.get_consonants_lowercase(stripped)
            result.append(treated)

    with open(output_filepath, "w+") as f:
        f.write("\n".join(result))
