#!/bin/bash

# Check if the directory is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: bash fill.sh <directory_path>"
    exit 1
fi

DIRECTORY=$1

# Loop through all image files in the directory
for IMAGE in "$DIRECTORY"/*.{jpg,jpeg,png}; do
    # Check if the file exists
    if [ -e "$IMAGE" ]; then
        # Define output path
        OUTPUT="${IMAGE%.*}_filled.png"
        
        # Call the Python script
        python flood_fill.py "$IMAGE" "$OUTPUT"
        
        echo "Processed $IMAGE and saved to $OUTPUT"
    else
        echo "No image files found in the directory."
    fi
done