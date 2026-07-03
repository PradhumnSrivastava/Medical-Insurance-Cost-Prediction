import pandas as pd
import logging

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
    df = pd.read_csv(path)
    
    logging.info("Data loaded successfully.")
    logging.info(f"Data shape: {df.shape}")
    
    return df
    