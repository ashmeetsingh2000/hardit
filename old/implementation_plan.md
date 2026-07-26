# Implementation Plan for Recreating Mobile Webpage

## Goal
Recreate the mobile version of `https://webgency.tilda.ws/template5` as a static, self‑contained HTML/CSS project with local assets. The result should be pixel‑accurate (95‑99%) to the original.

## User Review Required
[!IMPORTANT]
- **Asset Download**: The script will download ~60 images and a few font files from `static.tildacdn.net`. Verify that you have permission to host these assets locally. If any asset is protected, a placeholder will be generated and clearly marked for manual replacement.
- **RSVP Form**: The original page uses a Tilda‑generated popup with form handling. We will recreate the visual UI only (no backend). Confirm if you need a functional form (e.g., email submit) or just the visual placeholder.
- **Animations**: The original uses Tilda’s animation engine (scale, fade, slide). We will approximate these with CSS transitions/animations. Let us know if any animation must be exact (e.g., envelope opening), otherwise we will use a close visual match.
- **Fonts**: The page loads Google Font **Ovo** and several custom `@font-face` families (`Template1`, `Unique`, `newtemplate`). We will include the Google Font and map custom families to the closest Google equivalents (e.g., `Playfair Display`, `Cormorant`). Confirm if you prefer to keep the custom Tilda‑hosted fonts (we can download the `.woff` files) or replace them with Google fonts.

## Open Questions
- **Form Backend**: Should we integrate a simple `mailto:` action for the RSVP form, or leave it as a non‑functional placeholder?
- **Video / Audio**: The page includes an audio element (`Alex Warren - Ordinary Lyrics.mp3`) and no visible video. Do you want these assets included (downloaded) or omitted?
- **Color Palette**: Do you want us to extract exact HEX colors from the CSS, or are we allowed to define a curated palette based on the visual inspection?
- **Deployment Target**: Will you host the project on a static file server (GitHub Pages) that serves the `images/` and `videos/` folders? This affects relative paths.

## Proposed Changes
We will create the following files in the project root (`c:/Users/User/Desktop/Weddingtemplate/viktor and paula/code`):

### [NEW] `index.html`
- Semantic HTML5 structure:
  - `<header>` containing the envelope graphic and opening button.
  - `<main>` with sections: Hero, Wedding Details, Countdown, Schedule, Location, Dress Code, Details, RSVP Popup, Footer.
  - `<footer>` with thank‑you text.
- All text will be copied verbatim from the original page (see analysis output).
- Image tags will reference local files in `images/` (e.g., `<img src="images/Polygon_4.png" alt="" class="hero‑bg‑left">`).
- The RSVP popup will be a hidden `<dialog>` that becomes visible on button click, styled to match the original.

### [NEW] `style.css`
- Reset / base styles (box‑sizing, margin, font smoothing).
- Import Google Font **Ovo** and any chosen fallback fonts.
- Section‑specific styles using BEM‑like class names (e.g., `.hero`, `.countdown`, `.schedule`).
- Media queries for the required mobile widths (360‑430 px). The layout will be fluid, using `max-width: 100%` and flexbox/grid where appropriate.
- Recreate key animations:
  - Envelope opening (scale + slide) using `@keyframes envelopeOpen`.
  - Fade‑in for elements on scroll using `opacity` transition and the `IntersectionObserver` helper (tiny JS snippet).
- Colors, shadows, border‑radius, and spacing will be extracted from the Tilda CSS blocks (the `<style>` element inside each `rec`). We will copy the exact values (e.g., `#66021f` for title text, `rgba(0,0,0,.45)` overlay).
- All custom CSS will be grouped under comment headings (`/* HERO */`, `/* COUNTDOWN */`, etc.) as required.

### [NEW] `script.js` (optional, minimal)
- Small helper to open/close the RSVP dialog and trigger scroll‑reveal animations.
- No external libraries.

### [NEW] `images/` folder
- Download every image URL discovered in the analysis (≈ 60). Filenames will be the original basename (e.g., `Polygon_4.png`).
- A placeholder `placeholder.png` will be generated for any asset that cannot be downloaded.
- Add a `README.txt` inside the folder noting any placeholders.

### [NEW] `videos/` folder (if needed)
- The page only contains an audio file (`Alex Warren - Ordinary Lyrics.mp3`). We'll place it in `audio/` (or `videos/` as per spec) as `ordinary_lyrics.mp3` and reference it locally.

### [NEW] `assets/` (optional) – could be merged with `images/`.

## Verification Plan
1. **Build Verification**: Run a local HTTP server (`python -m http.server 8000`) and open `http://localhost:8000` on a mobile‑sized viewport (Chrome dev tools). Ensure layout matches the original screenshots.
2. **Visual Diff**: Use a headless browser to capture screenshots of each section and compare them side‑by‑side with the original (manual review).
3. **Responsive Test**: Resize the viewport to 360 px, 375 px, 390 px, 393 px, 412 px, 430 px and verify no overflow or layout break.
4. **Interaction Test**: Click the envelope opening element and the RSVP button to confirm animations and popup work.
5. **Asset Check**: Verify that all `<img>` `src` attributes point to files that exist in the `images/` folder.

### Automated Tests (optional)
- None required for a static visual replica, but a simple script could verify that all asset files exist.

---
*All file paths are relative to the project root. The implementation will respect the folder structure you provided.*

**Next Step**: Await your approval or answers to the open questions before generating the files.
