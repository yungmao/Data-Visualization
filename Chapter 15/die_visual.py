from die import Die
from plotly.graph_objs import  Bar, Layout
from plotly import offline

# Create a D6
die = Die(6)

# Make some rolls, and store results in list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# Visualize the results
x_value = list(range(1, die.num_sides+1))
data = [Bar(x=x_value, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
