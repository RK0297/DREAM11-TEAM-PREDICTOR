# Dream11 Team Predictor

A machine learning-based application that predicts optimal Dream11 teams for Indian T20 League matches.

## Overview

This application uses machine learning to analyze player statistics and predict the best possible Dream11 team for Indian T20 League matches. It considers various factors including:

- Player performance metrics
- Team composition
- Player roles (Batsman, Bowler, All-rounder, Wicket-keeper)
- Credits allocation
- Recent form
- Batting order

## Features

- **ML-based Prediction**: Uses a Gradient Boosting Regressor model trained on historical player data
- **Optimization**: Employs linear programming to select the best team within credit constraints
- **Role Balancing**: Ensures proper distribution of player roles
- **Captain/Vice-Captain Selection**: Intelligently assigns captain and vice-captain based on predicted performance
- **Docker Support**: Containerized application for easy deployment

## Requirements

- Python 3.8.20
- Docker (optional, for containerized deployment)

## Installation

### Local Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r req.txt
   ```
3. Run the training script to create the model:
   ```
   python TRAIN1.py
   ```
4. Run the application:
   ```
   python app1.py <match_number>
   ```

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t neuralnetninjas .
   ```
2. Run the container:
   ```
   docker run --rm -v ~/Downloads/SquadPlayerNames_IndianT20League.xlsx:/root/Downloads/SquadPlayerNames_IndianT20League.xlsx neuralnetninjas <match_number>
   ```

## Input Data

The application expects an Excel file named `SquadPlayerNames_IndianT20League.xlsx` in your Downloads folder. This file should contain:

- Player names
- Credits
- Player types (BAT, BOWL, ALL, WK)
- Team information
- Batting order (optional)

Each match should be in a separate sheet named `Match_1`, `Match_2`, etc.

## Output

The application generates a CSV file named `predicted_team_match_X.csv` in your Downloads folder, where X is the match number. The output includes:

- Selected players
- Their teams
- Captain and vice-captain assignments

## Dependencies

- pandas (>=1.3.0,<2.0.0)
- numpy (>=1.21,<1.24)
- pulp (3.1.1)
- joblib (1.2.0)
- pycaret (3.1.0)
- openpyxl (3.1.2)
- scikit-learn (1.0.2)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
