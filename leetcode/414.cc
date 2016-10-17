class Solution {
public:
  int thirdMax(vector<int>& nums) {
    long long int values[3];

    std::fill_n(values, 3, std::numeric_limits<long long int>::min());
    for (int i = 0; i < nums.size(); ++ i) {
      if (nums[i] > values[0]) {
        values[2] = values[1];
        values[1] = values[0];
        values[0] = nums[i];
      } else if (values[0] > nums[i] && nums[i] > values[1]) {
        values[2] = values[1];
        values[1] = nums[i];
      } else if (values[1] > nums[i] && nums[i] > values[2]) {
        values[2] = nums[i];
      }
    }

    return (values[2] == std::numeric_limits<long long int>::min()) ? values[0] : values[2];
  }
};
