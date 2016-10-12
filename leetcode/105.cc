/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    return Helper(preorder.begin(), preorder.end(), inorder.begin(), inorder.end());
  }

  TreeNode* Helper(std::vector<int>::iterator p_start, std::vector<int>::iterator p_end,
                   std::vector<int>::iterator i_start, std::vector<int>::iterator i_end)
  {
    if (p_start == p_end || i_start == i_end)
      return nullptr;

    int root_val = *p_start;
    TreeNode *root = new TreeNode(root_val);
    auto root_iter = std::find(i_start, i_end, root_val);
    TreeNode *left = Helper(p_start + 1, p_start + 1 + std::distance(i_start, root_iter), i_start, root_iter);
    TreeNode *right = Helper(p_start + 1 + std::distance(i_start, root_iter), p_end, root_iter + 1, i_end);
    root->left = left;
    root->right = right;
    return root;
  }
};
