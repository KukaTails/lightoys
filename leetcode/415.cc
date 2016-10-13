class Solution {
public:
  string addStrings(string num1, string num2) {
    std::reverse(num1.begin(), num1.end());
    std::reverse(num2.begin(), num2.end());

    std::string result;
    int carry = 0, rest = 0;
    for (auto iter1 = num1.begin(), iter2 = num2.begin(); iter1 != num1.end() || iter2 != num2.end();) {
      int val1 = iter1 != num1.end() ? (*(iter1++) - '0') : 0;
      int val2 = iter2 != num2.end() ? (*(iter2++) - '0') : 0;

      rest = (val1 + val2 + carry) % 10;
      carry = (val1 + val2 + carry) / 10;
      result.push_back('0' + rest);
    }
    if (carry != 0)
      result.push_back('0' + carry);
    std::reverse(result.begin(), result.end());
    return result;
  }
};
