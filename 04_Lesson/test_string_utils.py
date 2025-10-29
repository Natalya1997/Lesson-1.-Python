import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected', [
    ('i am', 'I am'),
    ('tired', 'Tired'),
    ('because of', 'Because of'),
    ('Python', 'Python')
])

def test_capitalize_positive(input_text, expected):
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_text, expected', [
    ('123abc', '123abc'),
    ('', ''),
    ('   ', '   '),
])
def test_capitalize_negative(input_text, expected):
    assert string_utils.capitalize(input_text) == expected

@pytest.mark.positive
@pytest.mark.parametrize(
    'input_text, expected',
    [
        ('    python', 'python'),
        ('    Python', 'Python'),
        ('Hello, Python', 'Hello, Python'),
        ('    Python is difficult', 'Python is difficult'),
        ('    python is cool', 'python is cool'),
        ('    123', '123'),
        ('123python', '123python'),
        ('  ', ''),
        ('', ''),
    ],
)

def test_trim_positive(input_text, expected):
    assert string_utils.trim(input_text) == expected 
    
@pytest.mark.negative
@pytest.mark.parametrize("input_text", [
    (None),
    (123),
    [' python '],
])
def test_trim_negative(input_text):
    with pytest.raises(TypeError):
        string_utils.trim(input_text)
        

@pytest.mark.positive
@pytest.mark.parametrize(
    'text, symbol',
    [
        ('Happy', 'H'),
        ('Flower', 'wer'),
        ('girl', 'g'),
        ('python123', '1'),
        ('89python', '89p'),
        ('tree12', '12'),
    ],
)

def test_contains_positive(text, symbol):
    assert string_utils.contains(text, symbol) is True
    
@pytest.mark.negative
@pytest.mark.parametrize(
    'text, symbol',
    [
        ('I want to cry', 'H'),
        ('sad', 'w'),
        ('Python', 'p'),
        ('finish', '11'),
    ],
)

def test_contains_negative(text, symbol):
    assert string_utils.contains(text, symbol) is False
    
@pytest.mark.positive
@pytest.mark.parametrize(
    'text, symbol, expected',
    [
        ('HappyHouse', 'House', 'Happy'),
        ('123Python', '123', 'Python'),
        ('rainbows89', 's89', 'rainbow'),
        ('HTTPS', 'S', 'HTTP'),
        ('disgusting', 'dis', 'gusting'),
        ('tree', 't', 'ree'),
    ],
)

def test_delete_symbol_positive(text, symbol, expected):
    assert string_utils.delete_symbol(text, symbol) == expected
    

@pytest.mark.negative
@pytest.mark.parametrize(
    'text, symbol, expected',
    [
        ('I want to scream', 'H', 'I want to scream'),
        ('outloud', '', 'outloud'),
        ('', 'p', ''),
        ('titired', 'ti', 'red'),
    ],
)

def test_delete_symbol_negative(text, symbol, expected):
    assert string_utils.delete_symbol(text, symbol) == expected