import time

from sugarpowder.tick import tick


def test_tick_returns_float():
    t = tick()
    assert isinstance(t, float)


def test_tick_returns_increasing_time():
    t1 = tick()
    time.sleep(0.01)
    t2 = tick(t1)
    assert t2 > t1


def test_tick_prints_elapsed(capsys):
    t = tick()
    time.sleep(0.01)
    tick(t)
    output = capsys.readouterr().out
    assert "Elapsed:" in output


def test_tick_prints_label(capsys):
    t = tick()
    tick(t, label="step 1")
    output = capsys.readouterr().out
    assert "Elapsed step 1:" in output


def test_tick_prints_msg(capsys):
    t = tick()
    tick(t, msg="데이터 로딩")
    output = capsys.readouterr().out
    assert "/ 데이터 로딩" in output


def test_tick_label_and_msg(capsys):
    t = tick()
    tick(t, label="step 1", msg="완료")
    output = capsys.readouterr().out
    assert "Elapsed step 1:" in output
    assert "/ 완료" in output


def test_tick_prints_caller_location(capsys):
    t = tick()
    tick(t)
    output = capsys.readouterr().out
    assert "test_tick_prints_caller_location" in output


def test_tick_no_output_without_since(capsys):
    tick()
    output = capsys.readouterr().out
    assert output == ""
