import csv

def process_csv(input_file, output_file, col1_index, col2_index, threshold=0):
    # Open and read the input CSV file
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        
        # Read the header (first row) and add the 'Total' column to the header
        header = next(reader)
        header.append('Total')

        # Prepare for the output CSV file
        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            # Process each row in the input CSV
            for row in reader:
                try:
                    # Convert the columns to integers and calculate the total
                    value1 = int(row[col1_index])
                    value2 = int(row[col2_index])
                    total = value1 + value2
                    
                    # Add the 'Total' column to the row
                    row.append(total)

                    # Apply filtering condition: only include rows where the total is above the threshold
                    if total > threshold:
                        writer.writerow(row)
                
                except ValueError:
                    # Handle invalid data (non-integer values)
                    print(f"Skipping row due to invalid data: {row}")
                    continue

def main():
    # File paths
    input_file = 'input.csv'  # Input CSV file path
    output_file = 'output.csv'  # Output CSV file path
    
    # Column indices (change as per your CSV structure)
    col1_index = 1  # Index of the first column to sum
    col2_index = 2  # Index of the second column to sum
    
    # Threshold value to filter rows
    threshold = 100
    
    # Call the function to process the CSV file
    process_csv(input_file, output_file, col1_index, col2_index, threshold)
    print(f"Processed data has been written to {output_file}")

if __name__ == "__main__":
    main()
