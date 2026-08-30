# post-commit auto-sync: dev repo -> deploy copy (~/.cline/skills)
# Run automatically after commit; can also run manually.
param(
    [string]$Dest = ""
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# repo name -> deploy dir mapping (extend as needed)
$map = @{
    "paper-master"        = "C:\Users\21288\.cline\skills\paper-master"
    "math-modeling-agent" = "C:\Users\21288\.cline\skills\math-modeling-agent"
    "academic-flowchart"  = "C:\Users\21288\.cline\skills\academic-flowchart"
}
$name = Split-Path -Leaf $RepoRoot
if (-not $Dest) {
    if (-not $map.ContainsKey($name)) {
        Write-Output "[sync] unknown repo: $name, skipped"
        exit 0
    }
    $Dest = $map[$name]
}

if (-not (Test-Path $Dest)) {
    New-Item -ItemType Directory -Force -Path $Dest | Out-Null
}

$xd = @(".git", "__pycache__", ".pytest_cache", ".skill-opt", ".venv", "node_modules")
$args = @($RepoRoot, $Dest, "/MIR", "/XF", "*.pyc", "/XD") + $xd +
        @("/NJH", "/NJS", "/NDL", "/NFL", "/R:1", "/W:1")
& robocopy @args | Out-Null
$rc = $LASTEXITCODE
if ($rc -ge 8) {
    Write-Output "[sync] FAILED robocopy rc=$rc ($RepoRoot -> $Dest)"
    exit 1
}
Write-Output "[sync] OK $(Get-Date -Format 'HH:mm:ss') $RepoRoot -> $Dest"
exit 0
