import copy

# Example input data
measure_arrays = {
    'A': [
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
    ],
    'B': [
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
    ],
    'C': [
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
}

# Function to transform data
def transform_data(measure_arrays):
    result = {}
    
    # Initialize result templates for each metric
    all_dates = set()
    metrics = set()
    
    # Gather all metrics and dates
    for key, measures in measure_arrays.items():
        for measure in measures:
            metrics.add(measure['metric'])
            for record in measure['history']:
                all_dates.add(record['date'])
    
    # Create a template for all dates
    template = {date: {'date': date, **{k: '' for k in measure_arrays.keys()}} for date in all_dates}
    
    # Populate the result for each metric and date
    for metric in metrics:
        metric_result = copy.deepcopy(template)
        
        for source, measures in measure_arrays.items():
            for measure in measures:
                if measure['metric'] == metric:
                    for record in measure['history']:
                        metric_result[record['date']][source] = record['value']
        
        result[f"{metric}_result"] = list(metric_result.values())
    
    return result

# Transform the data
transformed_data = transform_data(measure_arrays)

# Print the results
for key, value in transformed_data.items():
    print(f"{key} = {value}")

# Results can also be accessed individually, e.g.:
bugs_result = transformed_data.get('bugs_result', [])
coverage_result = transformed_data.get('coverage_result', [])
duplicate_result = transformed_data.get('duplicate_lines_result', [])
smell_result = transformed_data.get('code_smells_result', [])
