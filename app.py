from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    try:
        # Sample static data
        data = {
            'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'sales': [100, 120, 140, 130, 150, 160]
        }
        
        # KPIs
        kpis = {
            'Total Sales': f"${sum(data['sales']):,.0f}",
            'Average Sales': f"${sum(data['sales'])/len(data['sales']):,.0f}",
            'Peak Sales': f"${max(data['sales']):,.0f}"
        }
        
        return render_template('dashboard.html', 
                             data=data,
                             kpis=kpis)
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return f"An error occurred: {str(e)}", 500

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(debug=True)
