import pandas as pd
import re
import plotly.graph_objs as go
from plotly.offline import plot

# File paths
file_paths = ["./bhimagold.csv", "./bluestone.csv", "./chennaidiamonds.csv",
              "./joyalukkas.csv", "./KushalsFashionJewellery.csv", "./mellora.csv",
              "./pcjeweller.csv", "./pngjewellers.csv", "./sencogoldanddiamonds.csv"]

# Function to sum values based on a pattern
def sum_value(pattern):
    total_sum = 0
    for file in file_paths:
        df = pd.read_csv(file, header=None)
        matching_rows = df[df.apply(lambda row: any(pattern.search(str(value)) for value in row.values), axis=1)]
        if not matching_rows.empty:
            sum_values = matching_rows.iloc[:, 1].astype(float).sum()
            total_sum += sum_values
    return total_sum

# Regular expression patterns for different jewelry categories
pattern_men_rings = re.compile(r"\b(?:Men's Rings|Total_Rings_for_men|Men_rings)\b", flags=re.IGNORECASE)
pattern_women_rings = re.compile(r"\b(?:Women's Rings|Women_Rings|Women_rings)\b", flags=re.IGNORECASE)
pattern_men_earrings = re.compile(r"\b(?:Men's Earring|Men_earrings)\b", flags=re.IGNORECASE)
pattern_women_earrings = re.compile(r"\b(?:Women's Earring|Women_earrings)\b", flags=re.IGNORECASE)
pattern_men_necklaces = re.compile(r"\b(?:Men's Necklaces|Male's Necklaces|Necklaces_and_Pendants_for_Men)\b", flags=re.IGNORECASE)
pattern_women_necklaces = re.compile(r"\b(?:Women's Necklaces|female's Necklaces|Necklaces_and_Pendants_for_women)\b", flags=re.IGNORECASE)
pattern_men_bracelets = re.compile(r"\b(?:Men's Bracelets|Male's Bracelets|Total_no_of_Men_Bracelets)\b", flags=re.IGNORECASE)
pattern_women_bracelets = re.compile(r"\b(?:Women's Bracelets|Women_Bracelets)\b", flags=re.IGNORECASE)

# Calculate total sums for each category and gender
total_sum_rings = sum_value(pattern_men_rings)
total_sum_ringsw = sum_value(pattern_women_rings)
total_sum_earrings = sum_value(pattern_men_earrings)
total_sum_earringsw = sum_value(pattern_women_earrings)
total_sum_necklace = sum_value(pattern_men_necklaces)
total_sum_necklacew = sum_value(pattern_women_necklaces)
total_sum_bracelet = sum_value(pattern_men_bracelets)
total_sum_braceletw = sum_value(pattern_women_bracelets)

# Define the data for the bubble chart
categories = ['Rings', 'Earrings', 'Necklaces and Pendants', 'Bracelets']
men_data = [total_sum_rings, total_sum_earrings, total_sum_necklace, total_sum_bracelet]
women_data = [total_sum_ringsw, total_sum_earringsw, total_sum_necklacew, total_sum_braceletw]

# Calculate sizeref based on maximum values
max_data = max(max(men_data), max(women_data))
sizeref = 2.0 * max_data / (100 ** 2)  # Adjust the 100 value to control the bubble size

# Create custom text annotations for each bubble
men_annotations = [f"Total: {value}" for value in men_data]
women_annotations = [f"Total: {value}" for value in women_data]

# Create the bubble chart
trace1 = go.Scatter(
    x=categories,
    y=[1] * len(categories),
    mode='markers+text',
    marker=dict(
        size=men_data,
        sizemode='area',
        sizeref=sizeref,
        color='green',
        opacity=0.5,
        line=dict(width=2),
    ),
    text=men_annotations,
    textposition='top center',
    name='Men'
)

trace2 = go.Scatter(
    x=categories,
    y=[2] * len(categories),
    mode='markers+text',
    marker=dict(
        size=women_data,
        sizemode='area',
        sizeref=sizeref,
        color='red',
        opacity=0.5,
        line=dict(width=2),
    ),
    text=women_annotations,
    textposition='top center',
    name='Women'
)

data = [trace1, trace2]

# Define the layout
layout = go.Layout(
    title='Category-wise Distribution of Jewelry by Gender',
    yaxis=dict(
        tickvals=[1, 2],
        ticktext=['Men', 'Women'],
        showticklabels=True,
        tickmode='array',
        ticklen=0,
        tickfont=dict(size=12)
    ),
    xaxis=dict(
        title='Categories',
        showgrid=False,
        tickfont=dict(size=12)
    ),
    margin=dict(l=50, r=50, t=50, b=50),
)

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Display the chart
plot(fig, filename='bubble_chart.html', auto_open=True)
