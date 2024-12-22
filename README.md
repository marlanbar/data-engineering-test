# IFCO Data Analysis Project

## Overview

This project processes and analyzes business data for IFCO's Data Team. It includes data manipulation, and sales commission calculations.

## Project Structure

- **data/**: Contains input data files.
- **src/**: Contains source code for data processing and visualization.
- **tests/**: Contains unit tests for each module.
- **output/**: Contains generated CSV files.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Data Files**: Place `orders.csv` and `invoicing_data.json` in the `resources/` directory.

## Running the Project

1. **Run the Main Script**:
   ```bash
   python src/main.py
   ```

2. **Check the Output**: Review the generated CSV files in the `output` directory.

## Running Unit Tests

To ensure everything is working correctly, run the unit tests:

```bash
python -m unittest discover -s tests
```

## Dependencies

- **pandas==1.3.3**
