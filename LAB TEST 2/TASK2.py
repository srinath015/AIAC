class YieldTracker:
    """
    Tracks values keyed by unique IDs, allowing add, remove, and summary operations.

    Methods:
        add(id: str, value: float): Adds or updates the value for the given ID.
        remove(id: str): Removes the value for the given ID if present.
        summary() -> tuple[int, float|None]: Returns (count, average) of current values.
    """
    def __init__(self):
        self._data = {}

    def add(self, id, value):
        self._data[id] = value

    def remove(self, id):
        self._data.pop(id, None)

    def summary(self):
        count = len(self._data)
        if count == 0:
            return 0, None
        avg = round(sum(self._data.values()) / count, 2)
        return count, avg

if __name__ == "__main__":
    tracker = YieldTracker()
    print("Enter a list of operations ")
    # Example input: [{'op': 'add', 'id': 'a1', 'value': 22}, {'op': 'add', 'id': 'b2', 'value': 17}, {'op': 'remove', 'id': 'a1'}, {'op': 'add', 'id': 'c3', 'value': 19}]
    try:
        user_input = input()
        # Safely evaluate the input as a list of dicts
        import ast
        ops = ast.literal_eval(user_input)
        if not isinstance(ops, list):
            raise ValueError
    except Exception:
        print("Invalid input format. Please enter a list of operation dictionaries as shown in the sample input.")
        exit(1)

    for op in ops:
        if not isinstance(op, dict) or 'op' not in op or 'id' not in op:
            continue
        if op['op'] == 'add' and 'value' in op:
            try:
                value = float(op['value'])
                tracker.add(op['id'], value)
            except ValueError:
                continue
        elif op['op'] == 'remove':
            tracker.remove(op['id'])
        # Ignore invalid operations

    count, avg = tracker.summary()
    print(f"count={count}, avg={avg}")
