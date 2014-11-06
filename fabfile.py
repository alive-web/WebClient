from fabric.api import put, run
from fabvenv import Venv

ROOT = "/opt/lv128/WebClient/"

def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("server.py", ROOT)
    put("style.css", ROOT)
    put("web_cl.service", ROOT)
    put("index.html", ROOT)
    put("script.js", ROOT)
    run("sudo mv %s/web_cl.service /etc/systemd/system/" % ROOT)
    run("sudo systemctl enable web_cl")
    run("sudo systemctl restart web_cl")