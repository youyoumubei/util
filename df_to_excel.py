import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from multiprocessing import Pool

# Create a function to write a DataFrame to a given sheet
def write_dataframe_to_sheet(df, sheet):
    for row in dataframe_to_rows(df, index=False, header=True):
        sheet.append(row)

# Create a function to handle writing data using multiprocessing
def write_data(args):
    df, sheet = args
    write_dataframe_to_sheet(df, sheet)

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['your_database']
collection = db['your_collection']

# Define the pipeline
pipeline = [
    # ... your aggregation stages ...
]

# Execute the pipeline and get a cursor
cursor = collection.aggregate(pipeline)

# Define a batch size
batch_size = 1000

# Generator function to yield batches of results
def batched_results(cursor, batch_size):
    batch = []
    for doc in cursor:
        batch.append(doc)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

# Process the results in batches
for result_batch in batched_results(cursor, batch_size):
    # Process each document in the batch
    for doc in result_batch:
        # Process the document as needed
        print(doc)


if __name__ == "__main__":
    # Create some sample DataFrames
    data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    data2 = {'X': [7, 8, 9], 'Y': [10, 11, 12]}
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    
    # Create an Excel writer
    output_path = "output.xlsx"
    writer = pd.ExcelWriter(output_path, engine='openpyxl')
    
    # Write each DataFrame to a separate sheet using multiprocessing
    sheets_data = [(df1, 'Sheet1'), (df2, 'Sheet2')]
    
    with Pool(processes=len(sheets_data)) as pool:
        pool.map(write_data, sheets_data)
    
    # Save and close the Excel writer
    writer.save()
    writer.close()
