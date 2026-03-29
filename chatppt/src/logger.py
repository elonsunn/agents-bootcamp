import logging
import sys
from pathlib import Path

LOG = logging.getLogger("chatppt")
if not LOG.handlers:
    LOG.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s:%(lineno)d - %(message)s")

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    LOG.addHandler(sh)

    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_dir / "app.log", encoding="utf-8")
    fh.setFormatter(fmt)
    LOG.addHandler(fh)
