struct Record {
  int val1, val2;
  Record(int x, int y): val1(x), val2(y) {}
  bool operator <(const Record& rhs) const { return val1 + val2 >= rhs.val1 + rhs.val2; }
  std::pair<int, int> GetPair() const { return std::pair<int, int>(val1, val2); }
};

class Solution {
public:
  vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    std::priority_queue<Record> heap;

    for (int i = 0; i < k && i < nums1.size(); ++ i) {
      for (int j = 0; j < k && j < nums2.size(); ++ j) {
        int val1 = nums1[i], val2 = nums2[j];
        heap.push(Record(val1, val2));
      }
    }

    std::vector<pair<int, int>> result;
    while (result.size() < k && heap.size() > 0) {
      Record tmp = heap.top();
      heap.pop();
      result.push_back(tmp.GetPair());
    }
    return result;
  }
};
