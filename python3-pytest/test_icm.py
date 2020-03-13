import pytest
import main
"""
run from command line with
pytest test_icm.py
Note: capsys is a built-in pytest fixture,
"""
@pytest.fixture
def linef(capsys):
    main.main()
    output,err = capsys.readouterr()
    lines =  output.split('\n')
    return lines

def test_name(linef):
    data = linef[0].split(':')
    assert "Name" == data[0]
    assert data[1]

def test_flavor(linef):
    data = linef[1].split(':')
    assert "Flavor" == data[0] 
    assert data[1]

def test_tub_volume(linef):
    data = linef[2].split(':')
    assert "Tub" == data[0] 
    assert pytest.approx(779.7040267128167) == float(data[1])

def test_scoop_volume(linef):
    data = linef[3].split(':')
    assert "Sphere" == data[0]
    assert pytest.approx(4.1887902047863905) == float(data[1])

def test_servings(linef):
    data = linef[4].split(':')
    assert "Servings" == data[0]
    assert pytest.approx(186.140625) == float(data[1])
              
def test_code_quality():
    from pylint import epylint as lint
    (pylint_stdout, pylint_stderr) = lint.py_run('main.py', return_std=True)
    expected = "Your code has been rated at 10.00/10"
    actual = pylint_stdout.getvalue()
    assert expected in actual
