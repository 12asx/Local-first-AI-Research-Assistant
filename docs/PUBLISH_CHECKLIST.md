# Public-repository checklist

- [ ] Create a separate copy of the working project. NEVER publish the only copy.
- [ ] Confirm permission to distribute code, assets, icons and test data.
- [ ] Audit third-party licenses and agree on one project license. PyMuPDF uses AGPL/commercial licensing.
- [ ] Delete private PDFs, CAJ, DOCX, OCR images and screenshots.
- [ ] Delete `data/`, including memory, conversations, citation indexes, keys and caches.
- [ ] Delete `.env`, machine-specific settings, token caches and logs.
- [ ] Replace all hard-coded Windows paths and account names with examples/placeholders.
- [ ] Review `git status` / `git ls-files` / `git diff --cached` before first push.
- [ ] Run `python tools/prepublish_check.py` and manually review its warnings.
- [ ] Install dependencies and run tests from a *clean checkout* using a dummy API key or none.
- [ ] Document local-only hosting and cloud data disclosure behavior.
- [ ] Create a GitHub repository and publish from the clean copy.
- [ ] Check the GitHub repository file list as an anonymous visitor.
- [ ] Only then create a version tag and release ZIP/source archive.
