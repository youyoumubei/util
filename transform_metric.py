import copy

# Example input data
A_measures = [
    {
        'metric': 'bugs',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '100'},
            {'date': '2023-08-09T05:43:35', 'value': '105'},
        ]
    },
    {
        'metric': 'coverage',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '85'},
            {'date': '2023-08-09T05:43:35', 'value': '90'},
        ]
    }
]

B_measures = [
    {
        'metric': 'bugs',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '110'},
            {'date': '2023-08-09T05:43:35', 'value': '115'},
        ]
    },
    {
        'metric': 'coverage',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '80'},
            {'date': '2023-08-09T05:43:35', 'value': '85'},
        ]
    }
]

C_measures = [
    {
        'metric': 'bugs',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '120'},
            {'date': '2023-08-09T05:43:35', 'value': '125'},
        ]
    },
    {
        'metric': 'coverage',
        'history': [
            {'date': '2023-08-08T05:43:35', 'value': '75'},
            {'date': '2023-08-09T05:43:35', 'value': '80'},
        ]
    }
]

# Combine the measures into a dictionary for easy access
combined_measures = {
    'A': A_measures,
    'B': B_measures,
    'C': C_measures
}

# Function to transform data
def transform_data(combined_measures):
    result = {}
    
    # Initialize result templates for each metric
    metrics = {measure['metric'] for measure in combined_measures['A']}
    dates = {record['date'] for measure in combined_measures['A'] for record in measure['history']}
    template = {date: {'date': date, 'A': '', 'B': '', 'C': ''} for date in dates}
    
    # Populate the result for each metric and date
    for metric in metrics:
        metric_result = copy.deepcopy(template)
        
        for source, measures in combined_measures.items():
            for measure in measures:
                if measure['metric'] == metric:
                    for record in measure['history']:
                        metric_result[record['date']][source] = record['value']
        
        result[f"{metric}_result"] = list(metric_result.values())
    
    return result

# Transform the data
transformed_data = transform_data(combined_measures)

# Print the results
for key, value in transformed_data.items():
    print(f"{key} = {value}")

# Results can also be accessed individually, e.g.:
bugs_result = transformed_data['bugs_result']
coverage_result = transformed_data['coverage_result']
duplicate_result = transformed_data.get('duplicate_lines_result', [])
smell_result = transformed_data.get('code_smells_result', [])
