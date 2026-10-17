"""index.html(아티팩트 원본)을 GitHub Pages용 완성 문서 docs/index.html로 만든다."""
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "index.html").read_text(encoding="utf-8")

head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]

reset = (
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>"
)

doc = (
    "<!doctype html>\n<html lang=\"ko\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
    "<meta name=\"robots\" content=\"noindex,nofollow\">\n"
    f"{reset}\n{head}\n</head>\n<body>\n{body.strip()}\n</body>\n</html>\n"
)

out = ROOT / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(doc, encoding="utf-8")
(out / "CNAME").write_text("chungsim.lain.kr\n", encoding="utf-8")
(out / ".nojekyll").write_text("", encoding="utf-8")
print(f"docs/index.html {len(doc):,} bytes")
