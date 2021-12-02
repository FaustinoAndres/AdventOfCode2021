
def read_file():

    data = []
    with open('data.txt', 'r') as f:
        for line in f:
            data.append(int(line.strip()))

    return data

def count_increases(data):

    count = 0

    for i in range(3, len(data)):
        count += int((data[i])>data[i-3])

    return count


if __name__ == '__main__':

    data = read_file()
    count = count_increases(data)
    print(count)

