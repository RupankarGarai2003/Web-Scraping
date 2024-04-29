import plotly.graph_objects as go

# Define your data
categories = ['Men', 'Women', 'Rings', 'Men\'s Rings', 'Women\'s Rings', 'Earrings', 
              'Men\'s Earrings', 'Women\'s Earrings', 'Male\'s Earrings', 'Diamonds', 
              'Men\'s Diamonds', 'Women\'s Diamonds', 'Female\'s Diamonds', 'Silver', 
              'Men\'s Silver', 'Women\'s Silver', 'Male\'s Silver', 'Necklaces', 
              'Men\'s Necklaces', 'Women\'s Necklaces', 'Male\'s Necklaces', 'Bracelets', 
              'Men\'s Bracelets', 'Women\'s Bracelets', 'Male\'s Bracelets', 'Pendant Sets', 
              'Men\'s Pendant Sets', 'Women\'s Pendant Sets', 'Male\'s Pendant Sets', 
              'Necklace Sets', 'Men\'s Necklace Sets', 'Women\'s Necklace Sets', 
              'Male\'s Necklace Sets', 'Harams', 'Women\'s Harams', 'Bangles', 
              'Men\'s Bangles', 'Women\'s Bangles', 'Male\'s Bangles', 'Accessories', 
              'Women\'s Accessories', 'Nose Pins', 'Women\'s Nose Pins', 'Solitaire', 
              'Men\'s Solitaire', 'Women\'s Solitaire', 'Gifts', 'Men\'s Gifts', 
              'Women\'s Gifts', 'Men\'s Gold Coins', 'Women\'s Gold Coins', 'Male\'s Gold Coins']

item_counts = [987, 6234, 2170, 308, 1856, 2270, 73, 2095, 29, 5638, 779, 5062, 2, 946, 
               229, 787, 10, 496, 9, 485, 6, 488, 46, 401, 16, 420, 244, 402, 8, 161, 
               2, 160, 2, 3, 3, 451, 26, 421, 21, 130, 9, 111, 111, 170, 13, 158, 1345, 
               514, 929, 107, 430, 3]

# Create the bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=item_counts, marker_color='blue')])

# Customize the layout with HTML styling for the title
fig.update_layout(title='<span style="color:red">This Is The Graph Of Bluestone Jewellery</span>',
                  xaxis_title='<span style="color:black">Category</span>',
                  yaxis_title='<span style="color:black">Total Item Count</span>')

# Show the chart
fig.show()
