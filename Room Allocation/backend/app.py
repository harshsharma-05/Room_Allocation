from flask import Flask, render_template, request, jsonify
from csv_handler import parse_group_csv, parse_hostel_csv
from room_allocation import allocate_rooms

app = Flask(__name__, template_folder="c:\\xampp\\htdocs\\Room Allocation\\forntend")

# Configure static folder
app.static_folder ='../backend/static'
app.static_url_path ='/static'  # URL path for static files

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    group_file = request.files['groupFile']
    hostel_file = request.files['hostelFile']
    
    if group_file and hostel_file:
        group_data = parse_group_csv(group_file)
        hostel_data = parse_hostel_csv(hostel_file)
        
        if group_data and hostel_data:
            allocation_result = allocate_rooms(group_data, hostel_data)
            return jsonify(allocation_result)
        else:
            return jsonify({'error': 'Invalid CSV files'})
    else:
        return jsonify({'error': 'Files not uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
