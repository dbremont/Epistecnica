---
tags: [tool]
---

# Flex

- [GNU Bison](note.html?n=technica/computation/language-system/conceptual-model-language-system/gnu-bison.md)

> Flex is a program that takes a Grammar Spec and generates a Lexical Analyzer.
> 

> A Lexical Analyzer is a coroutine sinse it has memory of the last work.
> 

```c
// fb1-1.l/* state / variables */%{    int chars = 0;    int words = 0;    int lines = 0;%}/* patterns / actions */%%    [a-zA-Z]+ { words++; chars += strlen(yytext); }    \n { chars++; lines++; }    . { chars++; }%%/* computation */main(int argc, char **argv){    yylex();    printf("%8d%8d%8d\n", lines, words, chars);}
```

```bash
flex fb1-1.lcc lex.yy.c -lfl./a.out < echo "The boy stood on the burning deckshelling peanuts by the peck"
```

## Intrinsic

- `yylex`: Return the next **token**.
- `yyin`: This is a file pointer variable that represents the input stream used by lex to read input. By default, yyin is set to stdin, but you can change it to read from a file or any other input source.
- `yyout`: This is a file pointer variable that represents the output stream used by lex for writing output. By default, yyout is set to stdout, but you can redirect it to a file or any other output destination.
- `yytext`: This is a character array that stores the matched input token. It contains the text corresponding to the matched pattern defined in your lexical rules.
- `yylineno`: This variable holds the current line number being processed by yylex. It is typically used to track the line number for error reporting or debugging purposes.
- `yywrap`: This function is called by yylex when it reaches the end of input. By default, it returns 1 to indicate the end of input, but you can redefine it to handle situations where multiple input sources need to be processed.

## Scanning

- Flex scanners reaad from the standard input unless you tell them **otherwise**.

## References

- [Flex](https://en.wikipedia.org/wiki/Flex_(lexical_analyser_generator))
- [Flex Tutorial](https://www.geeksforgeeks.org/flex-fast-lexical-analyzer-generator/)
- [Lex − A Lexical Analyzer Generator](http://mbzz.de/unix/ultrix/etc/lex.pdf)