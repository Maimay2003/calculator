name: Check Style
on: push

jobs:
  check-style:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.11.3

      - name: Install tools
        run: python -m pip install --upgrade pip pycodestyle

      - name: Check Style
        run: pycodestyle --first *.py


