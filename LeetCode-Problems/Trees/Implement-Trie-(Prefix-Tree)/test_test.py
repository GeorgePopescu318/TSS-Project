import pytest
from test import Trie  # Replace with the actual module name

@pytest.fixture
def trie():
    return Trie()

def test_insert_and_search(trie):
    # Test inserting and searching single word
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    
    # Test inserting and searching multiple words
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("apple") is True

def test_search_non_existent_word(trie):
    # Test searching for a word that does not exist
    assert trie.search("banana") is False

def test_starts_with(trie):
    # Test prefix checking with existing words
    trie.insert("apple")
    assert trie.startsWith("app") is True
    assert trie.startsWith("appl") is True
    assert trie.startsWith("apple") is True
    assert trie.startsWith("banana") is False

    # Test prefix with partially matching word
    trie.insert("ban")
    assert trie.startsWith("ban") is True
    assert trie.startsWith("banan") is False

def test_insert_duplicate_words(trie):
    # Test inserting the same word multiple times
    trie.insert("apple")
    trie.insert("apple")
    assert trie.search("apple") is True

def test_case_sensitivity(trie):
    # Test case sensitivity of implementation
    trie.insert("Apple")
    assert trie.search("Apple") is True
    assert trie.search("apple") is False
    assert trie.startsWith("App") is True
    assert trie.startsWith("app") is False

def test_empty_string(trie):
    # Test edge case of inserting and searching empty string
    trie.insert("")
    assert trie.search("") is True
    assert trie.startsWith("") is True
