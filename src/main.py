from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource

import sys
import csv
from typing import Dict

def load_csv_data(path: str) -> Dict:
    output = {
        "x_values": [],
        "y_values": [],
        "fuck_around": [],
        "find_out": [],
    }

    with open(path, "r") as f:
        reader = csv.reader(f)
        # skip the first row (column headers)
        next(reader)

        for row in reader:
            # descriptions of what happened
            output["fuck_around"].append(row[0])
            output["find_out"].append(row[1])

            # numerical values from the csv
            output["x_values"].append(float(row[2]))
            output["y_values"].append(float(row[3]))

    return output


def default_csv_data():
    data = {
        "x_values": [1, 2, 3, 4],
        "y_values": [1, 2, 3, 4],
        "fuck_around": ["1", "2", "3", "4fo"],
        "find_out": ["1", "2", "3", "4"],
    }

    return data


source_file = sys.argv[1]
save_path = sys.argv[2]

print(f"converting data at {source_file} to output file at {save_path}")

# the tooltip that appears at every data point
TOOLTIPS = [
    ("Fuck Around", "(@x_values{0.2f}) @fuck_around"),
    ("Find Out", "(@y_values{0.2f}) @find_out"),
]

CIRCLE_SIZE = 15

# create a figure with a 16x9 aspect ratio
p = figure(width=160, height=90, x_range=(0, 10), y_range=(0, 10), tooltips=TOOLTIPS, title="How to Find Out")

data = load_csv_data(source_file)
source = ColumnDataSource(data=data)

# some plot attributes to make things look nice
p.sizing_mode = "scale_both"
p.border_fill_color = "whitesmoke"

# axis labels
p.xaxis.axis_label = "Fuck Around"
p.yaxis.axis_label = "Find Out"

# plot the data on the figure
p.circle(x="x_values", y="y_values", source=source, size=CIRCLE_SIZE)

# save the output
output_file(save_path)
save(p, title="Find Out")
