param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("backup", "restore")]
    [string]$Mode,

    [Parameter(Mandatory = $true)]
    [string]$DbName,

    [string]$DbHost = "localhost",
    [string]$DbPort = "5432",
    [string]$DbUser = "odoo-user",
    [string]$DbPassword = "",

    [string]$RepoRoot = "E:\ODOO\odoo-19.0",
    [string]$PgBin = "C:\Program Files\PostgreSQL\17\bin",
    [string]$DataDir = "C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo",
    [string]$OutputDir = ".\handover_out",
    [switch]$IncludeCustomAddons
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Assert-PathExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PathValue,
        [Parameter(Mandatory = $true)]
        [string]$Label
    )
    if (-not (Test-Path -LiteralPath $PathValue)) {
        throw "$Label khong ton tai: $PathValue"
    }
}

function Ensure-OutputDir {
    param([string]$PathValue)
    if (-not (Test-Path -LiteralPath $PathValue)) {
        New-Item -ItemType Directory -Path $PathValue | Out-Null
    }
}

function Resolve-ToolPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$BinDir,
        [Parameter(Mandatory = $true)]
        [string]$ExeName
    )
    $tool = Join-Path $BinDir $ExeName
    Assert-PathExists -PathValue $tool -Label $ExeName
    return $tool
}

function Export-Db {
    param(
        [string]$DumpFile,
        [string]$Host,
        [string]$Port,
        [string]$User,
        [string]$Database,
        [string]$PgDumpExe
    )
    Write-Host "Dang backup DB $Database -> $DumpFile"
    & $PgDumpExe --format=custom --no-owner --no-privileges --host $Host --port $Port --username $User --dbname $Database --file $DumpFile
    if ($LASTEXITCODE -ne 0) {
        throw "pg_dump that bai voi ma loi $LASTEXITCODE"
    }
}

function Restore-Db {
    param(
        [string]$DumpFile,
        [string]$Host,
        [string]$Port,
        [string]$User,
        [string]$Database,
        [string]$DropDbExe,
        [string]$CreatedbExe,
        [string]$PgRestoreExe
    )
    Write-Host "Dang drop/create DB $Database"
    & $DropDbExe --if-exists --host $Host --port $Port --username $User $Database
    & $CreatedbExe --host $Host --port $Port --username $User $Database
    if ($LASTEXITCODE -ne 0) {
        throw "createdb that bai voi ma loi $LASTEXITCODE"
    }

    Write-Host "Dang restore dump $DumpFile vao DB $Database"
    & $PgRestoreExe --clean --if-exists --no-owner --no-privileges --host $Host --port $Port --username $User --dbname $Database $DumpFile
    if ($LASTEXITCODE -ne 0) {
        throw "pg_restore that bai voi ma loi $LASTEXITCODE"
    }
}

function Copy-Filestore {
    param(
        [ValidateSet("export", "import")]
        [string]$Action,
        [string]$Database,
        [string]$DataDirectory,
        [string]$TargetRoot
    )
    $sourcePath = Join-Path (Join-Path $DataDirectory "filestore") $Database
    $targetPath = Join-Path (Join-Path $TargetRoot "filestore") $Database

    if ($Action -eq "export") {
        Assert-PathExists -PathValue $sourcePath -Label "Filestore source"
        if (-not (Test-Path -LiteralPath (Join-Path $TargetRoot "filestore"))) {
            New-Item -ItemType Directory -Path (Join-Path $TargetRoot "filestore") | Out-Null
        }
        Write-Host "Dang copy filestore -> $targetPath"
        Copy-Item -Path $sourcePath -Destination $targetPath -Recurse -Force
    }
    else {
        Assert-PathExists -PathValue $targetPath -Label "Filestore package"
        if (-not (Test-Path -LiteralPath (Join-Path $DataDirectory "filestore"))) {
            New-Item -ItemType Directory -Path (Join-Path $DataDirectory "filestore") | Out-Null
        }
        Write-Host "Dang copy filestore -> $sourcePath"
        if (Test-Path -LiteralPath $sourcePath) {
            Remove-Item -Path $sourcePath -Recurse -Force
        }
        Copy-Item -Path $targetPath -Destination $sourcePath -Recurse -Force
    }
}

function Package-CustomAddons {
    param(
        [string]$RepositoryRoot,
        [string]$TargetRoot
    )
    $addonsPath = Join-Path $RepositoryRoot "addons_custom"
    Assert-PathExists -PathValue $addonsPath -Label "addons_custom"

    $zipPath = Join-Path $TargetRoot "addons_custom.zip"
    if (Test-Path -LiteralPath $zipPath) {
        Remove-Item -Path $zipPath -Force
    }

    Write-Host "Dang dong goi addons_custom -> $zipPath"
    Compress-Archive -Path (Join-Path $addonsPath "*") -DestinationPath $zipPath
}

if ($DbPassword -ne "") {
    $env:PGPASSWORD = $DbPassword
}

Ensure-OutputDir -PathValue $OutputDir
Assert-PathExists -PathValue $PgBin -Label "PgBin"
Assert-PathExists -PathValue $DataDir -Label "DataDir"

$pgDump = Resolve-ToolPath -BinDir $PgBin -ExeName "pg_dump.exe"
$pgRestore = Resolve-ToolPath -BinDir $PgBin -ExeName "pg_restore.exe"
$dropdb = Resolve-ToolPath -BinDir $PgBin -ExeName "dropdb.exe"
$createdb = Resolve-ToolPath -BinDir $PgBin -ExeName "createdb.exe"
$dumpPath = Join-Path $OutputDir "$DbName.dump"

if ($Mode -eq "backup") {
    Export-Db -DumpFile $dumpPath -Host $DbHost -Port $DbPort -User $DbUser -Database $DbName -PgDumpExe $pgDump
    Copy-Filestore -Action "export" -Database $DbName -DataDirectory $DataDir -TargetRoot $OutputDir

    if ($IncludeCustomAddons) {
        Package-CustomAddons -RepositoryRoot $RepoRoot -TargetRoot $OutputDir
    }

    Write-Host "Backup hoan tat. Thu muc: $OutputDir"
}
else {
    Assert-PathExists -PathValue $dumpPath -Label "Dump file"
    Restore-Db -DumpFile $dumpPath -Host $DbHost -Port $DbPort -User $DbUser -Database $DbName -DropDbExe $dropdb -CreatedbExe $createdb -PgRestoreExe $pgRestore
    Copy-Filestore -Action "import" -Database $DbName -DataDirectory $DataDir -TargetRoot $OutputDir
    Write-Host "Restore hoan tat cho DB: $DbName"
}
