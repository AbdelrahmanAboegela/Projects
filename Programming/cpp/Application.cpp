#include <iostream>
#include <string>

struct Contact {
    std::string name;
    std::string phoneNumber;

    Contact(const std::string& n, const std::string& num) {
        name = n;
        phoneNumber = num;
    }

    Contact() {
        name = "";
        phoneNumber = "";
    }
};

struct Node {
    Contact contact;
    Node* left;
    Node* right;

    Node(const Contact& c) {
        contact = c;
        left = right = nullptr;
    }

    Node() {
        contact = Contact();
        left = right = nullptr;
    }
};

class ContactManager {
private:
    Node* root;

    Node* insertRec(Node* root, const Contact& contact) {
        if (root == nullptr)
            return new Node(contact);

        if (contact.name < root->contact.name)
            root->left = insertRec(root->left, contact);
        else if (contact.name > root->contact.name)
            root->right = insertRec(root->right, contact);

        return root;
    }

    Node* searchRec(Node* root, const std::string& name) {
        if (root == nullptr || root->contact.name == name)
            return root;

        if (name < root->contact.name)
            return searchRec(root->left, name);
        else
            return searchRec(root->right, name);
    }

    Node* findMinNode(Node* root) {
        if (root == nullptr || root->left == nullptr)
            return root;

        return findMinNode(root->left);
    }

    Node* deleteRec(Node* root, const std::string& name) {
        if (root == nullptr)
            return root;

        if (name < root->contact.name)
            root->left = deleteRec(root->left, name);
        else if (name > root->contact.name)
            root->right = deleteRec(root->right, name);
        else {
            // Node to be deleted found

            // Case 1: No child or one child
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            // Case 2: Two children
            Node* minNode = findMinNode(root->right);
            root->contact = minNode->contact;
            root->right = deleteRec(root->right, minNode->contact.name);
        }

        return root;
    }

    Node* findClosestRec(Node* root, const std::string& name, Node* closest) {
        if (root == nullptr)
            return closest;

        if (name == root->contact.name)
            return root;

        if (name < root->contact.name) {
            if (closest == nullptr || root->contact.name < closest->contact.name)
                closest = root;
            return findClosestRec(root->left, name, closest);
        }
        else {
            if (closest == nullptr || root->contact.name > closest->contact.name)
                closest = root;
            return findClosestRec(root->right, name, closest);
        }
    }

public:
    ContactManager() {
        root = nullptr;
    }

    void addContact(const std::string& name, const std::string& phoneNumber) {
        Contact contact(name, phoneNumber);
        root = insertRec(root, contact);
    }

    void searchContact(const std::string& name) {
        Node* result = searchRec(root, name);
        if (result != nullptr)
            std::cout << "Contact Found - Name: " << result->contact.name << ", Phone Number: " << result->contact.phoneNumber << std::endl;
        else
            std::cout << "Contact Not Found" << std::endl;
    }

    void deleteContact(const std::string& name) {
        root = deleteRec(root, name);
    }

    void findClosestContact(const std::string& name) {
        Node* closest = nullptr;
        closest = findClosestRec(root, name, closest);

        if (closest != nullptr)
            std::cout << "Closest Contact - Name: " << closest->contact.name << ", Phone Number: " << closest->contact.phoneNumber << std::endl;
        else
            std::cout << "No Closest Contact Found" << std::endl;
    }

    void findMinContact() {
        Node* minNode = findMinNode(root);
        if (minNode != nullptr)
            std::cout << "Minimum Contact - Name: " << minNode->contact.name << ", Phone Number: " << minNode->contact.phoneNumber << std::endl;
        else
            std::cout << "Contact List is Empty" << std::endl;
    }

    Node* getRoot() {
        return root;
    }
};

void printTree(Node* root, int depth = 0) {
    if (root == nullptr) {
        return;
    }

    for (int i = 0; i < depth; ++i) {
        std::cout << "  ";
    }
    std::cout << root->contact.name << std::endl;

    printTree(root->left, depth + 1);
    printTree(root->right, depth + 1);
}

int main() {
    ContactManager contactManager;

    contactManager.addContact("Alice", "1234567890");
    contactManager.addContact("Bob", "9876543210");
    contactManager.addContact("Charlie", "5555555555");

    contactManager.searchContact("Alice");
    contactManager.searchContact("Dave");

    contactManager.deleteContact("Bob");

    contactManager.findClosestContact("Charlie");

    contactManager.findMinContact();

    // Call the printTree() function with the root node obtained from getRoot()
    printTree(contactManager.getRoot());

    return 0;
}
