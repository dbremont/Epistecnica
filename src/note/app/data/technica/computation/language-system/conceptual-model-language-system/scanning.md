---
tags: [language-system]
---

# Scanning

- [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md)

> **Scanning or Lexing**: A **scanner** (or **lexer**) takes in the linear stream of characters and **chunks them together** into a **series of something** more akin to “words”. In programming languages, each of these words is called a **token**. Some tokens are single characters, like `(` and `,`. Others may be several characters long, like numbers (`123`), string literals (`"hi!"`), and identifiers (`min`).
> 

\

- How to think about Scanning?
- What issues arise in grammars where a given input can map to multiple tokens? How to prove that a grammar is non-ambigous (one to one)?
- What types of process doe  a **Deterministic Finite Automaton (DFA)** can Represent?

## Strategy

> What are the different Scanning Strategies?
> 

| **Strategy** | **Description** | **Determinism** | **Context Sensitivity** | **Performance** |
| --- | --- | --- | --- | --- |
| **DFA-based** | Uses a deterministic finite automaton derived from regular expressions; transitions are fixed and unambiguous. | Deterministic | None | Very high — linear in input length. |
| **NFA-based** | Simulates multiple active states of a non-deterministic automaton; simpler to build but slower to execute. | Non-deterministic | None | Moderate — may require parallel state tracking. |
| **Backtracking** | Explores multiple token matches, reverting when a path fails; enables context-dependent decisions. | Non-deterministic | Optional | Variable — can degrade to exponential in worst cases. |
| **Longest-match / Priority** | Chooses the longest possible token, or highest-priority rule if ties occur; resolves overlapping regexes. | Deterministic | None | High — typically linear; small overhead for tie-breaking. |
| **Table-driven** | Implements state transitions through lookup tables rather than code logic; often generated automatically. | Deterministic | None | Moderate — slower than direct-coded DFAs due to table lookups. |
| **Context-sensitive** | Tokenization depends on parser or semantic context (e.g., typedefs, indentation). | Contextual | High | Variable — depends on grammar complexity and context interaction. |
| **Incremental** | Maintains lexer state across input updates for streaming or interactive environments. | Deterministic | Contextual | High for incremental updates; excellent for IDEs or real-time analysis. |

## Case Study

```bash
# DFA-based lexer for a simple grammar
# Tokens: IDENT ([A-Za-z][A-Za-z0-9]*), NUMBER ([0-9]+), PLUS, STAR, LPAREN, RPAREN, WS (skipped)
# We'll implement a table-driven DFA and a maximal-munch scanner:
from typing import List, Tuple, Optional

# Character classes
def char_class(ch: str) -> str:
    if ch.isalpha():
        return "LETTER"
    if ch.isdigit():
        return "DIGIT"
    if ch in "+":
        return "PLUS"
    if ch in "*":
        return "STAR"
    if ch in "(":
        return "LPAREN"
    if ch in ")":
        return "RPAREN"
    if ch.isspace():
        return "WS"
    return "OTHER"

# DFA transition table: state -> {char_class: next_state}
# We'll design states:
# 0: start
# 1: in identifier (accept ID)
# 2: in number (accept NUM)
# 3: saw '+' (accept PLUS)  - single-char accept
# 4: saw '*' (accept STAR)
# 5: saw '(' (accept LPAREN)
# 6: saw ')' (accept RPAREN)
# 7: in whitespace (accept WS)
transitions = {
    0: {"LETTER": 1, "DIGIT": 2, "PLUS": 3, "STAR": 4, "LPAREN": 5, "RPAREN": 6, "WS": 7},
    1: {"LETTER": 1, "DIGIT": 1},  # identifier: letters or digits continue
    2: {"DIGIT": 2},               # number: digits continue
    7: {"WS": 7},                  # whitespace continues
    # accepting single-char states have no outgoing transitions (will be handled by maximal-munch logic)
}

# Accepting states -> token type (WS will be skipped)
accepting = {
    1: "IDENT",
    2: "NUMBER",
    3: "PLUS",
    4: "STAR",
    5: "LPAREN",
    6: "RPAREN",
    7: "WS"
}

# Scanner implementing maximal munch using the DFA above
def lex(input_text: str) -> List[Tuple[str, str, int, int]]:
    """
    Returns list of tokens as tuples: (token_type, lexeme, start_pos, end_pos)
    Raises ValueError on lexical error.
    """
    i = 0
    n = len(input_text)
    tokens = []
    while i < n:
        state = 0
        last_accept_state: Optional[int] = None
        last_accept_pos: Optional[int] = None
        j = i
        # advance through input until no transition is defined
        while j < n:
            cls = char_class(input_text[j])
            if state in transitions and cls in transitions[state]:
                state = transitions[state][cls]
                j += 1
                if state in accepting:
                    last_accept_state = state
                    last_accept_pos = j
            else:
                # no transition from current state with this char_class
                break
        # If we consumed zero chars at start, maybe there is an accepting single-char state at start
        # Handle case where start state directly accepts single chars (we set transitions from 0 to those states)
        if last_accept_state is None:
            raise ValueError(f"Lexical error at position {i}: unexpected character {input_text[i]!r}")
        lexeme = input_text[i:last_accept_pos]
        tok_type = accepting[last_accept_state]
        if tok_type != "WS":  # skip whitespace tokens
            tokens.append((tok_type, lexeme, i, last_accept_pos))
        i = last_accept_pos  # continue after the longest accepted lexeme
    return tokens

# Example usage:
examples = [
    "foo + 42 * (bar123)",
    "a1b2  007 +x", 
    "(  ) + *",
    "123abc",  # note: this will be lexed as NUMBER '123' then IDENT 'abc' because of maximal munch
]

lex("42 + 40");

for ex in examples:
    try:
        toks = lex(ex)
        print(f"Input: {ex!r}")
        for t in toks:
            print("  ", t)
        print()
    except ValueError as e:
        print("Lexing error in input:", ex, "->", e)
        print()
```

## References

- https://en.wikipedia.org/wiki/Lexical_analysis
- [Grammar](note.html?n=technica/computation/language-system/conceptual-model-language-system/grammar.md)
- https://www.reddit.com/r/ProgrammingLanguages/comments/10aalbq/are_there_better_more_efficient_ways_to_perform/
- https://crates.io/crates/logos