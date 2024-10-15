import random

def random_allocation(projects, total_resources):
    allocation = []
    remaining_resources = total_resources

    for project in projects:
        if remaining_resources >= project['requirement']:
            allocation.append(project)
            remaining_resources -= project['requirement']
    return allocation

def explore_neighbor(current_allocation, projects, total_resources):
    new_allocation = current_allocation[:]

    if new_allocation:
        new_allocation.remove(random.choice(new_allocation))

    remaining_resources = total_resources - sum(p['requirement'] for p in new_allocation)
    candidates = [p for p in projects if p not in new_allocation and p['requirement'] <= remaining_resources]

    if candidates:
        new_allocation.append(random.choice(candidates))

    return new_allocation

def rhc(projects, objective_function, total_resources, iterations=1000):
    current_allocation = random_allocation(projects, total_resources)
    current_value, _ = objective_function(current_allocation)
    
    for _ in range(iterations):
        new_allocation = explore_neighbor(current_allocation, projects, total_resources)
        new_value, comparison_type = objective_function(new_allocation)
        
        if (comparison_type == 'max' and new_value > current_value) or \
           (comparison_type == 'min' and new_value < current_value):
            current_allocation = new_allocation
            current_value = new_value
    
    return current_allocation, current_value

def maximize_benefit(allocation):
    return sum(p['benefit'] for p in allocation), 'max'

def minimize_time(allocation):
    return sum(p['time'] for p in allocation), 'min'

resources = [100, 60]

test_cases = {
        1: [{'id': 1, 'requirement': 20, 'benefit': 40},
            {'id': 2, 'requirement': 30, 'benefit': 50},
            {'id': 3, 'requirement': 25, 'benefit': 30},
            {'id': 4, 'requirement': 15, 'benefit': 25}],

        2: [{'id': 'A', 'requirement': 10, 'time': 15},
            {'id': 'B', 'requirement': 40, 'time': 60},
            {'id': 'C', 'requirement': 20, 'time': 30},
            {'id': 'D', 'requirement': 25, 'time': 35},
            {'id': 'E', 'requirement': 5, 'time': 10}],

        3: [{'id': 'X', 'requirement': 50, 'benefit': 80},
            {'id': 'Y', 'requirement': 30, 'benefit': 45},
            {'id': 'Z', 'requirement': 15, 'benefit': 20},
            {'id': 'W', 'requirement': 25, 'benefit': 35}]
        }

for num_resources in resources:
    print(f'running test cases with {num_resources} available resources per test case')

    allocation_tc1, value_tc1 = rhc(test_cases[1], maximize_benefit, num_resources)
    print(f'allocation for test case 1: ')
    for allocation in allocation_tc1:
        print(allocation)
    print(f'total benefit: {value_tc1}')
    print('===========================================================================')

    allocation_tc2, value_tc2 = rhc(test_cases[2], minimize_time, num_resources)
    print(f'allocation for test case 2: ')
    for allocation in allocation_tc2:
        print(allocation)
    print(f'total time: {value_tc2}')
    print('===========================================================================')

    allocation_tc3, value_tc3 = rhc(test_cases[3], maximize_benefit, num_resources)
    print(f'allocation for test case 3: ')
    for allocation in allocation_tc3:
        print(allocation)
    print(f'total benefit: {value_tc3}')
    print('===========================================================================')
