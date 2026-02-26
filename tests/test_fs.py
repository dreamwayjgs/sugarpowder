import tempfile
from pathlib import Path

from sugarpowder.fs import create_directory_recursive


def test_create_directory_recursive():
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "a" / "b" / "c"
        create_directory_recursive(str(target))
        assert target.exists()
        assert target.is_dir()


def test_create_directory_recursive_already_exists():
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "a"
        target.mkdir()
        create_directory_recursive(str(target))  # should not raise
        assert target.exists()
