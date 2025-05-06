def activity_selection(start_times, finish_times):
    """
    we have to selects the maximum number of activities that don't overlap.
    
    Parameters:
        start_times (list): A list of start times of activities.
        finish_times (list): A list of finish times of activities.
        
    Returns:
        list: A list of indices of the selected activities.
    """
    # Combine start and finish times with their indices
    activities = list(enumerate(zip(start_times, finish_times)))
    
    # Here we sort activities by their finish times
    activities.sort(key=lambda x: x[1][1])

    selected_activities = []
    last_finish_time = 0

    for index, (start, finish) in activities:
        if start >= last_finish_time:
            selected_activities.append(index)
            last_finish_time = finish

    return selected_activities

