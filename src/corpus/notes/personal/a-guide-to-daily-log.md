---
tags: [note, guia]
---

# A Guide to Daily Log

**Contains:** [A Guide to The Learning Log](/view.html?p=notes/personal/a-guide-to-the-learning-log.md)

> Uses Cases + Implementation Abstractions.
> 

> An only append register of all the inflow of tasks, things to remember, etc.
> 

> Serialize {Mind, Reality} into an Append-Only Log.
> 

> Personal Diary.
> 

> Designing a Personal Log System
> 

QA:

- How to create annotation for the records?
- Which the taxonomy of the elements being log?
- How to represent structure data in logs? How to track schemas evolution?
- **What are the best practices for encoding or encrypting security-sensitive or personal information in log files?**

## Index

## Annotations:

> Multi-level annotations.
> 

> Tags about reality logging, and brain.
> 
- **Data Tags** *(Categorizing and specifying types of data collected) (reality logging)*
    - `#data` – General tag for all data entries
    - `#data/<topic>/temporal` – Data related to time aspects (e.g., timestamps, durations)
    - `#data/<topic>/quantitative` – Numerical data or measurable metrics
    - `#data/<topic>/qualitative` – Descriptive data or subjective observations
    - `#data/<topic>/categorical` – Data that falls into specific categories or groups
- **Event Tags** *(Types of events or experiences)*
    - `#event/meeting` – Work or social meetings
    - `#event/celebration` – Birthdays, holidays, or special occasions
    - `#event/challenge` – Difficult situations or obstacles encountered
- **Action Tags** *(Indicating actions taken or needed)*
    - `#action/to-do` – Tasks or thoughts that require action
    - `#action/review` – Thoughts to revisit later
- **Cognitive Tags** *(Representing mental processes and thoughts)*
    - `#insight` – New realizations or understandings
    - `#reflection` – Thoughts on past experiences
    - `#idea` – Creative thoughts or concepts
- **Priority & Impact Tags** *(How significant it is)*
    - `#priority/high` – Urgency or importance
    - `#impact/life-changing` – Long-term relevance
- Content-Based Tags (What the record is about)
    - `#thought/philosophy` – Abstract ideas, theories, or reflections
    - `#event/meeting` – Concrete happenings
    - `#task/work` – Actionable responsibilities
    - `#task/work/start` – Actionable responsibilities
    - `#task/work/continue` – Actionable responsibilities
    - `#task/work/aborted` – Actionable responsibilities
    - `#task/work/done` – Actionable responsibilities
- **Emotional & Psychological Tags** *(How it felt or affected you)*
    - `#mood/energetic` – Emotional state
    - `#stress/low` – Cognitive load
- **Relationship & Reference Tags** *(Links to other records or sources)*
    - `#related/entry-20250225` – Internal reference to another log
    - `#source/book-title` – External references

Future Work:

- `@stadistic` Log Network Used.
- `@stadistic` Log
- Create  a Language Server.

## Identification

> For multi-step or complex tasks that generate subsequent actions, use **UUIDs** (Universally Unique Identifiers) or **GUIDs** (Globally Unique Identifiers) to uniquely track and manage each step.
> 

## Representing Sequence-Tree Task Process

> How to model working on a problem?
> 

> How to model the paths? How to model the backtracks in a text document? Take an easy approach;  every significant backtrack yield a new path. Every path is a document sub-section.
> 

> Look I Can Used  **`GUIDs`** for this  to.
> 

```

## Path 1: Approach A
- Step 1: Analyze problem.
- Step 2: Implement solution X.
- Outcome: Failed.
- Backtrack: Revert to Step 1.

## Path 1.1: Revised Approach A
- Step 1: Analyze problem.
- Step 2: Implement solution X with modification.
- Outcome: Success.

References
- https://en.wikipedia.org/wiki/Search_problem
- https://en.wikipedia.org/wiki/Backtracking
- https://en.wikipedia.org/wiki/Tree_(abstract_data_type)
```

Prototype:

```
action(task id) end.
follow(task id)/(new path)
...
follow(task id)/(path id) : ...
follow(task id)/(path id) : ...
task(ids): ...
```

## References

- https://es.wikipedia.org/wiki/Diario_de_navegaci%C3%B3n
- https://es.wikipedia.org/wiki/Bit%C3%A1cora
- https://github.com/dbremont/Autoregia/tree/main/daily
- https://www.reddit.com/r/startrek/comments/wkib9x/what_is_the_purpose_of_everyone_keeping_personal/
- https://news.ycombinator.com/item?id=21906650
