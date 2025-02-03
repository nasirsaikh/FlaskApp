from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import plotly

app = Flask(__name__)

# Sample data generation
def get_sample_data():
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [100, 120, 140, 130, 150, 160],
        'Expenses': [80, 90, 95, 85, 100, 110],
        'Profit': [20, 30, 45, 45, 50, 50]
    })
    return df

@app.route('/')
def dashboard():
    df = get_sample_data()
    
    # Create visualizations
    sales_fig = px.line(df, x='Month', y='Sales', title='Monthly Sales')
    sales_chart = json.dumps(sales_fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    profit_fig = px.bar(df, x='Month', y='Profit', title='Monthly Profit')
    profit_chart = json.dumps(profit_fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # KPIs
    kpis = {
        'Total Sales': f"${df['Sales'].sum():,.0f}",
        'Average Profit': f"${df['Profit'].mean():,.0f}",
        'Profit Margin': f"{(df['Profit'].sum() / df['Sales'].sum() * 100):.1f}%"
    }
    
    return render_template('dashboard.html', 
                         sales_chart=sales_chart,
                         profit_chart=profit_chart,
                         kpis=kpis,
                         data=df.to_dict('records'))

if __name__ == '__main__':
    app.run()
