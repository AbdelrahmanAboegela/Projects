// The operations of the Queue ADT are:
// Enqueue: adds an element to the end of the queue.
// Dequeue: removes and returns the first element of the queue.
// Front: returns the first element of the queue without removing it.
// Rear: returns the last element of the queue without removing it.
// IsEmpty: returns true if the queue is empty, false otherwise.
// Size: returns the number of elements in the queue.
// If implemented using a dynamic array, the complexity of each operation would be:
// Enqueue: O(1) amortized, O(n) worst case if the array needs to be resized.
// Dequeue: O(n) worst case if the array needs to be resized and elements need to be shifted.
// Front: O(1).
// Rear: O(1).
// IsEmpty: O(1).
// Size: O(1).
// Here is an implementation of the Queue ADT using a dynamic array in C++:
#include <iostream>
#include <stdexcept>

using namespace std;

class Queue {
private:
    int front, rear, capacity;
    int* array;
public:
    Queue(int size) {
        front = 0;
        rear = -1;
        capacity = size;
        array = new int[capacity];
    }

    ~Queue() {
        delete[] array;
    }

    void enqueue(int item) {
        if (isFull()) {
            throw overflow_error("Queue is full");
        }
        rear = (rear + 1) % capacity;
        array[rear] = item;
    }

    int dequeue() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        int item = array[front];
        front = (front + 1) % capacity;
        return item;
    }

    int size() {
        return (capacity - front + rear + 1) % capacity;
    }

    bool isEmpty() {
        return (size() == 0);
    }

    bool isFull() {
        return (size() == capacity);
    }

    int frontElement() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        return array[front];
    }

    int rearElement() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        return array[rear];
    }
};
// Here is an implementation of the Queue ADT using a singly linked list in C++:
#include <iostream>
#include <stdexcept>

using namespace std;

template<typename T>
class Queue {
private:
    struct Node {
        T data;
        Node* next;
        Node(T data) {
            this->data = data;
            this->next = nullptr;
        }
    };
    Node* front;
    Node* rear;
    int size;
public:
    Queue() {
        front = nullptr;
        rear = nullptr;
        size = 0;
    }

    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }

    void enqueue(T item) {
        Node* newNode = new Node(item);
        if (isEmpty()) {
            front = newNode;
        } else {
            rear->next = newNode;
        }
        rear = newNode;
        size++;
    }

    T dequeue() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        Node* tempNode = front;
        T item = front->data;
        front = front->next;
        if (front == nullptr) {
            rear = nullptr;
        }
        delete tempNode;
        size--;
        return item;
    }

    int getSize() {
        return size;
    }

    bool isEmpty() {
        return (size == 0);
    }

    T frontElement() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        return front->data;
    }

    T rearElement() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        return rear->data;
    }
};
// Here is an example C++ program that uses the Queue STL:
#include <iostream>
#include <queue>

using namespace std;

int main() {
    queue<int> q;

    q.push(10);
    q.push(20);
    q.push(30);

    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }

    return 0;
}

// The difference between the Queue STL
// and the implementations in the previous 
// questions is that the Queue STL is a pre-built
// implementation of the Queue ADT provided by the
// C++ Standard Template Library (STL). It is optimized 
// for performance and may have additional features that
// the custom implementations do not have. However, the
// custom implementations allow for more control and
// flexibility in how the Queue ADT is

// a. The supported operations of the Deque (Double-Ended Queue) ADT are:

// insertFront(): adds an element to the front of the deque.
// insertRear(): adds an element to the rear of the deque.
// deleteFront(): removes and returns the element at the front of the deque.
// deleteRear(): removes and returns the element at the rear of the deque.
// getFront(): returns the element at the front of the deque without removing it.
// getRear(): returns the element at the rear of the deque without removing it.
// isEmpty(): returns true if the deque is empty, false otherwise.
// size(): returns the number of elements in the deque.
// b. Here are the algorithms for each operation in the Deque using a Doubly Linked List:

// insertFront():

// Create a new node with the given data.
// If the deque is empty, set both front and rear pointers to the new node.
// Otherwise, set the previous pointer of the current front node to the new node, and set the next pointer of the new node to the current front node.
// Set the front pointer to the new node.
// Increment the size of the deque.
// insertRear():

// Create a new node with the given data.
// If the deque is empty, set both front and rear pointers to the new node.
// Otherwise, set the next pointer of the current rear node to the new node, and set the previous pointer of the new node to the current rear node.
// Set the rear pointer to the new node.
// Increment the size of the deque.
// deleteFront():

// If the deque is empty, throw an underflow error.
// Otherwise, store the data of the front node in a temporary variable.
// If the deque has only one node, set both front and rear pointers to null.
// Otherwise, set the next pointer of the front node to the new front node, and set the previous pointer of the new front node to null.
// Delete the old front node.
// Decrement the size of the deque.
// Return the stored data.
// deleteRear():

// If the deque is empty, throw an underflow error.
// Otherwise, store the data of the rear node in a temporary variable.
// If the deque has only one node, set both front and rear pointers to null.
// Otherwise, set the previous pointer of the rear node to the new rear node, and set the next pointer of the new rear node to null.
// Delete the old rear node.
// Decrement the size of the deque.
// Return the stored data.
// getFront():

// If the deque is empty, throw an underflow error.
// Otherwise, return the data of the front node.
// getRear():

// If the deque is empty, throw an underflow error.
// Otherwise, return the data of the rear node.
// isEmpty():

// Return true if the size of the deque is 0, false otherwise.
// size():

// Return the size of the deque.