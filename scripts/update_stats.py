"""Generate a small, dependency-free SVG from public GitHub API fields."""

import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

USER = "Davitmatoss"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def get(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Davitmatoss-profile"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urlopen(Request(url, headers=headers), timeout=20) as response:
        return json.load(response)


profile = get(f"https://api.github.com/users/{USER}")
stars = 0
page = 1
while True:
    repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=owner")
    if not repos:
        break
    stars += sum(repo.get("stargazers_count", 0) for repo in repos if not repo.get("fork"))
    if len(repos) < 100:
        break
    page += 1

metrics = [
    ("REPOSITÓRIOS PÚBLICOS", profile.get("public_repos", 0)),
    ("ESTRELAS RECEBIDAS", stars),
    ("SEGUIDORES", profile.get("followers", 0)),
]
parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 230" role="img" '
    'aria-label="Estatísticas públicas atualizadas do GitHub de Davi">',
    '<rect width="960" height="230" rx="20" fill="#101a2e"/>',
    '<rect x="1" y="1" width="958" height="228" rx="19" fill="none" stroke="#284264"/>',
    '<circle cx="52" cy="49" r="6" fill="#FF7185"/>',
    '<text x="72" y="56" fill="#E5EEFF" font-family="Arial,sans-serif" font-size="23" font-weight="700">ATIVIDADE PÚBLICA</text>',
]
for index, (label, value) in enumerate(metrics):
    x = 50 + index * 305
    parts.extend(
        [
            f'<rect x="{x}" y="85" width="282" height="104" rx="13" fill="#172742" stroke="#2B4266"/>',
            f'<text x="{x+19}" y="136" fill="#79A8FF" font-family="Arial,sans-serif" font-size="37" font-weight="700">{int(value)}</text>',
            f'<text x="{x+19}" y="165" fill="#AAB9D3" font-family="Arial,sans-serif" font-size="14">{escape(label)}</text>',
        ]
    )
parts.append('<text x="50" y="216" fill="#8295B5" font-family="Arial,sans-serif" font-size="14">Dados públicos do GitHub · atualização diária</text></svg>')
Path("assets/github-stats.svg").write_text("".join(parts), encoding="utf-8")
