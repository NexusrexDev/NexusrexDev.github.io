"""Build the Jekyll resume page and export it as a PDF with WeasyPrint."""

from __future__ import annotations

import argparse
import functools
import http.server
import os
import shutil
import subprocess
import threading
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "assets" / "Ahmed Ibrahim Abutahoun Resume.pdf"


def configure_native_runtime() -> list[object]:
    if os.name != "nt":
        return []

    configured = os.environ.get("WEASYPRINT_DLL_DIR")
    candidates = [
        Path(configured) if configured else None,
        Path(r"C:\msys64\ucrt64\bin"),
        Path(r"C:\msys64\mingw64\bin"),
        Path(r"C:\Program Files\GTK3-Runtime Win64\bin"),
    ]
    handles = []
    for candidate in candidates:
        if candidate and candidate.is_dir():
            os.environ["PATH"] = str(candidate) + os.pathsep + os.environ["PATH"]
            handles.append(os.add_dll_directory(str(candidate)))
    return handles


def build_site() -> None:
    bundle = shutil.which("bundle.bat") or shutil.which("bundle")
    if not bundle:
        raise FileNotFoundError(
            "Bundler was not found on PATH. Install Ruby and Bundler before building the resume."
        )
    subprocess.run(
        [bundle, "exec", "jekyll", "build"],
        cwd=ROOT,
        check=True,
    )


def serve_site(site_dir: Path) -> tuple[http.server.ThreadingHTTPServer, threading.Thread, str]:
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=str(site_dir),
    )
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address
    return server, thread, f"http://{host}:{port}"


def write_pdf(output: Path) -> None:
    dll_handles = configure_native_runtime()
    try:
        from weasyprint import HTML
    except ImportError as error:
        raise SystemExit(
            "WeasyPrint is required. Install it with "
            "'python -m pip install -r requirements-resume.txt'."
        ) from error
    except OSError as error:
        raise SystemExit(
            "WeasyPrint's Python package is installed, but its native GTK/Pango "
            "runtime is unavailable. Install the Windows runtime described at "
            "https://doc.courtbouillon.org/weasyprint/stable/first_steps.html "
            "before exporting the PDF."
        ) from error

    site_dir = ROOT / "_site"
    resume_page = site_dir / "resume" / "index.html"
    if not resume_page.is_file():
        raise FileNotFoundError(f"Generated resume page not found: {resume_page}")

    output.parent.mkdir(parents=True, exist_ok=True)
    server, thread, base_url = serve_site(site_dir)
    try:
        HTML(url=f"{base_url}/resume/").write_pdf(str(output))
    finally:
        server.shutdown()
        thread.join()
        server.server_close()
        for handle in dll_handles:
            handle.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="PDF output path, relative to the repository root or absolute.",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Convert the existing _site/resume page without rebuilding Jekyll.",
    )
    args = parser.parse_args()

    output = args.output if args.output.is_absolute() else ROOT / args.output
    if not args.skip_build:
        build_site()
    write_pdf(output)
    print(f"Created {output}")


if __name__ == "__main__":
    main()
