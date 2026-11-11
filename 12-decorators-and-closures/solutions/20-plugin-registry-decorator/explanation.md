# Deep-Dive Explanation: 20-plugin-registry-decorator

## 💡 Algorithmic & Architectural Thinking

The decorator-based registry is the foundational design pattern powering frameworks like Flask (`@app.route`), FastAPI, Pytest (`@pytest.fixture`), and Click (`@cli.command`):
- Instead of maintaining central registration lists, functions register themselves declaratively at point of definition.
- `register` returns the original function unaltered, allowing normal testing and reuse while populating internal dispatch tables.

---

## 📊 Complexity Analysis

- **Registration Time**: $O(1)$ dictionary insertion.
- **Lookup Time**: $O(1)$ dictionary retrieval.
- **Space Complexity**: $O(P)$ where $P$ is total registered plugins.
