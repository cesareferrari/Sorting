def simple_implementation(arr):
    # loop from 1 to end of array
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i # j is keeping track of where to swap

        while j > 0 and temp < arr[j - 1]:
            # copy element to left to this position
            arr[j] = arr[j - 1]

            j -= 1

        arr[j] = temp

    return arr



# Sorting books

class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} in {self.genre}"


books = [
        Book("Melville", "Moby Dick", "whale stories"),
        Book("Hamlet", "Immortal William", "Danish prices"),
        ]

def insertion_sort(books):
    for 1 in range(1, len(books)):
        temp = books[i]

        j = i

        # while we are not at front of list and these two should be swapped
        while j > 0 and temp.genre < books[j - 1].genre:
            books[j] = books[j - 1]
            j -= 1

        books[j] = temp

    return books



