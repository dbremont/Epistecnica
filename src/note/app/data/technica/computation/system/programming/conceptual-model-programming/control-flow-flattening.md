---
tags: [technique]
---

# Control Flow Flattening


> Suppose our **description of the computation** has a deeply nested branching structure—how can we make it more readable that is flat?
> 

> **To which class of techniques** does this belongs to? Control-Flow Reification, Control Techniques.
> 

> **Note:** The flattening is applied to the description of the computation - not the computation itself.
> 

## Case

> **Note:** In this simple case, we will de-nest the description structure. The real benefits become apparent when dealing with deeply nested blocks containing multiple lines of code.
> 

```bash
if cond1(x):
    if cond2(x):
       do_a(x)
    else:
       if cond3(x):
           do_b(x)
       else:
           do_c(x)
else:
    do_d(x)
```

## Transformation

> Note: This is an abstract idea the Control Variable - here one **possible implementation** Tactic (Mechanism) (or if you like low level technique).
> 

```bash
action = None

if cond1(x) and cond2(x):
    action = 'do_a'
elif cond1(x) and cond3(x):
    action = 'do_b'
elif cond1(x):
    action = 'do_c'
else:
    action = 'do_d'

# Execute the selected action
if action == 'do_a':
    do_a(x)
elif action == 'do_b':
    do_b(x)
elif action == 'do_c':
    do_c(x)
elif action == 'do_d':
    do_d(x)
```

## Relation

| Idea | Relation |
| --- | --- |
| **Next Action / Control Variable** | Directly flattens deeply nested conditional logic by representing the next computation as a variable rather than nested `if`s. |
| **Finite-State Machine (FSM) Encoding** | Treats each conditional path as a “state” and transitions via the control variable. Closely related to state-driven design patterns. |
| **Guard Clauses / Early Return** | Instead of deep nesting, check for exit conditions early and return or break. Simplifies readability without extra control variables. |
| **Lookup Table / Dispatch Dictionary** | Maps condition combinations to actions, allowing direct execution without long chains of `if/elif`. Especially useful for predictable condition-action patterns. |
| **Continuation-Passing Style (CPS)** | Encodes “what to do next” explicitly as a continuation function—related to control-flow reification. |
| **Command Pattern / Encapsulated Actions** | Each possible action is represented as an object or callable, decoupling selection from execution. |
| **Decision Table / Rule Engine** | Represents nested logic as a structured table (conditions × actions), making complex branching easier to maintain. |
| **Switch/Case Emulation** | In languages without `switch`, a flattened structure via mapping or dispatch emulates it. |
| **State Machine Libraries / Generators** | Automates control-variable updates and transitions. Useful in UI, workflows, or asynchronous logic. |

## References

- https://en.wikipedia.org/wiki/Finite-state_machine
- https://zerotistic.blog/posts/cff-remover/