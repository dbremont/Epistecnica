#!/usr/bin/env python3
"""Validate the approximation playground bank.

The problems are generated in the browser from the scheme specs in
src/corpus/notes/epistemica/playground/approximation-problems.json;
this checker guards the data so a broken scheme is caught in `make check`
rather than in the page.

Checks:

- the file parses and carries version, title, intro, toleranceKinds, topics;
- every topic has id, name, icon, color, blurb and at least one scheme;
  topic ids are unique and kebab-case;
- every scheme has id, kind, prompt, tolerance and steps; scheme ids are
  unique within their topic;
- `kind` names a generator the page implements (the list below is kept in
  sync by hand — it is the contract between the JSON and the page);
- a `const-table` scheme names a table that exists;
- a `choice` question carries at least two choices and a correctChoice
  index in range;
- the tolerance kind is declared in toleranceKinds, and `rel`/`factor`/`abs`
  carry their value where required;
- prompts and steps only use placeholders that are known for the generator.

Usage: python3 bin/approximation_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STORE = (REPO / 'src' / 'corpus' / 'notes' / 'epistemica'
         / 'playground' / 'approximation-problems.json')

KINDS = {
    'const-table', 'doubling', 'divide', 'percent-of', 'ratio-simple', 'remainder',
    'power', 'sqrt', 'cbrt', 'rule72', 'exact-double', 'log-return', 'pct-points',
    'decades', 'trig-exact', 'trig-decimal', 'deg-to-rad', 'small-angle',
    'exp-value', 'half-life', 'half-life-count', 'half-life-time', 'growth-factor',
    'circle', 'triangle-area', 'sphere', 'hypotenuse', 'c-to-f', 'km-to-mi',
    'kwh-to-j', 'ms-to-s', 'mean-list', 'mean-outlier', 'mean-vs-median',
    'median-list', 'median-robust', 'mode-list', 'two-period', 'cagr',
    'future-value', 'loss-recovery', 'continuous', 'bacteria', 'up-down',
    'geometric', 'vol-drag', 'vol-drag-gap', 'portfolio', 'corr-angle',
    'zero-variance', 'drawdown', 'pe', 'earnings-yield', 'sharpe',
    'concentration', 'unit-price', 'dice', 'bet', 'fair-price', 'present-value',
    'perpetuity', 'time-to-value', 'std-list', 'std-from-var', 'annualise',
    'daily', 'bayes', 'bayes-generic', 'bayes-neglect', 'ph-from', 'ph-dilute',
    'decibels',
}

# placeholders each generator substitutes into the prompt / steps
PLACEHOLDERS = {
    'const-table': {'q', 'vE', 'v', 'exp', 'lo', 'hi'},
    'doubling': {'a', 'b', 'ratio', 'n'},
    'divide': {'a', 'b', 'ans', 'aE', 'bE', 'ansE'},
    'percent-of': {'p', 'a', 'ans'},
    'ratio-simple': {'a', 'b', 'ans'},
    'remainder': {'a', 'b', 'q', 'bq', 'r'},
    'power': {'x', 'n', 'ans', 'exp'},
    'sqrt': {'x', 'ans', 'lo', 'hi', 'lo2', 'hi2'},
    'cbrt': {'x', 'ans', 'lo', 'hi', 'lo3', 'hi3', 'exp'},
    'rule72': {'r', 'approx', 'exact'},
    'exact-double': {'r', 'denom', 'ans'},
    'log-return': {'p0', 'p1', 'ratio', 'ans', 'pct'},
    'pct-points': {'a', 'b', 'ans', 'rel'},
    'decades': {'F', 'ans'},
    'trig-exact': {'fn', 'deg', 'exact', 'ans'},
    'trig-decimal': {'fn', 'deg', 'rad', 'ans'},
    'deg-to-rad': {'deg', 'ans', 'pi', 'pi180'},
    'small-angle': {'mrad', 'rad', 'exact'},
    'exp-value': {'x', 'ans'},
    'half-life': {'n', 'ans', 'pct'},
    'half-life-count': {'t', 'hl', 'ans'},
    'half-life-time': {'hl', 'denom', 'k', 'ans'},
    'growth-factor': {'p', 'n', 'base', 'ans'},
    'circle': {'r', 'r2', 'ans'},
    'triangle-area': {'b', 'h', 'ans'},
    'sphere': {'r', 'r3', 'ans'},
    'hypotenuse': {'a', 'b', 'a2', 'b2', 'sum', 'ans'},
    'c-to-f': {'c', 'ans'},
    'km-to-mi': {'km', 'ans'},
    'kwh-to-j': {'kwh', 'ansSci'},
    'ms-to-s': {'ms', 'ans'},
    'mean-list': {'list', 'sum', 'n', 'ans'},
    'mean-outlier': {'n', 'old', 'add', 'oldSum', 'newSum', 'n1', 'ans'},
    'mean-vs-median': {'list', 'sorted', 'mean', 'median', 'verdict'},
    'median-list': {'list', 'sorted', 'n', 'ans'},
    'median-robust': {'list', 'sorted', 'old', 'add', 'n1', 'ans'},
    'mode-list': {'list', 'counts', 'modes', 'ans'},
    'two-period': {'r1', 'r2', 'f1', 'f2', 'ans', 'sum'},
    'cagr': {'start', 'end', 'n', 'ans'},
    'future-value': {'pv', 'r', 't', 'ans'},
    'loss-recovery': {'L', 'factor', 'inv', 'ans'},
    'continuous': {'pv', 'r', 't', 'rt', 'ans'},
    'bacteria': {'d', 'n0', 't', 'k', 'ans'},
    'up-down': {'r1', 'r2', 'f1', 'f2', 'ans'},
    'geometric': {'r1', 'r2', 'r3', 'ans', 'arith'},
    'vol-drag': {'mu', 'sigma', 'drag', 'ans'},
    'vol-drag-gap': {'mu', 'sigma', 'ans'},
    'portfolio': {'w1', 'w2', 's1', 's2', 'rho', 'a', 'b', 'c', 'var', 'ans'},
    'corr-angle': {'rho', 'ans', 'verdict'},
    'zero-variance': {'s1', 's2', 'ans'},
    'drawdown': {'peak', 'trough', 'ans'},
    'pe': {'price', 'eps', 'ans'},
    'earnings-yield': {'price', 'eps', 'ans'},
    'sharpe': {'mu', 'rf', 'sigma', 'ans'},
    'concentration': {'mass', 'vol', 'ans', 'ppm'},
    'unit-price': {'price', 'qty', 'ans'},
    'dice': {'faces', 'sum', 'ans'},
    'bet': {'pw', 'win', 'lose', 'up', 'down', 'ans'},
    'fair-price': {'p', 'win', 'ans'},
    'present-value': {'fv', 'r', 't', 'ans'},
    'perpetuity': {'c', 'r', 'rFrac', 'ans'},
    'time-to-value': {'pv', 'r', 'fv', 'lnRatio', 'lnRate', 'ans'},
    'std-list': {'list', 'mean', 'sq', 'var', 'ans'},
    'std-from-var': {'v', 'ans'},
    'annualise': {'m', 'sqrt12', 'ans'},
    'daily': {'a', 'sqrt252', 'ans'},
    'bayes': {'prev', 'sens', 'spec', 'esc', 'pPos', 'pFlag', 'ans'},
    'bayes-generic': {'pa', 'pbA', 'pbNotA', 'paNot', 'pB', 'ans'},
    'bayes-neglect': {'pa', 'pbA', 'pbNotA', 'paNot', 'pB', 'ans'},
    'ph-from': {'h', 'e', 'ans'},
    'ph-dilute': {'ph', 'k', 'delta', 'ans'},
    'decibels': {'F', 'ans'},
}

# tables the page implements
TABLES = {'magnitudes', 'money-scale'}

ID_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
PH_RE = re.compile(r'\{([a-zA-Z0-9_]+)\}')

errors = []


def err(msg):
    errors.append(msg)


def check_tolerance(here, tol, kinds):
    if not isinstance(tol, dict):
        err(f'{here}: tolerance is not an object')
        return
    kind = tol.get('kind')
    if kind not in kinds:
        err(f'{here}: tolerance kind {kind!r} is not declared in toleranceKinds')
        return
    if kind in ('rel', 'factor') and not isinstance(tol.get('value', tol.get('pct')), (int, float)):
        err(f'{here}: tolerance {kind} needs a numeric value')
    if kind == 'abs' and not isinstance(tol.get('value'), (int, float)):
        err(f'{here}: tolerance abs needs a numeric value')


def check_placeholders(here, text, kind):
    allowed = PLACEHOLDERS.get(kind, set())
    for m in PH_RE.finditer(text):
        name = m.group(1)
        if name not in allowed:
            err(f'{here}: placeholder {{{name}}} is not supplied by kind {kind!r}')


def main():
    if not STORE.is_file():
        print(f'[approximation] FAIL: {STORE.relative_to(REPO)} missing', file=sys.stderr)
        return 1
    try:
        data = json.loads(STORE.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        print(f'[approximation] FAIL: invalid JSON ({exc})', file=sys.stderr)
        return 1

    for k in ('version', 'title', 'intro', 'toleranceKinds', 'topics'):
        if k not in data:
            err(f'header missing {k!r}')
    kinds = set((data.get('toleranceKinds') or {}).keys())
    topics = data.get('topics') or []
    if not topics:
        err('no topics')

    seen_topics = set()
    n_schemes = 0
    for t in topics:
        tid = t.get('id')
        here = f'topic {tid!r}'
        if not isinstance(tid, str) or not ID_RE.match(tid or ''):
            err(f'{here}: id is not kebab-case')
        if tid in seen_topics:
            err(f'{here}: duplicate topic id')
        seen_topics.add(tid)
        for k in ('name', 'icon', 'color', 'blurb', 'schemes'):
            if k not in t:
                err(f'{here}: missing {k!r}')
        schemes = t.get('schemes') or []
        if not schemes:
            err(f'{here}: no schemes')
        seen_schemes = set()
        for s in schemes:
            sid = s.get('id')
            sh = f'{tid}/{sid}'
            if not isinstance(sid, str) or not ID_RE.match(sid or ''):
                err(f'{sh}: scheme id is not kebab-case')
            if sid in seen_schemes:
                err(f'{sh}: duplicate scheme id')
            seen_schemes.add(sid)
            kind = s.get('kind')
            if kind not in KINDS:
                err(f'{sh}: unknown generator kind {kind!r}')
                continue
            for k in ('prompt', 'tolerance', 'steps'):
                if k not in s:
                    err(f'{sh}: missing {k!r}')
            if kind == 'const-table' and s.get('table') not in TABLES:
                err(f'{sh}: table {s.get("table")!r} is not implemented by the page')
            if kind == 'choice' or 'choices' in s:
                ch = s.get('choices') or []
                if len(ch) < 2:
                    err(f'{sh}: a choice question needs at least two choices')
                cc = s.get('correctChoice')
                if not isinstance(cc, int) or cc < 0 or cc >= len(ch):
                    err(f'{sh}: correctChoice {cc!r} is out of range')
            check_tolerance(sh, s.get('tolerance') or {}, kinds)
            check_placeholders(sh + ' prompt', s.get('prompt') or '', kind)
            for i, step in enumerate(s.get('steps') or []):
                check_placeholders(f'{sh} step {i + 1}', step, kind)
            n_schemes += 1

    if errors:
        print(f'[approximation] FAIL: {len(errors)} error(s)', file=sys.stderr)
        for e in errors:
            print('  -', e, file=sys.stderr)
        return 1

    print(f'[approximation] ok: {len(topics)} topics, {n_schemes} schemes, '
          f'{len(KINDS)} generator kinds -> {STORE.relative_to(REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
