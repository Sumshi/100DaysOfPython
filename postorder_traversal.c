// preoder traversal = root->left->right

// C program for different tree traversals
#include <stdio.h>
#include <stdlib.h>

// A binary tree node has data, pointer to left child
// and a pointer to right child
struct node {
	int data;
	struct node* left;
	struct node* right;
};

// Helper function that allocates a new node with the
// given data and NULL left and right pointers.
struct node* newNode(int data)
{
	struct node* node
		= (struct node*)malloc(sizeof(struct node));
	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return (node);
}

// Given a binary tree, print its nodes according to the
// "bottom-up" postorder traversal.
void printPostorder(struct node* node)
{
	if (node == NULL)
		return;

	// First recur on left subtree
	printPostorder(node->left);

	// Then recur on right subtree
	printPostorder(node->right);

	// Now deal with the node
	printf("%d ", node->data);
}

// Driver code
int main()
{
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);

	// Function call
	printf("Postorder traversal of binary tree is \n");
	printPostorder(root);

	getchar();
	return 0;
}

