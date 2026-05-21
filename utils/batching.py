def create_batches(data, batch_size):

    batches = []

    for i in range(0, len(data), batch_size):
        batches.append(data[i:i+batch_size])

    return batches