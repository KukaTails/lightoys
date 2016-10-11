#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>

using std::vector;
using std::string;

struct TrieNode {
  char key;
  TrieNode *next[26];
  bool is_end;

  TrieNode(char ch): key(ch), is_end(false)
  {
    memset(next, 0, sizeof(next));
  }
};

class Trie {
public:
  Trie(): root_(new TrieNode('a')) {}

  void Insert(const std::string& word) {
    TrieNode *visitor = root_;

    for (int i = 0; i < word.size(); ++ i) {
      int ch_index = word[i] - 'a';
      if (visitor->next[ch_index]) {
        visitor = visitor->next[ch_index];
      } else {
        visitor->next[ch_index] = new TrieNode(word[i]);
      }
    }
    visitor->is_end = true;
  }

public:
  TrieNode *root_;
};

class Solution {
public:
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    Trie trie;
    board_ = board;
    row_ = board.size();
    column_ = board[0].size();
    visited_ = new int[row_ * column_];
    memset(visited_, 0, sizeof(int*) * row_ * column_);

    for (auto iter = words.cbegin(); iter != words.cend(); ++ iter)
      trie.Insert(*iter);
    for (int i = 0; i < row_; ++ i) {
      for (int j = 0; j < column_; ++ j) {
        set_value(i, j, 1);
        Solve(i, j, trie.root_->next[board[i][j]-'a'], "" + board[i][j]);
        set_value(i, j, 0);
      }
    }
    return ans_;
  }

  int get_value(int i, int j) const {  return visited_[i * column_ + j]; }
  void set_value(int i, int j, int val) { visited_[i * column_ + j] = val; }

  bool pos_valid(int i, int j) const
  {
    if (i < 0 || i >= row_ || j < 0 || j >= column_)
      return false;
    else
      return true;
  }

  void Solve(int i, int j, const TrieNode* node, const std::string& word) {
    if (!pos_valid(i, j) || !node || !node->next[board_[i][j]-'a'])
      return;

    printf("pos=(%d,%d) word=%s", i, j, word.data());
    if (node->next[board_[i][j]-'a']->is_end)
      ans_.push_back(word);

    int direction[8] = {-1, 0, 1, 0, 0, -1, 0, 1};
    for (int i = 0; i + 2 <= 8; i += 2) {
      int new_i = i + direction[i];
      int new_j = j + direction[i+1];

      if (!pos_valid(new_i, new_j) || get_value(new_i,new_j))
        continue;
      set_value(new_i, new_j, 1);
      Solve(new_i, new_j, node->next[board_[i][j]-'a'], word + board_[i][j]);
      set_value(new_i, new_j, 0);      
    }
  }

private:
  std::vector<std::vector<char>> board_;
  int *visited_;
  std::vector<std::string> ans_;
  int row_, column_;
};


// testing
int main(int argc, char **argv)
{
  std::vector<std::vector<char>> board = {{'o', 'a', 'a', 'n'}, {'e', 't', 'a', 'e'},
                                          {'i', 'h', 'k', 'v'}, {'i', 'f', 'l', 'v'}};
  std::vector<std::string> words = {"oath", "pea", "eat", "rain"};

  Solution().findWords(board, words);
  return 0;
}
