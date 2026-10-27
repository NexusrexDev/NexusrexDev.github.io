---
layout: project

# General information
title: "360 Training Management Tool"
release_date: "2026"
release_sort: "2026-03"
target: "Genesis Creations"
pitch: "A tool for synchronizing and managing 360-degree training videos across host and Quest devices."
tech_tags: ["Unity Engine", "C#", "FFMPEG", "Nginx"]
platforms: ["Windows", "Meta Quest"]
role: "Unity Developer"
resume_featured: true

screenshots: ["assets/project_assets/360-training-management-tool/thumbnail.png", "assets/project_assets/360-training-management-tool/360LibraryPlayer.mp4"]

about: "A training application that lets a host device manage a library of 360-degree videos, automatically distribute them to client Quest devices, and play them back in sync."
bullet_points:
  - "Built the host library system with folder and video CRUD operations, uploads, and hash-based validation."
  - "Implemented FFMPEG encoding so uploaded videos could run in Unity without editor imports."
  - "Integrated an Nginx media server and RPC notifications to keep client devices synchronized with the host."
  - "Designed the PC host UI with UI Toolkit and the Quest client UI with uGUI."
---
