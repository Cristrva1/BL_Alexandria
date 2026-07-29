# 11. Generación de Imagen & Visión — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `comfyui`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** The most powerful and modular AI engine for content creation.**.
**Stack:** python, typescript, javascript, react, docker, comfy
**Repo:** https://github.com/Comfy-Org/ComfyUI.git

**Instalación** [~]: `git clone https://github.com/Comfy-Org/ComfyUI.git && cd ComfyUI && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `stable-diffusion-webui`

## `comfyui-ipadapter-plus`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** The IPAdapter are very powerful models for image-to-image conditioning. The subject or even just the style of the reference image(s) can be easily transferred to a generation. Think of it as a 1-image lora.
**Stack:** python, typescript, javascript, postgres, comfy
**Repo:** https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

**Instalación** [~]: `pip install comfyui_ipadapter_plus   (o: uv add comfyui_ipadapter_plus)`
_Nombre PyPI puede diferir de 'ComfyUI_IPAdapter_plus'; verifica en pypi.org._

**Elige si:** quieres comfyui ipadapter plus
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `controlnet`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** News: A nightly version of ControlNet 1.1 is released!
**Stack:** python, typescript
**Repo:** https://github.com/lllyasviel/ControlNet.git

**Instalación** [~]: `pip install controlnet   (o: uv add controlnet)`
_Nombre PyPI puede diferir de 'ControlNet'; verifica en pypi.org._

**Elige si:** quieres news: a nightly version of controlnet 1.1 is released!
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `cosmos`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Table of Contents.
**Stack:** python, typescript, docker, postgres
**Repo:** https://github.com/NVIDIA/cosmos.git

**Instalación** [~]: `git clone https://github.com/NVIDIA/cosmos.git && cd cosmos && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** —
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `comfyui`, `stable-diffusion-webui`

## `deep-live-cam`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Real-time face swap and video deepfake with a single click and only a single image.
**Stack:** python, typescript, postgres
**Repo:** https://github.com/hacksider/Deep-Live-Cam.git

**Instalación** [~]: `git clone https://github.com/hacksider/Deep-Live-Cam.git && cd Deep-Live-Cam && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres deep-live-cam 2.1.6
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `diffusers`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at.
**Stack:** python, typescript, postgres
**Repo:** https://github.com/huggingface/diffusers.git

**Instalación** [~]: `pip install diffusers   (o: uv add diffusers)`
_Nombre PyPI puede diferir de 'diffusers'; verifica en pypi.org._

**Elige si:** quieres copyright 2022 - the huggingface team. all rights reserved.
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `face-recognition`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** _You can also read a translated version of this file in Chinese 简体中文版 or in Korean 한국어 or in Japanese 日本語._.
**Stack:** python, typescript, docker, postgres
**Repo:** https://github.com/ageitgey/face_recognition.git

**Instalación** [~]: `pip install face_recognition   (o: uv add face_recognition)`
_Nombre PyPI puede diferir de 'face_recognition'; verifica en pypi.org._

**Elige si:** quieres face recognition
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `fooocus`
role=skill · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Fooocus is an image generating software (based on Gradio ).
**Stack:** python, typescript, javascript, docker, comfy
**Repo:** https://github.com/lllyasviel/Fooocus.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Fooocus/). Si necesitas el código: git clone https://github.com/lllyasviel/Fooocus.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** —
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `gfpgan`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** 1. :boom: **Updated** online demo: ![Replicate](https://replicate.com/tencentarc/gfpgan). Here is the backup. 1. :boom: **Updated** online demo: ![Huggingface Gradio](https://huggingface.co/spaces/Xintao/GFPGAN) 1. .
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/TencentARC/GFPGAN.git

**Instalación** [~]: `pip install gfpgan   (o: uv add gfpgan)`
_Nombre PyPI puede diferir de 'GFPGAN'; verifica en pypi.org._

**Elige si:** quieres 1. :boom: **updated** online demo: [![replicate](https://img.shields.io/static/v
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `invokeai`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Invoke - Professional Creative AI Tools for Visual Media.
**Stack:** python, typescript, javascript, react, docker
**Repo:** https://github.com/invoke-ai/InvokeAI.git

**Instalación** [~]: `git clone https://github.com/invoke-ai/InvokeAI.git && cd InvokeAI && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres invoke - professional creative ai tools for visual media
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `litellm`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, Bedrock, Azure, and more — using the OpenAI format.
**Stack:** python, typescript, javascript, docker, postgres
**Repo:** https://github.com/BerriAI/litellm.git

**Instalación** [~]: `git clone https://github.com/BerriAI/litellm.git && cd litellm && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres 🚅 litellm
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `cosmos`, `comfyui`, `stable-diffusion-webui`

## `liveportrait`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** `2025/06/01`**: 🌍 Over the past year, **LivePortrait** has 🚀 become an efficient portrait-animation (humans, cats and dogs) solution adopted by major video platforms—Kuaishou, Douyin, Jianying, WeChat Channels—as well as numerous startups and creators. 🎉 `2025/01/01`**: 🐶 We updated a new version of the Animals model with more data, see **here**. `2024/10/18`**: ❗ We have upda.
**Stack:** python, typescript, javascript, postgres, comfy
**Repo:** https://github.com/KlingAIResearch/LivePortrait.git

**Instalación** [~]: `pip install liveportrait   (o: uv add liveportrait)`
_Nombre PyPI puede diferir de 'LivePortrait'; verifica en pypi.org._

**Elige si:** quieres liveportrait: efficient portrait animation with stitching and retargeting control
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `luxtts`
role=directory · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and realistic generation at speeds exceeding 150x realtime.
**Stack:** python, typescript, javascript, comfy
**Repo:** https://github.com/ysharma3501/LuxTTS.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/LuxTTS/). Si necesitas el código: git clone https://github.com/ysharma3501/LuxTTS.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** —
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `nemo`
role=runtime · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Checkout our HuggingFace🤗 collection for the latest open weight checkpoints and demos!.
**Stack:** python, typescript, docker
**Repo:** https://github.com/NVIDIA-NeMo/NeMo.git

**Instalación** [~]: `git clone https://github.com/NVIDIA-NeMo/NeMo.git && cd NeMo && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres **nvidia nemo speech**
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `sd-webui-controlnet`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** The WebUI extension for ControlNet and other injection-based SD controls.
**Stack:** python, typescript, postgres
**Repo:** https://github.com/Mikubill/sd-webui-controlnet.git

**Instalación** [~]: `pip install sd-webui-controlnet   (o: uv add sd-webui-controlnet)`
_Nombre PyPI puede diferir de 'sd-webui-controlnet'; verifica en pypi.org._

**Elige si:** quieres controlnet for stable diffusion webui
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `stable-diffusion-webui`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** A web interface for Stable Diffusion, implemented using Gradio library.
**Stack:** python, typescript, javascript, postgres
**Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/stable-diffusion-webui/). Si necesitas el código: git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres stable diffusion web ui
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`

## `tts`
role=library · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** 📣 ⓍTTSv2 is here with 16 languages and better performance across the board. 📣 ⓍTTS fine-tuning code is out. Check the example recipes. 📣 ⓍTTS can now stream with <200ms latency. 📣 ⓍTTS, our production TTS model that can speak 13 languages, is released Blog Post, Demo, [Docs](.
**Stack:** python, typescript, docker
**Repo:** https://github.com/coqui-ai/TTS.git

**Instalación** [~]: `pip install tts   (o: uv add tts)`
_Nombre PyPI puede diferir de 'TTS'; verifica en pypi.org._

**Elige si:** quieres 🐸coqui.ai news
**Evita si:** el caso no requiere generación multimedia o ya usas alternativas dedicadas
**Combina con:** `litellm`, `cosmos`, `comfyui`
