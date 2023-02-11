from os import remove


def find_unique_numbers(numbers):
    list_1=numbers
    output = []
    for x in list_1:
        if x not in output:
            output.append(x)
        else: output.remove(x)
    return output
if __name__ == "__main__":
    print(find_unique_numbers([1, 2,2]))


