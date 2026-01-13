#include <stdbool.h>
#include <stddef.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * struct TreeNode *left;
 * struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int targetSum) {
    // 1. Base Case: If the tree is empty, there is no path.
    if (root == NULL) {
        return false;
    }

    // 2. Check if this is a leaf node
    // A leaf has no children. If we are at a leaf, we check if
    // the current node's value matches the remaining targetSum.
    if (root->left == NULL && root->right == NULL) {
        return root->val == targetSum;
    }

    // 3. Recursive Step (DFS)
    // We subtract the current node's value from the targetSum
    // and continue the search in the left and right children.
    int newTarget = targetSum - root->val;
    
    return hasPathSum(root->left, newTarget) || hasPathSum(root->right, newTarget);
}