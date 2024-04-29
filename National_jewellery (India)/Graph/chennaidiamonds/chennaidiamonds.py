import plotly.graph_objects as go

# Define your data
categories = ['Men', 'Women', 'Male', 'Rings', 'Men\'s Rings', 'Women\'s Rings', 'Male\'s Rings', 'Female\'s Rings',
              'Earring', 'Men\'s Earring', 'Women\'s Earring', 'Male\'s Earring', 'Female\'s Earring',
              'Diamond', 'Men\'s Diamond', 'Women\'s Diamond', 'Male\'s Diamond', 'Female\'s Diamond',
              'Silver', 'Men\'s Silver', 'Women\'s Silver', 'Male\'s Silver', 'Female\'s Silver',
              'Necklaces', 'Men\'s Necklaces', 'Women\'s Necklaces', 'Male\'s Necklaces', 'Female\'s Necklaces',
              'Bracelets', 'Men\'s Bracelets', 'Women\'s Bracelets', 'Male\'s Bracelets', 'Female\'s Bracelets',
              'Pendant Sets', 'Men\'s Pendant Sets', 'Women\'s Pendant Sets', 'Male\'s Pendant Sets', 'Female\'s Pendant Sets',
              'Necklace Sets', 'Men\'s Necklace Sets', 'Women\'s Necklace Sets', 'Male\'s Necklace Sets', 'Female\'s Necklace Sets',
              'Harams', 'Men\'s Harams', 'Women\'s Harams', 'Male\'s Harams', 'Female\'s Harams',
              'Bangles', 'Men\'s Bangles', 'Women\'s Bangles', 'Male\'s Bangles', 'Female\'s Bangles',
              'Accessories', 'Men\'s Accessorie', 'Women\'s Accessorie', 'Male\'s Accessorie', 'Female\'s Accessorie',
              'Nose Pins', 'Men\'s Nose Pins', 'Women\'s Nose Pins', 'Male\'s Nose Pins', 'Female\'s Nose Pins',
              'Solitaire', 'Men\'s Solitaire', 'Women\'s Solitaire', 'Male\'s Solitaire', 'Female\'s Solitaire',
              'Gifts', 'Men\'s Gifts', 'Women\'s Gifts', 'Male\'s Gifts', 'Female\'s Gifts',
              'Gold Coins', 'Men\'s Gold Coins', 'Women\'s Gold Coins', 'Male\'s Gold Coins', 'Female\'s Gold Coins']

item_counts = [11, 73, 35, 6, 17, 73, 35, 6, 7, 18, 73, 36, 7, 65, 71, 79, 65, 65, 0, 11, 73, 35, 0, 32, 43, 73, 53, 32,
               20, 22, 80, 46, 20, 40, 51, 74, 56, 40, 44, 55, 74, 56, 44, 6, 17, 73, 36, 6, 18, 29, 74, 47, 18, 1, 12, 73, 35,
               1, 41, 48, 77, 43, 41, 12, 21, 75, 47, 12, 6, 16, 74, 38, 6, 45, 52, 78, 46, 45]

# Create the bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=item_counts, marker_color='blue')])

# Customize the layout
fig.update_layout(title='<b><span style="color:red">This Is The Graph Of chennaidiamonds Jewellery</span></b>',
                  xaxis_title='Category',
                  yaxis_title='Total Item Count')

# Show the chart
fig.show()
