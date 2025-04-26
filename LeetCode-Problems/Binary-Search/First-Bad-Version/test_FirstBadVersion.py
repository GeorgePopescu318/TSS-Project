import pytest

def isBadVersion(version: int) -> bool:
    return version >= 4

def firstBadVersion(n: int) -> int:
    for version in range(1, n + 1):
        if isBadVersion(version):
            return version
    return -1  # added a return statement for the scenario where no bad versions are detected

class TestFirstBadVersion:
    def test_first_bad_version_found(self):
        assert firstBadVersion(5) == 4, "Should return 4 for versions 1-5"

    def test_all_versions_good(self):
        global isBadVersion
        original_isBadVersion = isBadVersion
        isBadVersion = lambda x: False
        assert firstBadVersion(3) == -1, "Should return -1 when all versions are good"
        isBadVersion = original_isBadVersion

    def test_first_version_bad(self):
        global isBadVersion
        original_isBadVersion = isBadVersion
        isBadVersion = lambda x: True if x >= 1 else False
        assert firstBadVersion(3) == 1, "Should return 1 when the first version is bad"
        isBadVersion = original_isBadVersion

    def test_no_versions(self):
        assert firstBadVersion(0) == -1, "Should return -1 when there are no versions"

    def test_large_n(self):
        assert firstBadVersion(1000) == 4, "Should return 4 even for large n"
