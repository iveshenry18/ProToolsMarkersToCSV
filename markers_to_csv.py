import pandas as pd
import sys
import re

def parse_markers(text):
    """
    Parses the markers from the provided text content.
    
    Args:
    text (str): Text content of the file containing markers.

    Returns:
    list of tuples: Parsed marker data.
    """
    # Split the text into lines
    lines = text.strip().split('\n')

    # Extract the lines after the "MARKERS LISTING" line
    markers_start_index = next(i for i, line in enumerate(lines) if "M A R K E R S  L I S T I N G" in line)
    marker_lines = lines[markers_start_index + 2:]  # Skipping the header line

    # Define a pattern to extract the relevant data from each line
    pattern = r'(\d+)\s+(\d{2}:\d{2}:\d{2}:\d{2})\s+(\d+)\s+(\w+)\s+(.*?)\t+(.*)'

    # Initialize a list to hold the parsed data
    parsed_data = []

    # Process each line with the defined pattern
    for line in marker_lines:
        match = re.match(pattern, line)
        if match:
            parsed_data.append(match.groups())

    return parsed_data

def read_file(file_path):
    """
    Reads the content of a file.

    Args:
    file_path (str): Path to the file.

    Returns:
    str: Content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_csv(data, output_file_path):
    """
    Writes data to a CSV file.

    Args:
    data (list of tuples): Data to write to the CSV.
    output_file_path (str): Path to the output CSV file.
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data, columns=['Marker', 'Location', 'Time Reference', 'Units', 'Name', 'Comments'])

    # Write the DataFrame to a CSV file
    df.to_csv(output_file_path, index=False)

def process_markers(file_path, output_file_path):
    """
    Processes markers from a given file and writes them to a CSV file.

    Args:
    file_path (str): Path to the input file containing markers.
    output_file_path (str): Path to the output CSV file.
    """
    # Read the file content
    content = read_file(file_path)

    # Parse the markers
    parsed_markers = parse_markers(content)

    # Write the parsed data to a CSV file
    write_csv(parsed_markers, output_file_path)


def main(input_file_path, output_file_path):
    """
    Main function that processes the markers file and writes to a CSV file.

    Args:
    input_file_path (str): Path to the input file containing markers.
    output_file_path (str): Path to the output CSV file.
    """
    process_markers(input_file_path, output_file_path)

if __name__ == "__main__":
    # Extracting file paths from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python markers_to_csv.py <input_file_path> <output_file_path>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)