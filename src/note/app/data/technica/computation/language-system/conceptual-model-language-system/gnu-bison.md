---
tags: [language-system, tool]
---

# GNU Bison

- [Flex](note.html?n=technica/computation/language-system/conceptual-model-language-system/flex.md)

```c
/* Declarations */%{#include <stdio.h>%}%token NUMBER%token ADD SUB MUL DIV ABS%token EOL// Rules%%calclist: /* nothing */ matches at beginning of input| calclist exp EOL { printf("= %d\n", $1); } EOL is end of an expression;exp: factor default $$ = $1| exp ADD factor { $$ = $1 + $3; }| exp SUB factor { $$ = $1 - $3; };factor: term default $$ = $1| factor MUL term { $$ = $1 * $3; }| factor DIV term { $$ = $1 / $3; };term: NUMBER default $$ = $1| ABS term { $$ = $2 >= 0? $2 : - $2; };%%// Computationmain(int argc, char **argv){    yyparse();}yyerror(char *s){    fprintf(stderr, "error: %s\n", s);}
```

## Intrinsics

**Yacc (Yet Another Compiler-Compiler)** is a tool that generates parsers based on a formal grammar specification. In Yacc, the building blocks of a grammar specification are rules, tokens, and actions. Here is a list of some commonly used functions and variables in Yacc:

Functions: - **yyparse()**: The main function that starts the parsing process. - **yylex()**: A function that returns the next token in the input stream. - **yyerror(const char *s): A function called when a syntax error occurs, typically used for error handling. - yywrap(): A function that is called when the end of the input is reached. It is used to indicate the end of parsing. - yyrestart(FILE* file)**: A function to change the input source during parsing.

Variables: - **yyval**: A variable that holds the value of the semantic action associated with a production rule. - **yytext**: A variable that holds the text of the current token. - **yylval**: A variable that holds additional semantic information associated with a token. - **yylineno**: A variable that represents the current line number in the input file. - **yyin**: A variable that represents the input file stream. - **yyout**: A variable that represents the output file stream. - **yylloc**: A variable that holds location information (filename, line, and column) for the current token.

These are some of the common functions and variables used in Yacc. However, it’s important to note that the specific set of functions and variables can vary depending on the implementation and version of Yacc being used.

## Parsing Strategies

Yacc uses the shift-reduce parser.

## References

[GNU Bison](https://en.wikipedia.org/wiki/GNU_Bison)

Levine, John. [Flex & Bison: Text Processing Tools](https://web.iitd.ac.in/~sumeet/flex__bison.pdf). " O’Reilly Media, Inc.", 2009.

[YACC: A Parser Generator](https://cgi.di.uoa.gr/~thp06/12_13/09_10/yacc.pdf)