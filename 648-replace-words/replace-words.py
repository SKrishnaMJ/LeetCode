class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


# Convert dictionary to a set for faster lookup
        dictionary_set = set(dictionary)

        # Split the sentence into words
        words = sentence.split()

        # Initialize an empty list to store the final result
        result = []

        # For each word in the sentence
        for word in words:
            prefix_found = False
            # Check for each prefix starting from the shortest
            for i in range(1, len(word) + 1):
                # If a prefix is found in the dictionary, append it and break
                if word[:i] in dictionary_set:
                    result.append(word[:i])
                    prefix_found = True
                    break
            # If no prefix is found, append the original word
            if not prefix_found:
                result.append(word)

        # Join the result list into a string and return
        return ' '.join(result)

        