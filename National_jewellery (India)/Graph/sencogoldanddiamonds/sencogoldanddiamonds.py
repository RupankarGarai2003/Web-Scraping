import plotly.graph_objects as go

# Define the data
categories = ['Men', 'Women', 'Male', 'Rings', 'Men\'s Rings', 'Women\'s Rings', 'Male\'s Rings', 'Female\'s Rings',
              'Earring', 'Women\'s Earring', 'Male\'s Earring', 'Female\'s Earring',
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

item_counts = [728, 523, 2, 2827, 215, 30, 224, 3081, 2459, 26, 174, 1, 6781, 419, 73, 501, 2, 74, 1, 2, 17, 176, 17, 1, 90,
               79, 1, 3, 31, 1, 2, 3, 1100, 31, 1639, 2, 4, 1007, 13, 1, 2, 1, 133, 573, 17, 6, 43, 858, 112, 63, 62, 57,
               65, 1, 19, 5, 2, 68, 79, 3, 8, 12, 69, 2313, 247, 31, 193, 2416, 27, 1, 2, 6, 7160]

# Create the bar chart
fig = go.Figure(data=[go.Bar(x=categories, y=item_counts, marker_color='blue')])

# Customize the layout
fig.update_layout(title='<b><span style="color:red">This Is The Graph Of sencogoldanddiamonds Jewellery</span></b>',
                  xaxis_title='Category',
                  yaxis_title='Total Item Count')

# Show the chart
fig.show()
