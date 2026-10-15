"""
Maintenance script: checks that every solution passes its tests (and nothing is checked
in place: it works on temporary copies). Run from the practice/ folder:
    uv run --with pytest python solutions/check_all.py
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

JOBS = [
    ("exam_A", ROOT / "exam_A", [(ROOT / "solutions/exam_A/src", "src")], "."),
    ("exam_B", ROOT / "exam_B", [(ROOT / "solutions/exam_B/src", "src")], "."),
    ("exam_C", ROOT / "exam_C", [(ROOT / "solutions/exam_C/src", "src"),
                                 (ROOT / "solutions/exam_C/main_duration.py", "main_duration.py"),
                                 (ROOT / "solutions/exam_C/main_stairs.py", "main_stairs.py"),
                                 (ROOT / "solutions/exam_C/main_greenhouse.py", "main_greenhouse.py")], "."),
    ("drills bugs", ROOT, [(ROOT / "solutions/drills/find_the_bug_fixed.py", "drills/find_the_bug.py")], "drills/test_find_the_bug.py"),
    ("drills scratch", ROOT, [(ROOT / "solutions/drills/write_from_scratch_solutions.py", "drills/write_from_scratch.py")], "drills/test_write_from_scratch.py"),
]

ok = True
for name, project, overlays, target_tests in JOBS:
    with tempfile.TemporaryDirectory() as tmp:
        work = pathlib.Path(tmp) / "work"
        shutil.copytree(project, work, ignore=shutil.ignore_patterns("solutions", ".venv", "__pycache__", ".pytest_cache"))
        for source, target in overlays:
            target = work / target
            if source.is_dir():
                shutil.copytree(source, target, dirs_exist_ok=True)
            else:
                shutil.copy(source, target)
        result = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", target_tests], cwd=work,
                                capture_output=True, text=True)
        last = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else result.stderr[-300:]
        print(f"{name:15s} {last}")
        ok = ok and result.returncode == 0
sys.exit(0 if ok else 1)
