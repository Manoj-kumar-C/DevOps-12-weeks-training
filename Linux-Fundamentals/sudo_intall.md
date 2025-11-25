| Flag                      | Meaning                 | When to use            |
| ------------------------- | ----------------------- | ---------------------- |
| `-y`                      | Auto yes                | Scripts                |
| `-f`                      | Fix broken deps         | After failed install   |
| `--fix-missing`           | Retry missing downloads | Weak network           |
| `--no-install-recommends` | Lightweight install     | Docker/Minimal OS      |
| `-q`, `-qq`               | Quiet output            | CI/CD                  |
| `--download-only`         | Download only           | Offline use            |
| `--reinstall`             | Reinstall package       | Fix corrupted installs |
| `--purge`                 | Remove + config         | Clean uninstall        |
| `-s`                      | Simulation              | Safe testing           |
