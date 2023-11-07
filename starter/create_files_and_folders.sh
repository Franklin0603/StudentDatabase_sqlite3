#!/bin/bash

# Define the prefix
prefix="SchoolDatabase"

# Define the array of file names
declare -a files=(
    "${prefix}_ws_raw.ipynb"
    "${prefix}_ws_clean.ipynb"
    "${prefix}_dev.py"
    "${prefix}_prod.py"
    "config.ini"
)

# Loop through the array and create each file
for file in "${files[@]}"; do
    touch "$file"
done

# Create the data directory
mkdir -p "data"

echo "Files and folders created successfully."
