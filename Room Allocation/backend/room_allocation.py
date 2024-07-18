def allocate_rooms(group_data, hostel_data):
    # Algorithm to allocate rooms based on given criteria
    allocation_result = []
   
    for group in group_data:
        allocation_result.append({
            'Group ID': group['Group ID'],
            'Hostel Name': 'Boys Hostel A',
            'Room Number': '101',
            'Members Allocated': group['Members']
        })
    
    return allocation_result