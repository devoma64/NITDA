# employee_list = [
    
#     {"id": 12345, "name": "John", "department": "Kitchen"}, 
#     {"id": 12458, "name": "Paul", "department": "House Floor"}
#     ]

# def get_employee_record(id):
#     for employee in employee_list:
#         if (employee['id'] == id):
#             return employee
        
        
# print(get_employee_record(12345))

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_disct(id):
    return employee_dict[id];

print(get_employee_from_disct(12458));