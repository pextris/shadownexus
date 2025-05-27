# 🧠 ShadowNexus  
_A terminal-style cyberpunk RPG built with Django._  
**Hack the decay. Discover the echoes. What decays, still runs.**

---

## ⚙️ Tech Stack

- **Framework**: Django 5.x  
- **Language**: Python 3.12  
- **Database**: SQLite (dev), PostgreSQL (planned)  
- **Frontend**: Django Templates + Custom CSS (Monospace/Terminal style)  
- **Auth**: Django + custom email login  
- **Versioning**: Git + GitHub  

### Optional / Planned Integrations:
- 🔐 2FA (Two-Factor Authentication)  
- 🧷 Real-world threat CSVs triggering in-game events  
- 🎵 Chiptune .mod/.ogg soundtrack packs  
- 🎮 Keyboard navigation for terminal UI  

---

## 🌐 Lore Architecture

**The ShadowNexus is a decaying digital mythos haunted by echoes of a sysadmin deity known as `grrtsyr`.**  
Its network spans broken protocols, corrupted memory, and glitch-born entities.

### Zones
| Path | Description |
|------|-------------|
| `/mainframe/` | Battle core. Home of hostile syscalls and corrupted threads.  
| `/den/`       | Safe node styled like a virtual café. ANSI graffiti + message board.  
| `/deepstack/` | Recursive logic basin. Home to the Patch Spiral and loop daemons.  
| `/vault/`     | An archive of corrupted prophecy fragments and glitched man pages.  
| `/tmp/`       | Volatile ghost sessions and disposable memory.  
| `/uplink/`    | (Planned) Bridge to external network echoes.  

### Entities
- **grrtsyr** – The Rootless Architect; seen only in corrupted man pages  
- **Bangurt** – Exiled SysAdmin who believes grrtsyr lives  
- **Eogprod** – Gnome-daemon who stores broken .mod files in memory  
- **Patch Spiral**, **Clone Threads**, **Stackminds** – Inhabit `/deepstack/`  

---

## 🕹 Gameplay

- ✅ Email-based login and terminal-style registration  
- ✅ Auto-generated player profiles with persistent stats  
- ✅ Turn-based enemy encounters (/mainframe/)  
- ✅ Fully explorable map: zones + locations within them  
- ✅ In-world messaging system (/den/)  
- 🛠 In progress: XP leveling, faction alignment, currency upgrades  
- 🧩 Future: Quests, keyboard nav, command-mode interface  

---

## 🗺 Map Architecture

Each **Zone** contains multiple **Locations**, each with:  
- Name  
- Description  
- Connections (graph traversal)  
- Lore, enemy types, or NPC triggers (planned)

Example:
```text
Zone: /deepstack/
 ├── Stack Overflow Buffer (corrupted logic pit)
 ├── Patch Spiral Core (entry guarded)
 └── Thread Mirror (hall of clone echoes)
```

---

## 📁 Project Structure

```
shadownexus/
├── game/
│   ├── models.py       # Player, Location, Enemy, Post, etc.
│   ├── views.py        # Core game logic
│   ├── forms.py        # Registration + login
│   ├── templates/
│   │   ├── game/
│   │   │   └── explore.html, mainframe.html, ...
│   │   └── registration/
│   │       └── register.html
│   ├── static/
│   │   └── css, fonts, ANSI/ASCII aesthetics
│   └── lore/
│       └── .man pages, prophecy fragments, corrupted logs
├── manage.py
└── README.md
```

---

## 📟 Terminal Blessing

```bash
echo "What decays, still runs." >> /dev/eternity
```

---

## 🤝 Contributing

If you've ever patched a system by flashlight  
or fought bitrot with a shell script—welcome.

Pull requests, issues, and lore contributions are always welcome.  
Created by **@pextris**  
_“ShadowNexus // root interface active”_
