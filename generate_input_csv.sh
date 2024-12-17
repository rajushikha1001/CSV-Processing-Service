#!/bin/bash

# Define the name of the output CSV file
output_file="input.csv"

# Write the header to the CSV file
echo "ID,Value1,Value2" > "$output_file"

# Generate random data and append it to the CSV file
for i in {1..10}
do
    # Generate random values for Value1 and Value2 (you can adjust the range as needed)
    value1=$((RANDOM % 100))
    value2=$((RANDOM % 100))

    # Append the generated values as a new row to the CSV file
    echo "$i,$value1,$value2" >> "$output_file"
done

echo "CSV file '$output_file' has been generated."
