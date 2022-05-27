"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_char_counts = {}
        magazine_char_counts = {}

        for c in ransomNote:
            ransom_note_char_counts[c] = ransom_note_char_counts.get(c, 0) + 1
        for c in magazine:
            magazine_char_counts[c] = magazine_char_counts.get(c, 0) + 1

        for c in ransom_note_char_counts:
            if not c in magazine_char_counts or magazine_char_counts[c] < ransom_note_char_counts[c]:
                return False

        return True