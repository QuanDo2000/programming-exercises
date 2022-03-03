param ($name = $(throw "Name parameter is required."))

$source = $PSScriptRoot
$file = "./$name.cpp"

if (-not(Test-Path -Path $file -PathType Leaf)) {
  try {
    $null = New-Item -ItemType File -Path $file -Force -ErrorAction Stop
    (Get-Content -Path "$source/template.cpp") | Set-Content -Path $file
    Write-Host "The file [$file] has been created."
  }
  catch {
    throw $_.Exception.Message
  }
}
else {
  Write-Host "File [$file] already exists."
}

$null = New-Item -ItemType File -Path "./$name.inp" -Force -ErrorAction Stop
$null = New-Item -ItemType File -Path "./$name.sout" -Force -ErrorAction Stop

code ./$name.inp
code ./$name.sout
code ./$name.cpp