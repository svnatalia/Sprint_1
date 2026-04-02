# Дополнительное задание 1

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def new_tickets(tikets):
    seen_tickets = set()
    filtered_tickets = {}
    for key, value in tickets.items():
        unique_tickets = []
        for ticket in value:
            if ticket not in seen_tickets:
                unique_tickets.append(ticket)
                seen_tickets.add(ticket)
        filtered_tickets[key] = unique_tickets
    return filtered_tickets

def tickets_by_type(types, tickets):
    clean_tickets = new_tickets(tickets)
    result = {}
    for key in types:
        result[types[key]] = clean_tickets[key]
    return result

print(tickets_by_type(types, tickets))