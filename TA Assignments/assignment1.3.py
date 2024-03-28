def sort_schedule(schedule):
    return sorted(schedule, key=lambda slot: slot[0])


def get_slots_between(start, end):
    slots = []

    while start + 1 <= end:
        slots.append([start, start + 1])

        start += 1

    return slots


def get_free_slots(schedule):
    free_slots = []

    for i in range(len(schedule) - 1):
        if i == 0 and schedule[i][0] > 8:
            free_slots += get_slots_between(start=8, end=schedule[i][0])

        free_slots += get_slots_between(start=schedule[i][1], end=schedule[i + 1][0])

    return free_slots


def get_intersection(first_free_slots, second_free_slots):
    intersection = []

    for slot in first_free_slots:
        if slot in second_free_slots:
            intersection.append(slot)

    for slot in second_free_slots:
        if slot not in intersection and slot in first_free_slots:
            intersection.append(slot)

    return sort_schedule(intersection)


first_schedule = sort_schedule(eval(input()))
second_schedule = sort_schedule(eval(input()))

first_free_slots = get_free_slots(first_schedule)
second_free_slots = get_free_slots(second_schedule)

intersection = get_intersection(first_free_slots, second_free_slots)

print(intersection if len(intersection) > 0 else "infeasible")
