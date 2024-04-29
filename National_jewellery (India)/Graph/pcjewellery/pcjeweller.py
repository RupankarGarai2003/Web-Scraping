import plotly.graph_objects as go

# Define the data
categories = ['Men\'s Items', 'Women\'s Items', 'Total Jewellery', 'Total Rings', 
              'Total Earrings', 'Men\'s Jewellery', 'Women\'s Jewellery', 
              'Men\'s Rings', 'Women\'s Rings', 'Women\'s Earrings', 
              'Men\'s Silver', 'Women\'s Silver']

total_counts = [64, 6, 7575, 2835, 2302, 420, 5390, 363, 2269, 1641, 60, 193]

# Create the bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=total_counts, marker_color='blue')])

# Customize the layout
fig.update_layout(title='<span style="color:red">This Is The Graph Of PcJeweller </span>',
                  xaxis_title='Category',
                  yaxis_title='Total Count')

# Show the chart
fig.show()
