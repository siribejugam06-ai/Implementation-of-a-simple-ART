import numpy as np

def art1(data, vigilance=0.8):
    categories = []

    for pattern in data:
        matched = False

        for category in categories:
            intersection = np.minimum(pattern, category)
            similarity = np.sum(intersection) / np.sum(pattern)

            if similarity >= vigilance:
                category[:] = intersection
                matched = True
                break

        if not matched:
            categories.append(pattern.copy())

    return categories


data = np.array([
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0]
])

result = art1(data)

print("ART1 Categories:")
for i, category in enumerate(result, 1):
    print("Category", i, ":", category)
