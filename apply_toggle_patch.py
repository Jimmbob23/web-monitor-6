from pathlib import Path

main = Path("app/main.py")
index = Path("app/templates/index.html")
site = Path("app/templates/site.html")

main_text = main.read_text(encoding="utf-8")

if '@app.post("/sites/{site_id}/toggle")' not in main_text:
    marker = '@app.post("/sites/{site_id}/check")'
    route = '''@app.post("/sites/{site_id}/toggle")
def toggle_site(site_id: int, request: Request, db: Session = Depends(get_db)):
    redirect = require_login(request, db)
    if redirect:
        return redirect

    site = db.get(Site, site_id)
    if site:
        site.enabled = not site.enabled
        site.last_status = "enabled" if site.enabled else "paused"
        db.commit()

    sync_jobs()
    referer = request.headers.get("referer") or "/"
    return RedirectResponse(referer, status_code=303)


'''
    main_text = main_text.replace(marker, route + marker)
    main.write_text(main_text, encoding="utf-8")
    print("main.py: toggle route inserted")
else:
    print("main.py: toggle route already exists")

index_text = index.read_text(encoding="utf-8")

if 'action="/sites/{{s.id}}/toggle"' not in index_text:
    old = '<form class="d-inline" method="post" action="/sites/{{s.id}}/check"><button class="btn btn-sm btn-outline-primary">Prüfen</button></form>'
    new = '''<form class="d-inline" method="post" action="/sites/{{s.id}}/check"><button class="btn btn-sm btn-outline-primary" {% if not s.enabled %}disabled title="Monitor ist pausiert"{% endif %}>Prüfen</button></form>
    <form class="d-inline" method="post" action="/sites/{{s.id}}/toggle">
      {% if s.enabled %}
      <button class="btn btn-sm btn-outline-warning">Pausieren</button>
      {% else %}
      <button class="btn btn-sm btn-outline-success">Aktivieren</button>
      {% endif %}
    </form>'''
    if old in index_text:
        index_text = index_text.replace(old, new)
    else:
        marker = '<form class="d-inline" method="post" action="/sites/{{s.id}}/delete"'
        insert = '''<form class="d-inline" method="post" action="/sites/{{s.id}}/toggle">
      {% if s.enabled %}
      <button class="btn btn-sm btn-outline-warning">Pausieren</button>
      {% else %}
      <button class="btn btn-sm btn-outline-success">Aktivieren</button>
      {% endif %}
    </form>
    '''
        index_text = index_text.replace(marker, insert + marker)

    index_text = index_text.replace(
        '<a href="/sites/{{s.id}}">{{s.name}}</a>',
        '<a href="/sites/{{s.id}}">{{s.name}}</a>{% if not s.enabled %} <span class="badge text-bg-secondary">pausiert</span>{% endif %}'
    )
    index.write_text(index_text, encoding="utf-8")
    print("index.html: toggle button inserted")
else:
    print("index.html: toggle button already exists")

site_text = site.read_text(encoding="utf-8")

if 'action="/sites/{{site.id}}/toggle"' not in site_text:
    marker = '<form method="post" action="/sites/{{site.id}}/check" class="d-inline">'
    insert = '''<form method="post" action="/sites/{{site.id}}/toggle" class="d-inline">
  {% if site.enabled %}
  <button class="btn btn-warning">Monitor pausieren</button>
  {% else %}
  <button class="btn btn-success">Monitor aktivieren</button>
  {% endif %}
</form>
'''
    site_text = site_text.replace(marker, insert + marker)
    site.write_text(site_text, encoding="utf-8")
    print("site.html: toggle button inserted")
else:
    print("site.html: toggle button already exists")
