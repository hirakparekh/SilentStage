<div align="center">

# 🎵 Silent Stage

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=22D3EE&center=true&vCenter=true&width=680&lines=Making+live+music+accessible+to+the+deaf+and+hard-of-hearing.;Real-time+AI+sign-language+avatars+for+concerts.;Audio+%E2%86%92+text+%E2%86%92+sign-friendly+%E2%86%92+animated+avatar." alt="Typing SVG" />

<p>
  <img src="https://img.shields.io/badge/Next.js-000000?logo=next.js&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-3DA639?logo=opensourceinitiative&logoColor=white" />
  <img src="https://img.shields.io/badge/status-proof--of--concept-orange" />
</p>

<em>An AI-generated sign-language avatar system that bridges the accessibility gap at live concerts and performances.</em>

</div>

---

## 🌍 The problem

Live music is heavily dependent on sound, making concerts largely inaccessible to deaf and
hard-of-hearing audiences. Captions work well for recorded media, but they often fail in live,
noisy environments — where timing, emotion, and context matter just as much as the words.

Silent Stage explores a prototype system for **AI-generated sign-language avatars** that aim to
close this gap in live settings. Rather than chasing perfect translation, the goal is to demonstrate
how AI, accessibility design, and real-time systems can come together to make live events more
inclusive. It's built as a **proof-of-concept**, emphasizing system design, extensibility, and
clarity of data flow over production-level accuracy.

<!-- 📸 Add a screenshot/GIF of the avatar interface here: docs/demo.png -->

## 🧩 System architecture

Silent Stage follows a modular pipeline so each stage can be improved independently:

| Layer | Responsibility |
|---|---|
| 🎙️ **Audio Input** | Captures live audio streams |
| 🔤 **Processing** | Converts speech to text and transforms it into sign-friendly structured output |
| 🧠 **Inference** | ML-based pose extraction and avatar signal generation |
| 🕺 **Visualization** | Renders the animated sign-language avatar in the frontend |

This modular design means an improved speech model or avatar system can drop in without
restructuring the whole pipeline.

## 📁 Project structure

```
backend/    FastAPI server for pose extraction and ML inference
frontend/   Next.js application for the UI and avatar rendering
```

## 🚀 Getting started

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## 🛠️ Tech Stack

![Next.js](https://img.shields.io/badge/Next.js-000000?logo=next.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

---

<div align="center">
<sub>Built by <a href="https://github.com/hirakparekh">@hirakparekh</a> · Licensed under MIT · A proof-of-concept exploration in assistive technology</sub>
</div>
