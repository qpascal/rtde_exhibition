import pandas as pd
import matplotlib.pyplot as plt

# Create a sample data dictionary
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [123, 234, 345, 210, 456]
}

# Load data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the Year column as the index
df.set_index('Year', inplace=True)

# Plot the data
df['Sales'].plot(kind='bar', color='skyblue')  # Change kind to 'line' if a line chart is preferred

# Add title and labels
plt.title('Annual Sales')
plt.xlabel('Year')
plt.ylabel('Sales (in units)')

# Show the plot
plt.show()