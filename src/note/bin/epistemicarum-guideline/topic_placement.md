# Topic placement strategy

> Reusable decision procedure for placing any new topic in the right space(s), with the
> right artifacts. First worked instance: Quarry → nature (node `quarry-ontic-001`,
> note `nature/quarry.md`). Follow it before creating nodes or notes.

1. **Cut the segment, name the question.** State what is included/excluded, then match the
   dominant question to a space — that fixes the meta workflow, the note schema, and the
   owning dataset:

   | Dominant question | Space | Meta workflow | Dataset / editor |
   | --- | --- | --- | --- |
   | What observer-independent furniture is here? | nature | "How to decompose any natural instance?" | `nature` (`/nature/edit.html`) |
   | How is transformation organized and performed? | technique | "How to decompose any technical instance?" | `technique` (`/technique/edit.html`) |
   | Which actors, institutions, roles, relations act here? | social | "How to decompose any social instance?" | `social` (`/social/edit.html`) |
   | What scaffolding warrants knowing it? | epistemica | "How to decompose any epistemic instance?" | `epistemica` (`/epistemica/edit.html`) |

2. **Type the root; ambiguity goes to the human, never guess.** When the instance is readable under
   several grammars (a quarry is a landform *and* a worksite *and* a facility), STOP and ask
   the human which readings to grow trees for (and which is primary) before decomposing.
    One tree per confirmed type (multi-root forest — never two types on one row). When
    the confirmed readings span *spaces*, document them in one multi-root note with
    a declared primary (see the ambiguity reading). Only when
    no answer comes, declare one default root and keep the others as `readable as …` prose
    cross-links.
3. **Fix the depth before decomposing; default to the middle path.** Every decomposition
   request states its level of detail — shallow (root plus direct constituents, no
   intermediaries), middle (full intermediate structure: grouping nodes throughout,
   every branch worked to instance leaves, exemplars only where a branch needs one),
   or deep (exhaustive attributes, fields, schedules, and deployment exemplars).
   When no depth is stated, assume the middle path: satisfy the Well-Expansion Rule
   (rich intermediates, all leaves resolving to instances) without enumerating
   deployment minutiae. E.g. pharmaceutical industry — shallow: sectors and major
   product groups; middle: plus production systems, key artifacts, standards, and
   institutions; deep: plus facility operations, batch records, and validation protocols.
4. **Single home.** Every node lives in exactly one owning dataset; other spaces compute
   views over it, never duplicate it (see "Derived views" above).
5. **Node, note, or both.** A note carries decomposition and argument (corpus home
   `app/note/data/`, kebab-case paths, new top-level sections allowed — e.g. `nature/`);
   a node carries graph addressability (edges, tags, search). First-class topics usually
   need both; note-first is fine. New nodes ship their local mirror plus seed/bootstrap
   coverage in the same change set (`data.json` is what `bin/seed_couchdb.py` and server
   startup read).
6. **Derived-view check.** If the topic plays a production role, tag the owning Social
   node `<space>-view` at creation time and regenerate (`make <space>-view`). Nature and
   technique nodes never carry view tags.
7. **Verify.** Rebuild the notes index (`python bin/build_note_index.py`, commit the
   result); pull the server mirror before committing dataset edits; smoke-test every
   touched route (`/, /<module>/, /<module>/edit.html`, note viewer path). One module
   (or one concern) per change set.
