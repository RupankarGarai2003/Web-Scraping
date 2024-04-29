import plotly.graph_objects as go

# Define the data
categories = ['Men', 'Women', 'Rings', 'Earring', 'Diamond', 'Silver', 'Necklaces', 
              'Men\'s Ring', 'Women\'s Ring', 'Men\'s Earring', 'Men\'s Diamond', 
              'Women\'s Diamond', 'Men\'s Gold', 'Women\'s Gold', 'Men\'s Silver', 
              'Women\'s Silver', 'Men\'s Necklaces', 'Women\'s Necklaces']

item_counts = [11, 9, 235, 596, 1020, 129, 152, 7, 6, 3, 8, 9, 11, 9, 0, 0, 0, 0]

# Create the bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=item_counts, marker_color='blue')])

# Customize the layout
fig.update_layout(title='<span style="color:red">This Is The Graph Of pngJewellers Jewellery</span>',
                  xaxis_title='Category',
                  yaxis_title='Total Item Count')

# Show the chart
fig.show()
