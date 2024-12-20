Python solutions for [Codewars](https://www.codewars.com/dashboard) Katas.

[![](https://github.com/asarkar/codewars-python/workflows/CI/badge.svg)](https://github.com/asarkar/codewars-python/actions)

## Searching for Katas

https://www.codewars.com/kata/search/python?q=&r%5B%5D=-4&xids=completed&beta=false&order_by=satisfaction_percent%20desc%2Ctotal_completed%20desc

## Development

```
codewars...% $(brew --prefix python)/bin/python3 -m venv ./venv

codewars...% ./venv/bin/python -m pip install --upgrade pip '.[test]' '.[lint]'
```

To remove the local copy of the package `pydata`:
```
codewars...% ./venv/bin/python -m pip uninstall -y pydata
```

## Running tests
```
./.github/run.sh <directory>
```