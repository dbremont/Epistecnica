# Handlebars JS


> **Handlebars.js** is a **logic-less templating engine** for JavaScript, designed to separate presentation logic from application logic. It is a superset of the **Mustache** templating language, providing additional capabilities such as custom helpers, block expressions, and partials.
> 

## 🔧 **Features**

### **Template Compilation**

Handlebars templates are compiled into optimized JavaScript functions. This enables efficient rendering by avoiding repeated parsing of the template string at runtime.

```jsx
const template = Handlebars.compile("Hello, {{name}}!");
const output = template({ name: "World" }); // => "Hello, World!"

```

- Compilation produces a **render function** with a predictable execution path.
- The compiler performs an **AST (Abstract Syntax Tree)** traversal of the template source, resolving literal text, expressions, blocks, and partials.

### **Expression Resolution**

Handlebars uses **contextual path resolution** to evaluate expressions. The `{{variable}}` syntax accesses properties of the current context object. Dot notation (`{{user.name}}`) and path traversal (`../parentProp`) are supported.

- It evaluates using a **lexical scope model**, descending into objects or block contexts.
- It doesn't support arbitrary JavaScript execution — only property lookups and predefined helpers.

### **Helpers**

Custom helpers allow injection of logic into templates without violating the logic-less paradigm.

- **Inline helpers**: `{{uppercase name}}`
- **Block helpers**:
    
    ```
    {{#if user.isAdmin}}
      <p>Welcome admin</p>
    {{/if}}
    
    ```
    

Helpers are functions registered globally with `Handlebars.registerHelper(name, fn)`.

### **Partials**

Partials are reusable template fragments.

```
{{> userInfo }}

```

- Loaded via `Handlebars.registerPartial(name, templateString)`
- Useful for component-like reuse and layout injection

### **Block Syntax**

Handlebars extends Mustache’s section tags by allowing:

- Custom block helpers with opening/closing tags (`{{#each items}} ... {{/each}}`)
- Inversion blocks using `{{else}}`

Block helpers receive the current context and optionally a block options hash.

### **Context and Scoping**

Templates execute within a data context, and blocks (e.g., `each`, `with`) modify the current scope. Handlebars manages context transitions internally via stack frames that preserve path resolution integrity.

### **Security & Escaping**

By default, Handlebars **HTML-escapes** interpolated output to prevent XSS:

- `{{name}}` → HTML-escaped
- `{{{name}}}` → unescaped

### **Extensibility**

Handlebars is designed to be extensible at compile-time and runtime:

- Custom AST transforms can be applied during compilation.
- Visitors can be injected into the parser or compiler pipeline for pre-processing templates.
- The runtime can be embedded into environments like browsers or Node.js.

### Internal Structure

- **Parser**: Converts template strings into an AST.
- **Compiler**: Transforms the AST into JavaScript source code.
- **Runtime**: Executes compiled templates with context and helpers.

## References

- [https://pugjs.org/api/getting-started.html](https://handlebarsjs.com/)
- https://github.com/handlebars-lang/handlebars.js