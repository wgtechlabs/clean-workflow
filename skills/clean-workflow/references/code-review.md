# Code Review Handling

For every review comment that is addressed:

1. Inspect the current remote head and relevant files.
2. Make the smallest repository-supported change.
3. Run focused validation.
4. Reply to that specific review comment.
5. Resolve the thread only after the reply and change are verified.
6. Confirm the final remote state and that the addressed thread is resolved.

Do not duplicate a fix that is already present on the current remote head.
Do not resolve a comment before the requested change and reply are complete.
