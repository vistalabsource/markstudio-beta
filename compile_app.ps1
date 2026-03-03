python.exe -m nuitka --standalone --onefile --enable-plugin=pyside6 --disable-console --output-filename="MarkStudio.exe" main.py

if (Test-Path "MarkStudio.exe") {
    Write-Host "ビルド成功: MarkStudio.exe が生成されました。"
} else {
    Write-Host "ビルド失敗: MarkStudio.exe が生成されませんでした。"
}