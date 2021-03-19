def integers():
    """Implement state-aware integers generator."""
    if not hasattr(integers, 'state'):
        integers.state = 0
    while True:
        integers.state += 1
        yield integers.state
