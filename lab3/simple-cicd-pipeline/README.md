# Lab 3 — Build and Optimize Your Application with GitHub Actions

This lab extends Lab 2 with application optimizations, advanced GitHub Actions workflows, caching, and error-handling patterns.

## Structure
- `src/app.js` — Optimized Express application
- `tests/app.test.js` — Jest + Supertest tests (includes performance endpoint)
- `.github/workflows/simple-ci.yml` — Baseline CI workflow (from Lab 2)
- `.github/workflows/optimized-ci.yml` — Optimized CI/CD workflow with caching + conditional deploy
- `.github/workflows/error-handling.yml` — Manual workflow demonstrating failure recovery patterns
- `performance-check.sh` — Local helper script to review project/perf characteristics
- `LAB3-GUIDE.md` — Lab 3 documentation

## Quick start
```bash
npm install
npm test
npm run build
npm start

```
