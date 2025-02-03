from flask import Flask, render_template
import plotly.graph_objects as go
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Sample data without using pandas
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 120, 140, 130, 150, 160]
    
    # Create plotly figure directly
    fig = go.Figure(data=[
        go.Scatter(x=months, y=sales, mode='lines+markers')
    ])
    fig.update_layout(title='Monthly Sales')
    
    chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Calculate KPIs
    kpis = {
        'Total Sales': f"${sum(sales):,.0f}",
        'Average Sales': f"${sum(sales)/len(sales):,.0f}",
        'Peak Sales': f"${max(sales):,.0f}"
    }
    
    return render_template('dashboard.html', 
                         chart=chart_json,
                         kpis=kpis,
                         table_data=zip(months, sales))

if __name__ == '__main__':
    app.run()
