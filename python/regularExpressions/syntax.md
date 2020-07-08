# Regular Expression Syntax

```
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check 
if a particular string matches a given regular expression (or if a given regular expression matches a particular string, 
which comes down to the same thing).
```

## Basics

- regular expressions can be concatenated 
- for details on the theory of regular expressions see [here](https://docs.python.org/3/library/re.html#frie09)
- gentler presentation of the basics are in the [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html#regex-howto)
- regular expressions contain both ordinary and special characters

### Ordinary Characters

- ordinary characters like ```R``` or ```o``` that would match themselves

### Special Characters

- characters like `|` or `(` are special characters
- they either stand for classes or ordinary characters, or affect how the expression around them are interpreted
- list of special characters
  - `.` matches any character except a newline; with DOTALL flag it matches any character uncluding newline
  - `^` matches the start of a string; with MULTILINE matches after each newline
  - `$` matches the end of a string or just before the newline; 
  - `*` causes RE to match 0 or more repetitions of the preceding RE; `ab*` matches `a`, `ab` or `a` with any amount of `b` &rarr; greedy
  - `+` causes RE to match 1 or more repetitions of the preceding RE &rarr; greedy
  - `?` causes RE to match 0 or 1 repitions of the preceding RE &rarr; greedy
  - `*?`, `+?`, `??` adding `?` after a greedy qualifier makes it perform a non-greedy match
  - `{m}`
  - `{m,n}`
  - `{m,n}?`
  - `\`
  - `[]`
  - `|`
  - `(...)`
  - `(?...)`
  - `(?aiLmsux)`
  - `(?:...)`
  - `(?aiLmsux-imsx:...)`
  - `(?P<name>...)`
  - `(?P=name)`
  - `(?#...)`
  - `(?=...)`
  - `(?!...)`
  - `(?<=...)`
  - `(?<!...)`
  - `(?(id/name)yes-pattern|no-pattern)`
  - `\number`
  - `\A` 
  - `\b`
  - `\B`
  - `\d` 
  - `\D`
  - `\s`
  - `\S`
  - `\w`
  - `\W`
  - `\Z`

### Repetition classifiers

- `*`, `*`, `?`, `{m,n}` etc are classifiers and CANNOT be nested directly
- e.g. `(?:a{6})*` watches for any multiple of six `a` characters

## Module Contents
