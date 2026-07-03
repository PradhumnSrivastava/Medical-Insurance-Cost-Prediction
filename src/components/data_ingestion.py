import pandas as pd
from src.logger.logger import logging
import logging

import os

print("Current Working Directory:", os.getcwd())

print("File is running...")
def load_data(path: str) -> pd.DataFrame: #type hinting
    #docstring is the first statement in the function and is used to describe what the function does
    """
    Load data from a CSV file.
    Parameters:
    path (str): The path to the CSV file.
    Returns:
    pd.DataFrame: The loaded data.
    """
    logging.info(f"Reading data from {path}")
    
    try:
        df = pd.read_csv(path)
        
        logging.info("Data loaded successfully.")
        logging.info(f"Data shape: {df.shape}")
        
        return df
        
    except Exception as e:
        logging.exception(f"Error occurred while loading data from {path}")
        raise


if __name__ == "__main__":
    print("__main__ block executed")
    df = load_data("data/medical_insurance.csv")
    print(df.head())
            
    
        