from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evidence_scaffold import scaffold  # noqa: E402

SCRIPT = Path(__file__).resolve().parents[1] / "evidence_scaffold.py"

NAMES = {
    "EVIDENCE_FACTS.md",
    "DOMAIN_NARRATIVE.md",
    "BASELINE_GAP.md",
    "CLAIM_INTERROGATION.md",
    "evidence_manifest.json",
}


def test_scaffold_creates_all_artifacts(tmp_path):
    manifest = scaffold(tmp_path, "Test Paper", "2025-01-01", "NeurIPS", force=False)
    assert set(manifest["artifacts"]) == NAMES - {"evidence_manifest.json"}
    for name in NAMES:
        assert (tmp_path / name).exists(), name
    facts = (tmp_path / "EVIDENCE_FACTS.md").read_text(encoding="utf-8")
    assert "Test Paper" in facts and "2025-01-01" in facts
    gap = (tmp_path / "BASELINE_GAP.md").read_text(encoding="utf-8")
    assert "not_found" in gap
    manifest_disk = json.loads((tmp_path / "evidence_manifest.json").read_text(encoding="utf-8"))
    assert manifest_disk["cutoff_date"] == "2025-01-01"
    assert manifest_disk["venue"] == "NeurIPS"


def test_scaffold_refuses_overwrite(tmp_path):
    scaffold(tmp_path, "Test Paper", "2025-01-01", "NeurIPS")
    with pytest.raises(FileExistsError):
        scaffold(tmp_path, "Test Paper", "2025-01-01", "NeurIPS")


def test_scaffold_force_overwrites(tmp_path):
    scaffold(tmp_path, "Old", "2024-01-01", "ICML")
    manifest = scaffold(tmp_path, "New", "2025-02-02", "ICLR", force=True)
    assert manifest["title"] == "New"
    facts = (tmp_path / "EVIDENCE_FACTS.md").read_text(encoding="utf-8")
    assert "New" in facts and "2025-02-02" in facts


def test_cli_refuses_overwrite(tmp_path):
    scaffold(tmp_path, "Test Paper", "2025-01-01", "NeurIPS")
    r = subprocess.run(
        [sys.executable, "-X", "utf8", str(SCRIPT), "--out", str(tmp_path),
         "--title", "Test Paper", "--cutoff", "2025-01-01", "--venue", "NeurIPS"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 2
    assert "overwrite" in (r.stdout + r.stderr).lower()


def test_cli_force_succeeds(tmp_path):
    r = subprocess.run(
        [sys.executable, "-X", "utf8", str(SCRIPT), "--out", str(tmp_path),
         "--title", "Test Paper", "--cutoff", "2025-01-01", "--venue", "NeurIPS"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0, r.stderr
    assert (tmp_path / "evidence_manifest.json").exists()
