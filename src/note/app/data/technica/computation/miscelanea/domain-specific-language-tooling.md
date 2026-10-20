# Domain Specific Language Tooling


> 

- Grammar: …
- Parsing: [https://tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)
- LSP
- Neovim Support

```jsx
.prs file
   ↓
Tree-sitter Grammar
   ↓
Generated Parser (C)
   ↓
Neovim Treesitter Runtime
   ↓
Syntax Tree / Queries
   ↓
Highlighting / Folding / Textobjects / Navigation
```

```bash
Create a full language tooling stack for the Personal Recording System Language (PRSL) inside Neovim, generated and derived from the formal grammar.

The target is not merely syntax highlighting.

The target is a complete language environment:

Tree-sitter parser
Syntax highlighting
Structural editing
Incremental parsing
Folding
Textobjects
Indentation engine
Semantic queries
LSP support
Formatter
Diagnostics
Snippets
Completion
Refactoring
Record navigation
Relation graph navigation
Metadata introspection
Schema-aware validation
Query language support
Temporal visualization support
Operational workflow support
```

Logs:

- The `highlights.scm` file - tree-sitter rust does not generates.
- tree-sitter highlight sample.prs --html > a.html
- Tree-sitter CLI versions are loosely coupled.
- `:lua print(vim.inspect(vim.treesitter.language_version))`
- what does '/home/dbremont/Code/prs/prs.so' enables?
- `prs.so` is the compiled Tree-sitter parser that transforms PRS source text into a structured syntax tree that Neovim and query engines can operate on.
- What is a query engine? What is a ‘query’?