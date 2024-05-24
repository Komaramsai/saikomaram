import statistics

def find_mode(data):
    try:
        mode_value = statistics.mode(data)
        return mode_value
    except statistics.StatisticsError:
        return "No unique mode found. Multiple values have the same highest frequency."

# Example usage
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
mode = find_mode(data)
print(f"The mode of the dataset is: {mode}")
