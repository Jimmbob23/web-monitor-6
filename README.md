# Enterprise 6 Backup/Restore Patch

Diese ZIP ergänzt Backup und Restore für Web Monitor Enterprise 6.

Enthalten:

```text
app/main.py
app/services/backups.py
app/templates/backups.html
app/templates/base.html
```

Nach dem Kopieren:

```bash
git add app/main.py app/services/backups.py app/templates/backups.html app/templates/base.html
git commit -m "Add backup and restore"
git push
```

Dann GitHub Actions abwarten und Portainer aktualisieren.
