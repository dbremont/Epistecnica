---
tags: [note, shell, command-line, unix, tool, search]
---

# rg

> `rg` (**ripgrep**) is a recursive, line-oriented search tool written in Rust and shipped as a single static binary: it walks a directory tree, searches the files it finds, and prints the matching lines with line numbers. It is the modern replacement for `grep -R`, and its reputation rests on two decisions — a regex engine with linear-time guarantees, and a default ignore policy that skips what a programmer almost never wants to search.

> The tool is a descendant of `grep`, `ack` and `ag` in purpose, but not in implementation: where `grep` is a POSIX utility and `ack`/`ag` are scripts, ripgrep is a compiled Rust program built around a regex library that was written for the same problem.

## In the toolchain

| | |
| --- | --- |
| **Abstract task** | Search content |
| **Relation** | `grep` |
| **Main advantage** | Much faster recursive search, gitignore-aware by default |

## Typical use

```sh
rg -n 'TODO' src/
```

## Why it is fast

> Four mechanisms explain the benchmarks, and none of them is "Rust is fast" in the abstract.

| Mechanism | What it does | Consequence |
| --- | --- | --- |
| **Finite-automaton regex engine** | The Rust `regex` crate compiles patterns to automata rather than backtracking | Guaranteed linear time in the input — no catastrophic backtracking, and worst-case behaviour is predictable |
| **Literal prefilter** | Extracts a required literal from the pattern and scans for it with SIMD (`memchr`) before running the full engine | Files that cannot match are rejected at memory bandwidth |
| **Parallel traversal** | Walks directories on a thread pool and searches files concurrently | Scales with cores for the common many-small-files case |
| **Ignore-aware walking** | Applies `.gitignore`, `.ignore` and `.rgignore` rules and skips hidden and binary files during the walk | Fewer files opened, and the right ones |

> The engine trade-off is deliberate: the automata approach cannot express backreferences or lookaround, so ripgrep offers **PCRE2** behind `-P` when those are needed, and accepts the weaker worst case in exchange. The default path stays linear.

> I/O is the other half. ripgrep uses memory maps where they help and incremental reads where they do not (`--no-mmap` forces the latter); the choice matters on network filesystems and on very large files, which is why it is a flag rather than a constant.

## The ignore policy

> `grep -R` searches what is on disk. `rg` searches what a repository *contains*, by default: it reads `.gitignore`, `.ignore` and `.rgignore`, honours a global git exclude, skips hidden files, and stops on binary content. That default is the largest single difference in practice — it is why a search in a project returns project files and not `node_modules`, `.git` and build output.

| Want | Flag |
| --- | --- |
| Search everything, including ignored and hidden | `-uu` (`-u` twice: `--no-ignore --hidden`) |
| Include ignored files but keep hidden skipped | `-u` (`--no-ignore`) |
| Search hidden files only | `--hidden` |
| Follow symlinks | `-L` (`--follow`) |
| Respect or ignore a specific glob | `-g '*.rs'`, `-g '!vendor/**'` |
| Search binary files | `--binary` / `-a` (treat as text) |

## The interface worth knowing

| Flag | Effect |
| --- | --- |
| `-n` / `--line-number` | Prepend line numbers (the default for terminal output) |
| `-i` / `-S` | Case-insensitive / smart case (insensitive only if the pattern has no uppercase) |
| `-t py` / `-T py` | Include or exclude a file type (`--type-list` shows the definitions) |
| `-g '*.md'` | Include only glob matches, with `!` to exclude |
| `-C 2` / `-A` / `-B` | Context lines around each match |
| `-l` / `--files-with-matches` | Print only the names of matching files |
| `-c` / `--count` | Count matching lines per file |
| `-r 'new'` | Replace matches in the output — useful for previewing a rewrite |
| `--json` | One JSON object per match, for tooling |
| `-P` / `--pcre2` | Use the PCRE2 engine for lookaround and backreferences |
| `-j 4` | Number of search threads |
| `-z` | Search compressed files (gzip, bzip2, xz, zstd, lz4) |
| `--stats` | Search statistics, including bytes and files searched |
| `-F` / `--fixed-strings` | Treat the pattern as a literal string |

> Configuration lives in a file named by `RIPGREP_CONFIG_PATH`, one flag per line: `--smart-case`, `--hidden`, `--glob '!vendor/**'` and the like, applied to every invocation. The usual shell setup is an alias that adds colour and a pager, kept out of the config so that scripts still get plain output.

## Comparison

| Tool | Implementation | Regex engine | Ignore handling | Parallel |
| --- | --- | --- | --- | --- |
| **`grep`** | C, POSIX/GNU | Backtracking (GNU) or DFA | None | No |
| **`ack`** | Perl | Perl regex | Built-in, file-type based | No |
| **`ag`** (the silver searcher) | C | PCRE | Built-in, gitignore | Yes |
| **`rg`** | Rust | Finite automata, PCRE2 optional | Built-in, gitignore + ignore files | Yes |

## References

- [rg](https://github.com/BurntSushi/ripgrep) — the project, with the user guide and the FAQ that argue the performance claims
- [ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) — the long-form explanation of the engine, the ignore rules and the flags
- [Rust regex crate](https://docs.rs/regex/latest/regex/) — the linear-time engine at the core
- [grep](/view.html?p=notes/technica/general/grep.md) — the traditional tool it replaces
- [fd](/view.html?p=notes/technica/general/fd.md) — the same author's replacement for `find`
