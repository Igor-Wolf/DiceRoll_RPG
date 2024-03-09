# diceroll_RPG

Description. 
The package diceroll_RPG is used to:
	- Roll dices with a random function
	- Get the result

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install diceroll

```bash
pip install diceroll_RPG
```

## Usage

```python
from diceroll_RPG import rolling
rolling.rollf()
```

```python
from diceroll_RPG import rolling
rolling.roll()
```

```python
from diceroll_RPG.rolling import rollf, roll

print(rollf("2d3 + 3d4 + 5"))
#(' ( 3 + 1 ) + ( 1 + 4  + 1 ) + ( 5 ) = 15', 15)

print(roll("2d3 + 3d4 + 5"))
#15
```

## Author
Igor Reis Barbosa

## License
[MIT](https://choosealicense.com/licenses/mit/)
