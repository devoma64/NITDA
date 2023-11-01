
employee_list = [
    
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Managment"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
    
]

def mod(employee_list):
    temp = employee_list['name'] + "-" + employee_list["department"]
    print(temp)
    return temp

def to_mod_list(employee_list):
    # modifying the employees list of dictionaries to list of department
    emp_departments = list(map(mod, employee_list))
    return emp_departments
    
def generate_usernames(mod_list):
    
    usernames = []
    
    for item in mod_list:
        if isinstance(item, dict):
            name = item.get('name', ' ')
            usernames.append(name.replace(' ', '_'))
        elif isinstance(item, str):
            usernames.append(item.replace(' ', '_'))
        else:
            usernames.append(str(item))
    return usernames

def map_id_to_initial(employee_list):
    n_dictionary = {item['id']: item['name'][0] for item in employee_list}
    return n_dictionary

def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")
    
    print(f"List of usernames: {generate_usernames(employee_list)}\n")
    
    print(f"Initials and ids: {map_id_to_initial(employee_list)}")
    
if __name__ == "__main__":
    main() 