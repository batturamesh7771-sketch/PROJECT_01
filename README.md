# # PROJECT 01: 3D Rocket & Live Satellite Orbit Tracker Suite

[![Author](https://img.shields.io/badge/Author-ELONIKHIL-blue.svg)](https://github.com/batturamesh7771-sketch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Google Colab](https://img.shields.io/badge/Colab-Interactive%20Notebook-orange.svg)](https://colab.research.google.com/drive/1kmFMOUY-lEJHc1an83skkmJc29ygtevn?usp=drive_link)
[![3D WebGL](https://img.shields.io/badge/Viewer-Three.js%20WebGL-black.svg)](index.html)

> **Lead Architect & Developer:** **ELONIKHIL** (@batturamesh7771-sketch)  
> **Aerospace Engineering & Orbital Astrodynamics Initiative**

An end-to-end space mission tracking and astrodynamics platform delivering real-time satellite trajectory calculation, 3D WebGL orbital visualization, SGP4/Keplerian orbital propagation, and cloud-based Google Colab analytical workflows.

---

## 📌 Project Overview
* **Interactive 3D Orbit Viewer:** WebGL globe with real-time ground tracks, orbital inclination rendering, and ground station visibility cones.
* **Astrodynamics Solver:** Python numerical propagation based on Kepler's equation and vis-viva orbital velocity.
* **Live Telemetry & Data:** Ephemeris state vectors, TLE parsing, and Starlink / ISS / Hubble orbital catalogs.
* **Google Colab Cloud Suite:** Direct integration with interactive Jupyter research notebooks.

---

## 📂 Repository Architecture

```text
PROJECT_01/
├── index.html                           # Standalone 3D WebGL Satellite & Orbit Tracking Console
├── scripts/
│   └── run_satellite_tracker.py         # SGP4 / Keplerian numerical orbital state propagator
├── data/
│   ├── iss_orbit_telemetry.csv          # Real-time ISS trajectory & ground footprint dataset
│   └── starlink_orbital_catalog.csv     # LEO, MEO, and GEO constellation ephemeris records
├── notebooks/
│   └── Google_Colab_Satellite_Tracker.md # Direct Google Colab cloud execution link & documentation
├── MY PROJECT LINK                      # Original project cloud link reference
├── LICENSE                              # MIT License (Author: ELONIKHIL)
├── .gitignore                           # Python and OS exclusion rules
└── README.md                            # Comprehensive technical documentation
```

---

## 🚀 Quick Start Guide

### 1. Launch Interactive 3D WebGL Tracker
Simply open `index.html` in any web browser to explore real-time orbits, ground track footprints, and satellite telemetry.

### 2. Run Python Astrodynamics Solver
```bash
python scripts/run_satellite_tracker.py
```

### 3. Open Google Colab Research Notebook
Launch the cloud notebook directly:
[Google Colab Satellite & Rocket Tracker](https://colab.research.google.com/drive/1kmFMOUY-lEJHc1an83skkmJc29ygtevn?usp=drive_link)

---

## 👨‍💻 Author & Attribution
* **Lead Engineer:** **ELONIKHIL** (@batturamesh7771-sketch)
* **Project Series:** PROJECT 01 of the Aerospace & Autonomous Systems Portfolio
* **License:** MIT License
