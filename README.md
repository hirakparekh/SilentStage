# Silent Stage

Live music experiences are heavily dependent on sound, making concerts largely inaccessible to deaf and hard-of-hearing audiences. While captions work well for recorded media, they often fail in live, noisy environments where timing, emotion, and context matter just as much as words.

This project explores a prototype system for AI-generated sign language avatars that aim to bridge this accessibility gap in live concert settings. The system follows a modular pipeline that captures audio input, converts speech or lyrics into text, processes the language for sign-friendly representation, and visualizes it through a digital avatar interface.

Rather than focusing on perfect translation, the goal of this project is to demonstrate how AI, accessibility design, and real-time systems can come together to make live events more inclusive. The project is built as a proof-of-concept, emphasizing system design, extensibility, and clarity of data flow over production-level accuracy.

This repository serves as an exploration of how assistive technologies can be reimagined for dynamic, real-world environments like concerts, festivals, and live performances.

## System Architecture Overview

Silent Stage follows a modular pipeline architecture:

1. Audio Input Layer – Captures live audio streams.

2. Processing Layer – Converts speech to text and transforms it into sign-friendly structured output.

3. Inference Layer – Handles ML-based pose extraction and avatar signal generation.

4. Visualization Layer – Renders the animated sign language avatar through the frontend interface.

This modular design ensures extensibility, allowing future integration of improved speech models or enhanced avatar systems without restructuring the entire pipeline.
## Project Structure

- `backend/`: FastAPI server for pose extraction and ML inference.
- `frontend/`: Next.js application for the user interface and avatar rendering.

## Getting Started

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`
