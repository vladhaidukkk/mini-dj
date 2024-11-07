import pytest

from hello import main


def test_main(capsys: pytest.CaptureFixture) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from mini-dj!\n"
