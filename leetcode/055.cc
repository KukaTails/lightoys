class Solution {
public:
  bool canJump(vector<int>& nums) {
    int index = 0;
    while (index < nums.size()) {
      int end = index + nums[index];

      int max_index = end;
      for (int j = index+1; j <= max_index && j < nums.size(); ++ j) {
        if (j + nums[j] > max_index)
          max_index = j + nums[j];
      }
      index = max_index;
      if (index >= nums.size()-1)
        return true;
      if (nums[index] == 0 && index != nums.size() - 1)
        return false;
    }
    return index >= nums.size();
  }
};

