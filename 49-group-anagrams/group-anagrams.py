class Solution(object):
    def groupAnagrams(self, strs):
        my_dict = defaultdict(list)
        for words in strs:
            sort_word = ''.join(sorted(words))
            my_dict[sort_word].append(words)
        return my_dict.values()
        