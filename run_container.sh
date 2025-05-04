#!/bin/bash

# Check if match number is provided
if [ $# -ne 1 ]; then
    echo "Usage: ./run_container.sh <match_number>"
    echo "Example: ./run_container.sh 1"
    exit 1
fi

MATCH_NUMBER=$1
EXCEL_FILE="SquadPlayerNames_IndianT20League.xlsx"
DOWNLOADS_PATH="$HOME/Downloads"
EXCEL_PATH="$DOWNLOADS_PATH/$EXCEL_FILE"

# Check if Excel file exists in Downloads folder
if [ ! -f "$EXCEL_PATH" ]; then
    echo "Error: $EXCEL_FILE not found in Downloads folder."
    echo "Please make sure the file exists at: $EXCEL_PATH"
    exit 1
fi

# Run the Docker container
echo "Running NeuralNetNinjas for match number $MATCH_NUMBER..."
docker run --rm -v "$EXCEL_PATH:/app/data/$EXCEL_FILE" neuralnetninjas "$MATCH_NUMBER"

echo "Done!" 