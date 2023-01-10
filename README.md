# ci-cd-python

Project to check python coverage scripts.

```
How to test with pytest + coverage
1 - First
coverage run -m pytest
2 - Second 
coverage report -m --omit="*/test*"
3 - Last
coverage xml
```

# Report test

```
pytest --junitxml report.xml
```

## Check Coverage

This part of the code checks if the coverage is higher than 80%.

```
COVER=$(xmllint --xpath 'string(/coverage/@line-rate)' coverage.xml)
echo $COVER
if [[ $COVER > 0.8 ]]; then
  echo "Boa cobertura"
else
  echo "Cobertura a ser melhorada"
fi
```