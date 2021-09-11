# Dir Diff

Display file name diffs of two directories.

The intended use case is to easily spot missing files across directories expected to contain the same files in different formats.

For example, given the following directories:

```
json
 - a.json
 - b.json
yml
 - a.yml
 - c.yml
```

the expected output would be:

```
==================
| json   | yml   |
==================
| b.json | c.yml |
==================
```
