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

# Define the data for the sunburst chart
sunburst_data = {
    'Jewelry': {
        'Men': {
            'Rings': total_sum_rings,
            'Earrings': total_sum_earrings,
            'Necklaces and Pendants': total_sum_necklace,
            'Bracelets': total_sum_bracelet
        },
        'Women': {
            'Rings': total_sum_ringsw,
            'Earrings': total_sum_earringsw,
            'Necklaces and Pendants': total_sum_necklacew,
            'Bracelets': total_sum_braceletw
        }
    }
}

# Function to create sunburst chart data
def create_sunburst_data(data_dict, parent_name=''):
    result = []
    for name, value in data_dict.items():
        if isinstance(value, dict):
            children = create_sunburst_data(value, parent_name=name)
            if children:
                result.append(dict(
                    name=name,
                    children=children
                ))
        else:
            result.append(dict(
                name=name,
                value=value,
                parent=parent_name
            ))
    return result

# Generate sunburst chart data
sunburst_data = create_sunburst_data(sunburst_data)

# Print sunburst data for inspection
print(sunburst_data)

# Create sunburst chart
fig_sunburst = go.Figure(go.Sunburst(
    labels=[node['name'] for node in sunburst_data],
    parents=[node.get('parent', '') for node in sunburst_data],
    values=[node.get('value', 0) for node in sunburst_data],
))

# Update layout
fig_sunburst.update_layout(
    title='Category-wise Distribution of Jewelry by Gender (Sunburst Chart)',
    margin=dict(t=50, l=0, r=0, b=0)
)

# Display the sunburst chart
fig_sunburst.show()
