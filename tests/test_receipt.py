import hashlib
def test_fixture():
    assert hashlib.sha1(b"parcel").digest()
