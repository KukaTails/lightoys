class Solution {
public:
  string getHint(string secret, string guess) {
    int bull = 0, cows = 0;

    std::map<char, int> ch_map;
    std::for_each(secret.begin(), secret.end(), [&](char ch) {
        if (ch_map.find(ch) == ch_map.end())
          ch_map[ch] = 1;
        else
          ++ch_map[ch];
      });
    for (auto iter = guess.begin(); iter != guess.end(); ++ iter) {
      if (ch_map.find(*iter) != ch_map.end() && ch_map[*iter] != 0) {
        --ch_map[*iter];
        ++cows;
      }
    }
    for (int i = 0; i < secret.size(); ++ i) {
      if (secret[i] == guess[i])
        ++bull;
    }
    return std::to_string(bull) + "A" + std::to_string(cows-bull) + "B";
  }
};
