
## Imports
import plotly.graph_objs as go
import pandas as pd
import random

# Load Data
data = pd.read_csv('./Data/data.csv')
data.sample(5)

def generate_plot(data):
    
    # 5 Random colunms
    random.seed(123)
    selected_cols = 5
    cols = random.sample(list(data.columns[1:-1]), selected_cols)

    # Inputs for plot
    dimensions = [dict(label=col, values=data[col]) for col in cols]
    colors = ['red', 'green', 'yellow', 'purple']

    # Plot
    fig = go.Figure(data=
        go.Splom(dimensions=dimensions, marker=dict(color=colors))
    )

    # layout
    fig.update_layout(
        title={'text': 'Scatter Matrix',
                'y': 0.95,
                'x' : 0.5,},
        width=1200,
        height= 850,
        plot_bgcolor = 'steelblue'
    )
    return fig

generate_plot(data)



