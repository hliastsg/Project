import datetime

def PrintHeaderInfo():
    print(datetime.datetime.now())
    print("Hlias Tsiggelis p16148")
    print("------------------------------------")
    print("Project4 gets a list of numbers and calcuates the standard deviation ")
    print("without using the 2 max and min values of this array")
    print("------------------------------------")
    print("Using python 2.7")
    print("------------------------------------")
    print("Prerequisite: None")
    print("------------------------------------")

def first_smaller(numbers):
    minimum1 = min(numbers)
    return minimum1

def first_largest(numbers):
    maximum1 = max(numbers)
    return maximum1

def remove_element(array,index):
    try:
        del array[index]
    except:
        pass
    return array

def calculate_std(array):
    sum = 0
    for i in array:
        sum = sum + i
    mean = sum / len(array)
    variance = 0
    for i in range(len(array)):
        variance = variance + (array[i] - mean) * (array[i] - mean)
    variance = variance / len(array)
    return variance^(1/2)

def get_the_array():
    array = raw_input("Give the list of numbers using space as seperator (eg 1 2 3  etc) : ")
    return map(int,array.split())

if __name__ == '__main__':
        PrintHeaderInfo()

        array = get_the_array()
        length = len(array)
        print ("Lenght of array is ", length-1)
        print ("The array is ", array)

        print ("1st maximum value is :", first_largest(array), "at position :", array.index(first_largest(array)) )
        print ("The array, after removing elements is ", remove_element(array,array.index(first_largest(array))))

        print ("2nd maximum value is :", first_largest(array), "at position :", array.index(first_largest(array)))
        print ("The array, after removing elements is ", remove_element(array, array.index(first_largest(array))))

        print ("1st minimum value is :", first_smaller(array), "at position :", array.index(first_smaller(array)))
        print("The array, after removing elements is ", remove_element(array, array.index(first_smaller(array))))

        print ("2nd minimum value is :", first_smaller(array), "at position :", array.index(first_smaller(array)))
        print("The array, after removing elements is ", remove_element(array, array.index(first_smaller(array))))

        print ("Standard Deviation of array is ", calculate_std(array))

