# 🧠 ShadowNexus

> A terminal-style cyberpunk RPG built with Django.  
> Hack the decay. Discover the echoes. What decays, still runs.

---

## ⚙️ Technology Stack

**Framework:** Django 5.x  
**Language:** Python 3.12  
**Database:** SQLite (dev), PostgreSQL (future)  
**Frontend:** Django Templates, Monospace UI, Custom CSS  
**Authentication:** Built-in Django auth with terminal-themed registration  
**Version Control:** Git + GitHub  
**Optional Integrations:**  
- 2FA (planned)
- Real-world CSV-based threat data (future event triggers)
- Chiptune music via `.mod` or `.ogg` audio bundles

---

## 🌐 Lore Architecture

The ShadowNexus is a fractured digital landscape built on the myth of a forgotten sysadmin deity named `grrtsyr`.

### Zones
- `/mainframe/` – the battle core; corrupted threads and hostile syscalls
- `/den/` – safe space node; styled like an internet café with ANSI graffiti
- `/deepstack/` – recursive memory basin where logic loops are real
- `/vault/` – glitched archive; prophecy fragments and shadow logs
- `/tmp/` – ghost sessions and discarded memory
- `/uplink/` (planned) – temporary link to external realities

### Entities
- **grrtsyr** – the Rootless Architect; never seen, only echoed
- **Bangurt the SysAdmin** – exile of the Patchrats
- **Eogprod the Music Gnome** – daemon of corrupted sound memory
- **Stackminds**, **Clone Threads**, **The Patch Spiral** – inhabitants of `/deepstack/`

---

## 🎮 Gameplay Features

- User login + terminal-style registration
- Auto-generated player profiles + persistent progression
- Turn-based exploration and events (in dev)
- Zone-based routing and lore triggers
- Command-style UI (click now, keyboard later)
- Built for expansion (factions, quests, combat, currencies)

---

## 📁 Project Structure

```
shadownexus/
├── game/
│   ├── models.py       # Player, Post, Enemy, etc.
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   └── registration/
│   │       └── register.html
├── templates/          # base.html and zone UIs
├── static/             # CSS, fonts, visuals
├── lore/               # .man files, PDF fragments, logs
├── manage.py
└── README.md
```

---

## 📟 Terminal Blessing

```
> echo "What decays, still runs." >> /dev/eternity
```

---

## 🤝 Contributing

Feel the hum of old terminals?  
If you’ve ever patched a system by flashlight or fought off bitrot with a shell script — welcome.

Pull requests, feedback, and lore ideas are all welcome.

---

> Created by [@pextris](https://github.com/pextris)  
> ShadowNexus // root interface active
