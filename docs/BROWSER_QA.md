# Browser QA

J-stack requires a real browser for product QA and must never claim visual verification from source inspection alone.

Detection order: project-configured harness → gstack browser if installed → existing Playwright → another explicit real-browser tool.

For a new project, Playwright is the boring fallback. The QA skill should test the lake acceptance path, meaningful error/recovery states, responsive behavior where relevant, and capture evidence. QA is report-first; code fixes happen in a separate authorized BUILD invocation.
