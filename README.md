<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=180&section=header&text=SQL%20Plan%20Viewer&fontSize=38&fontColor=ffffff&animation=fadeIn" width="100%" alt="SQL Plan Viewer banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2800&pause=900&color=2DD4BF&center=true&vCenter=true&width=760&lines=Inspect%20SQLite%20query%20plans%20as%20a%20readable%20tree." alt="Inspect SQLite query plans as a readable tree." />
<img src="assets/icon.svg" width="116" alt="SQL Plan Viewer icon" />

[![License](https://img.shields.io/github/license/CyberLoop-dev/sql-plan-viewer?style=for-the-badge)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/sql-plan-viewer?style=for-the-badge)](https://github.com/CyberLoop-dev/sql-plan-viewer)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/sql-plan-viewer?style=for-the-badge)](https://github.com/CyberLoop-dev/sql-plan-viewer/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/sql-plan-viewer?style=for-the-badge)](https://github.com/CyberLoop-dev/sql-plan-viewer/commits/main)

**Inspect SQLite query plans as a readable tree.**

</div>

## 🧭 Overview

SQL Plan Viewer is a small, local-first utility. Inspect SQLite query plans as a readable tree. It runs on your machine and does not require an account or hosted service.

## ✨ Features

- ✨ Explain SELECT and WITH queries against an existing SQLite database.
- ✨ Open database files in read-only mode.
- ✨ Render plan details with parent-child indentation.
- ✨ Use --json for scripts and tooling.
- ✨ Run a built-in indexed sample with no database setup.

## 🎬 Demo

Run the demo to see how SQLite uses an index. For your own database, provide its path followed by a SELECT query. The tool displays the planner output; it does not benchmark execution time.

## 🚀 Quick Start

```bash
python main.py --demo
```

## 🧰 Tech Stack

- 🟢 Python 3 standard library and sqlite3
- 🧱 Small, readable source files
- 🔒 Local processing with no telemetry

## 🗂️ Folder Structure

```text
sql-plan-viewer/
├── main.py
├── requirements.txt
├── assets/icon.svg
├── .gitignore
└── README.md
```

## 🗺️ Roadmap

- [ ] 🧪 Add focused automated tests
- [ ] 🧩 Add more examples based on feedback
- [ ] 📦 Publish a versioned release

## 🤝 Contributing

Issues and pull requests are welcome. Include a clear reproduction and keep changes focused.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Decorative wave footer" />
</div>
