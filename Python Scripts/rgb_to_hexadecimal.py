# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:15:05 2024

@author: USNA0501
"""

import pandas as pd

# Sample data: replace this with your actual data
file_path = 'C:/Users/USNA0501/Downloads/donne_rgb.xlsx'
df = pd.read_excel(file_path)
df = df.dropna()


# Function to convert RGB to hexadecimal
def rgb_to_hex(r, g, b):
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

# Apply the function to each row and create a new column for the hex values
df['Hex'] = df.apply(lambda row: rgb_to_hex(row['Couleur R'], row['Couleur V'], row['Couleur B']), axis=1)


color_dict = df[['Ingredient', 'Hex']].set_index('Ingredient')

output_file_path = 'C:/Users/USNA0501/Downloads/donne_hexadecimal.xlsx'
color_dict.to_excel(output_file_path, index=True)
# Print the DataFrame
print(color_dict)
