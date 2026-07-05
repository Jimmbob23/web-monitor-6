# Enterprise 6 Toggle/Pause Patch

Dieser Patch bringt die Funktion zurück, einzelne Monitore zu pausieren oder wieder zu aktivieren.

## Anwendung

1. ZIP entpacken.
2. `apply_toggle_patch.py` in das Hauptverzeichnis deines Enterprise-6-Projekts kopieren.
3. Im Projektordner ausführen:

```bash
python apply_toggle_patch.py
```

4. Änderungen committen und pushen:

```bash
git add app/main.py app/templates/index.html app/templates/site.html
git commit -m "Add monitor pause toggle"
git push
```

5. GitHub Actions abwarten.
6. In Portainer das neue Image aktualisieren.
