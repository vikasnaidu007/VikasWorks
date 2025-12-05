# READING CSV FILES IN PYTHON

import csv

# Open the CSV file in read mode
with open('model_logs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)    # Create a CSV reader object
    # print(reader)

    next(reader)    # Skip the header row

    # for row in reader:
    #     print(row)
    # print(reader)

    # find the day where the tokens are used max

    day_wise_tokens = {row[0]: row[3] for row in reader }
    print(day_wise_tokens)

    peak_day = max(day_wise_tokens, key=day_wise_tokens.get)
    print(f' peak Day Usage {peak_day}, tokens Generated {day_wise_tokens[peak_day]}')




