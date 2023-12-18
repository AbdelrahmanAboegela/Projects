#include <iostream>
#include <stdexcept>

class Queue {
private:
    struct Node {
        int data;
        Node* next;
        Node(int data) {
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
        while (front != nullptr) { 
            dequeue();
        }
    }

    void enqueue(int item) {
        Node* newNode = new Node(item);
        if (front == nullptr) { 
            front = newNode;
        } else {
            rear->next = newNode;
        }
        rear = newNode;
        size++;
    }

    int dequeue() {
        if (front == nullptr) {
            throw std::underflow_error("Queue is empty");
        }
        Node* tempNode = front;
        int item = front->data;
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

};
