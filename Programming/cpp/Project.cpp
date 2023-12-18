#include <iostream>
#include <climits>

// Node structure for BST
struct Node {
    int key;
    Node* left;
    Node* right;

    Node(int k) {
        key = k;
        left = right = nullptr;
    }
};

// Binary Search Tree class
class BST {
private:
    

    Node* insertRec(Node* root, int key) {
        if (root == nullptr)
            return new Node(key);

        if (key < root->key)
            root->left = insertRec(root->left, key);
        else if (key > root->key)
            root->right = insertRec(root->right, key);

        return root;
    }

    Node* deleteRec(Node* root, int key) {
        if (root == nullptr)
            return root;

        if (key < root->key)
            root->left = deleteRec(root->left, key);
        else if (key > root->key)
            root->right = deleteRec(root->right, key);
        else {
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

            Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = deleteRec(root->right, temp->key);
        }
        return root;
    }

    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current && current->left != nullptr)
            current = current->left;
        return current;
    }

    int findClosestRec(Node* root, int target, int closest, int& temp) {
        if (root == nullptr)
            return closest;

        if (abs(root->key - target) < abs(closest - target)) {
            temp = closest;
            closest = root->key;
        }
        else if (abs(root->key - target) == abs(closest - target) && closest != temp) {
            int minVal = std::min(root->key, temp);
            closest = std::min(minVal, closest);
        }

        if (target < root->key)
            return findClosestRec(root->left, target, closest, temp);
        else if (target > root->key)
            return findClosestRec(root->right, target, closest, temp);
        else
            return closest;
    }

public:
Node* root;
    BST() {
        root = nullptr;
    }

    void insert(int key) {
        root = insertRec(root, key);
    }

    void remove(int key) {
        root = deleteRec(root, key);
    }

    int findClosest(int target) {
        int closest = INT_MAX;
        int temp = closest;
        return findClosestRec(root, target, closest, temp);
    }

    void inorder(Node* root) {
        if (root == nullptr)
            return;
        inorder(root->left);
        std::cout << root->key << "        ";
        inorder(root->right);
    }
};

int main() {
    BST bst;
    bst.insert(4);
    bst.insert(2);
    bst.insert(1);
    bst.insert(3);
    bst.insert(6);
    bst.insert(5);
    bst.insert(7);

    std::cout << "Closest element to 4: " << bst.findClosest(4) << std::endl;
    std::cout << "Closest element to 2: " << bst.findClosest(2) << std::endl;
    std::cout << "Closest element to 5: " << bst.findClosest(5) << std::endl;

    bst.remove(4);
    std::cout << "Closest element to 4 after deletion: " << bst.findClosest(4) << std::endl;

    bst.inorder(bst.root);

    return 0;
}
