# Using LLMs to generate unit tests

Check the notebook. This is the workflow

- define target function for which to generate unit tests
- call LLM to generate unit test code
- run unit test
- run [test smells](https://github.com/maxpacs98/disertation) to probe for basic desired test properties
- run [`pylint`](https://www.pylint.org/) to analyze generated test quality

