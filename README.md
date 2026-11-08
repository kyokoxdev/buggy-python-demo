# buggy-python-demo

A tiny "shop" package with **intentionally planted defects**, used to demo
[llm-static-repair](https://github.com/kyokoxdev/llm-static-repair) (LLM + static analysis automated repair).

**Do not use this code for anything real.**

| File | Planted issues |
|---|---|
| `shop/db.py` | SQL injection via f-string and string concatenation (CWE-89); one constant-table query that tools flag but is a *false positive* |
| `shop/tools.py` | command injection with `shell=True` (CWE-78), `eval` on input (CWE-95), unclosed file; a fixed-argv `subprocess.run` that is a *false positive* |
| `shop/security.py` | hardcoded secret (CWE-798), MD5 password hashing (CWE-327), `random` for reset tokens (CWE-330), `pickle.loads` on untrusted data (CWE-502), `assert` used for authorization; a form-field name constant that is a *false positive* |
| `shop/cart.py` | logic bugs: mutable default argument, off-by-one loop and pagination, wrong discount math, division by zero, bare `except`, `== None` |

```bash
pip install -r requirements.txt
pytest -q      # 8 tests fail on purpose
```
