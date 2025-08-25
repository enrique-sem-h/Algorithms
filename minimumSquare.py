def minimumSquareSize(width, height):
    biggest = max(height, width)
    smallest = min(height, width)

    if biggest % smallest == 0:
        return smallest
    
    else:
        return minimumSquareSize(biggest % smallest, smallest)

def gcd(width, height):
    area = width * height
    while height != 0:
        width, height = height, width % height
    return (width, area // width ** 2)

print(gcd(4, 6))