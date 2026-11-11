# Module 04: Closures & Decorators 🎁

> *"A decorator is simply a callable that takes a function, extends its behavior, and returns a callable—without modifying the original function's source code."*

Decorators are one of Python's most powerful idioms for cross-cutting concerns (logging, authentication, caching, rate limiting, and instrumentation). To master decorators, you must understand Python's **execution model**:
1. **Functions are First-Class Objects**: They can be assigned to variables, passed as arguments to other functions, and returned from functions.
2. **Closures**: An inner function remembers and has access to variables in its enclosing scope, even after the outer function has finished executing!
3. **Decoration Time vs. Call Time**: Code at the top level of a decorator runs **at module import/definition time**, whereas code inside the inner wrapper runs **at call time**.

---

## 🧠 The Anatomy of a Decorator

```python
from functools import wraps

def my_decorator(func):
    # RUNS AT DECORATION TIME (when @my_decorator is evaluated)
    print("Decorating", func.__name__)

    @wraps(func) # Preserves __name__, __doc__, and signature
    def wrapper(*args, **kwargs):
        # RUNS AT CALL TIME (before original func)
        print("Before call")
        result = func(*args, **kwargs)
        # RUNS AT CALL TIME (after original func)
        print("After call")
        return result # CRITICAL: Must return the result!

    return wrapper
```

### The 4 Most Dangerous Beginner Traps:
1. **Forgetting to return `result`**: If the wrapper doesn't `return result`, calling the decorated function will silently return `None`!
2. **Missing `*args, **kwargs`**: The wrapper must accept `*args, **kwargs` and pass them into `func(*args, **kwargs)`, otherwise calling the function with arguments will crash with a `TypeError`.
3. **Confusing Decoration Time with Call Time**: Any logic placed outside `def wrapper` executes only once when the file is loaded, not every time the function is called.
4. **Losing Function Metadata**: Without `@wraps(func)` from `functools`, the decorated function's `__name__` becomes `"wrapper"` and its docstrings are erased.

---

## 🗺️ Module 04 Drill Directory (20 Progressive Drills)

### Level 1: Foundations & Closures (Drills 01 – 06)
* **01-function-as-data**: Functions as variables, arguments, and return values.
* **02-closure-state-accumulator**: Build a counter using closure state (`nonlocal`).
* **03-announce-execution-order**: Trace and predict exact decoration-time vs call-time print sequences (Quest 4).
* **04-return-value-forwarder**: Debug and repair decorators that swallow return values.
* **05-arguments-forwarder**: Forward positional and keyword arguments cleanly through wrappers.
* **06-metadata-preserver**: Use `@functools.wraps` to preserve `__name__`, `__doc__`, and signatures.

### Level 2: Practical Engineering Decorators (Drills 07 – 13)
* **07-call-counter-decorator**: Decorator that tracks and persists call count on a function attribute (Quest 4).
* **08-execution-timer**: Measure and print execution time in milliseconds.
* **09-memoization-cache**: Build `@memoize` decorator from scratch caching results in a closure dictionary.
* **10-input-type-enforcer**: Decorator that validates argument types against type annotations and raises `TypeError`.
* **11-retry-on-exception**: Parametric decorator `@retry(max_attempts=3, delay=0.1)` retrying on failure.
* **12-rate-limiter**: Restrict function execution to $N$ calls per second window.
* **13-deprecated-warning**: Decorator that emits a `DeprecationWarning` with replacement message on first call.

### Level 3: Advanced Metaprogramming & Architecture (Drills 14 – 20)
* **14-decorator-with-arguments**: Three-tier nesting for parametric decorators (`@repeat(num_times=3)`).
* **15-optional-arguments-decorator**: Decorator usable with or without parentheses (`@log` or `@log(prefix="DEBUG")`).
* **16-class-decorator**: Decorate an entire class to auto-instrument or register all its methods.
* **17-singleton-pattern-decorator**: Ensure only a single instance of a decorated class ever exists.
* **18-authorization-role-guard**: Simulate role-based access control (`@require_role("admin")`).
* **19-circuit-breaker**: Fault-tolerance circuit breaker decorator (states: Closed, Open, Half-Open).
* **20-plugin-registry-decorator**: Build a dynamic extensible plugin registration system using `@register`.
