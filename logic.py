import os

import markdown

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import (
    QCloseEvent,
    QColor,
    QFont,
    QSyntaxHighlighter,
    QTextCharFormat,
    QTextCursor,
)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import QDialog, QFileDialog, QInputDialog, QMainWindow, QMessageBox

from ui.mainwindow import Ui_MainWindow


class MarkdownHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        heading_format = QTextCharFormat()
        heading_format.setForeground(QColor("#ea00ff"))
        heading_format.setFontWeight(QFont.Bold)
        self.highlighting_rules.append(
            (QRegularExpression(r"^\s{0,3}#{1,6}\s.*$"), heading_format)
        )

        bold_format = QTextCharFormat()
        bold_format.setForeground(QColor("#ea00ff"))
        bold_format.setFontWeight(QFont.Bold)
        self.highlighting_rules.append(
            (QRegularExpression(r"\*\*[^*\n]+\*\*|__[^_\n]+__"), bold_format)
        )

        italic_format = QTextCharFormat()
        italic_format.setForeground(QColor("#ea00ff"))
        italic_format.setFontItalic(True)
        self.highlighting_rules.append(
            (QRegularExpression(r"\*[^*\n]+\*|_[^_\n]+_"), italic_format)
        )

        code_format = QTextCharFormat()
        code_format.setForeground(QColor("#20c997"))
        self.highlighting_rules.append((QRegularExpression(r"`[^`\n]+`"), code_format))
        self.highlighting_rules.append((QRegularExpression(r"^\s*```.*$"), code_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.highlighting_rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)


class MainWindowLogic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_file = None
        self.custom_styles = {}
        self._active_printer = None
        self._print_callback = None
        self.highlighter = MarkdownHighlighter(self.input_md.document())
        self.setWindowTitle("MarkStudio")

        self.input_md.textChanged.connect(self.update_preview)
        self.actionNew.triggered.connect(self.new_file)
        self.actionNewfile_2.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpenfile.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_2.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.save_file_as)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionQuit.triggered.connect(self.close_application)
        self.actionUndo.triggered.connect(self.input_md.undo)
        self.actionRedo.triggered.connect(self.input_md.redo)
        self.actionBold.triggered.connect(self.bold)
        self.actionItalic.triggered.connect(self.italic)
        self.actionLink.triggered.connect(self.link)
        self.actionImage.triggered.connect(self.image)
        self.actionQuotation.triggered.connect(self.quotation)
        self.actionICode.triggered.connect(self.inline_code)
        self.actionBCode.triggered.connect(self.block_code)
        self.actionLNBreak.triggered.connect(self.line_break)
        self.actionLine.triggered.connect(self.line)
        self.select_header.activated.connect(self.insert_header)
        self.select_list.activated.connect(self.insert_list)
        self.select_style.currentIndexChanged.connect(self.update_preview)
        self.actionBasic.triggered.connect(lambda: self.select_style.setCurrentIndex(0))
        self.actionGitHub_style.triggered.connect(lambda: self.select_style.setCurrentIndex(1))
        self.actionLocal_CSS.triggered.connect(self.local_css)
        self.actionOnline_CSS.triggered.connect(self.online_css)

        self.update_preview()

    def _print_override_css(self):
        return (
            "<style>"
            "@media print {"
            "  html, body {"
            "    -webkit-print-color-adjust: exact !important;"
            "    print-color-adjust: exact !important;"
            "  }"
            "  body { margin: 12mm !important; }"
            "}"
            "</style>"
        )

    def _render_html(self, text):
        if self.toc_check.isChecked():
            full = "[TOC]\n\n" + text
        else:
            full = text

        body = markdown.markdown(
            full,
            extensions=["extra", "codehilite", "toc", "fenced_code", "tables", "nl2br"],
        )

        style_index = self.select_style.currentIndex()
        if style_index == 1:
            css = (
                "<link rel='stylesheet' "
                "href='https://cdnjs.cloudflare.com/ajax/libs/"
                "github-markdown-css/5.1.0/github-markdown.min.css'>"
            )
            print_css = self._print_override_css()
            return (
                f"<html><head>{print_css}{css}</head>"
                f"<body class='markdown-body markdown-preview'>{body}</body></html>"
            )
        elif style_index == 2:
            css = """
<style>
            body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
               "Hiragino Kaku Gothic ProN", "Noto Sans JP",
               Meiryo, sans-serif;
  font-size: 16px;
  line-height: 1.75;
  color: #24292f;
  background-color: #ffffff;
  margin: 0;
  padding: 2rem;
}

main, .markdown-body {
  max-width: 780px;
  margin: 0 auto;
}

h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  line-height: 1.35;
  margin-top: 2.2em;
  margin-bottom: 0.8em;
}

h1 {
  font-size: 2.2rem;
  border-bottom: 2px solid #eaecef;
  padding-bottom: 0.4em;
}

h2 {
  font-size: 1.7rem;
  border-bottom: 1px solid #eaecef;
  padding-bottom: 0.3em;
}

h3 {
  font-size: 1.35rem;
}

p {
  margin: 1em 0;
}

strong {
  font-weight: 600;
}

em {
  font-style: italic;
  color: #444;
}

ul, ol {
  padding-left: 1.6em;
  margin: 1em 0;
}

li {
  margin: 0.4em 0;
}

a {
  color: #0969da;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}


code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.95em;
  background-color: #f6f8fa;
  padding: 0.2em 0.4em;
  border-radius: 4px;
}

pre {
  background-color: #f6f8fa;
  padding: 1em 1.2em;
  overflow-x: auto;
  border-radius: 6px;
  margin: 1.5em 0;
}

pre code {
  padding: 0;
  background: none;
}

blockquote {
  margin: 1.5em 0;
  padding: 0.6em 1.2em;
  color: #57606a;
  background-color: #f6f8fa;
  border-left: 4px solid #d0d7de;
}

table {
  border-collapse: collapse;
  margin: 1.5em 0;
  width: 100%;
}

th, td {
  border: 1px solid #d0d7de;
  padding: 0.6em 0.8em;
}

th {
  background-color: #f6f8fa;
  font-weight: 600;
}

hr {
  border: none;
  border-top: 1px solid #d0d7de;
  margin: 2.5em 0;
           
}
</style>
            """
            print_css = self._print_override_css()
            return (
                f"<html><head>{print_css}{css}</head>"
                f"<body class='markdown-body markdown-preview'>{body}</body></html>"
            )

        if style_index in self.custom_styles:
            css_type, css_value = self.custom_styles[style_index]
            print_css = self._print_override_css()
            if css_type == "inline":
                return (
                    f"<html><head>{print_css}<style>{css_value}</style></head>"
                    f"<body class='markdown-body markdown-preview'>{body}</body></html>"
                )
            if css_type == "url":
                css_link = f"<link rel='stylesheet' href='{css_value}'>"
                return (
                    f"<html><head>{print_css}{css_link}</head>"
                    f"<body class='markdown-body markdown-preview'>{body}</body></html>"
                )

        print_css = self._print_override_css()
        return f"<html><head>{print_css}</head><body>{body}</body></html>"

    def update_preview(self):
        self.view_md.setHtml(self._render_html(self.input_md.toPlainText()))

    def _maybe_save_before_destructive_action(self):
        if not self.input_md.document().isModified():
            return True

        response = QMessageBox.question(
            self,
            "確認",
            "変更を保存しますか？",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )
        if response == QMessageBox.Yes:
            return self.save_file()
        if response == QMessageBox.No:
            return True
        return False

    def new_file(self):
        if not self._maybe_save_before_destructive_action():
            return
        self.input_md.clear()
        self.current_file = None
        self.setWindowTitle("MarkStudio")
        self.input_md.document().setModified(False)

    def open_file(self):
        if not self._maybe_save_before_destructive_action():
            return
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Markdown (*.md);;All Files (*)"
        )
        if not file_path:
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.input_md.setPlainText(f.read())
        except OSError as e:
            QMessageBox.warning(self, "Open Error", str(e))
            return
        self.current_file = file_path
        self.setWindowTitle(f"MarkStudio - {file_path}")
        self.input_md.document().setModified(False)

    def save_file(self):
        if not self.current_file:
            return self.save_file_as()

        try:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.input_md.toPlainText())
        except OSError as e:
            QMessageBox.warning(self, "Save Error", str(e))
            return False

        self.input_md.document().setModified(False)
        return True

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File As",
            "",
            "Markdown (*.md);;HTML (*.html);;All Files (*)",
        )
        if not file_path:
            return False

        if file_path.endswith(".html"):
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self._render_html(self.input_md.toPlainText()))
            except OSError as e:
                QMessageBox.warning(self, "Save Error", str(e))
                return False

            return True

        self.current_file = file_path
        if not self.save_file():
            return False

        self.setWindowTitle(f"MarkStudio - {file_path}")
        return True

    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QDialog.Accepted:
            self._active_printer = printer

            def on_print_finished(success):
                view_finished = getattr(self.view_md, "printFinished", None)
                if view_finished is not None and hasattr(view_finished, "disconnect"):
                    try:
                        view_finished.disconnect(on_print_finished)
                    except (TypeError, RuntimeError):
                        pass
                if success:
                    QMessageBox.information(self, "印刷", "印刷が完了しました。")
                else:
                    QMessageBox.warning(self, "印刷", "印刷に失敗しました。")
                self._active_printer = None
                self._print_callback = None

            self._print_callback = on_print_finished
            page = self.view_md.page()
            page_print = getattr(page, "print", None)
            view_print = getattr(self.view_md, "print", None)

            if callable(page_print):
                try:
                    page_print(printer, on_print_finished)
                    return
                except TypeError:
                    pass
            if callable(view_print):
                try:
                    view_print(printer, on_print_finished)
                    return
                except TypeError:
                    view_finished = getattr(self.view_md, "printFinished", None)
                    if view_finished is not None and hasattr(view_finished, "connect"):
                        view_finished.connect(on_print_finished)
                        view_print(printer)
                        return
                    view_print(printer)
                    on_print_finished(True)
                    return

            self._active_printer = None
            self._print_callback = None
            QMessageBox.warning(
                self,
                "Print",
                "This PySide6/QWebEngine version does not support direct printing.",
            )

    def close_application(self):
        self.close()

    def closeEvent(self, event: QCloseEvent):
        if self._maybe_save_before_destructive_action():
            event.accept()
        else:
            event.ignore()

    def _wrap_selection(self, prefix, suffix=None):
        if suffix is None:
            suffix = prefix
        cursor = self.input_md.textCursor()
        if cursor.hasSelection():
            cursor.insertText(f"{prefix}{cursor.selectedText()}{suffix}")
        else:
            cursor.insertText(f"{prefix}{suffix}")
            cursor.movePosition(
                QTextCursor.MoveOperation.Left,
                QTextCursor.MoveMode.MoveAnchor,
                len(suffix),
            )
            self.input_md.setTextCursor(cursor)

    def bold(self):
        self._wrap_selection("**")

    def italic(self):
        self._wrap_selection("*")

    def link(self):
        url, ok = QInputDialog.getText(self, "リンクを挿入", "URLを入力してください")
        if not ok or not url:
            return
        cursor = self.input_md.textCursor()
        if cursor.hasSelection():
            cursor.insertText(f"[{cursor.selectedText()}]({url})")
        else:
            cursor.insertText(f"[text]({url})")
            cursor.movePosition(
                QTextCursor.MoveOperation.Left,
                QTextCursor.MoveMode.MoveAnchor,
                len(url) + 1,
            )
            self.input_md.setTextCursor(cursor)

    def image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Insert Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
        )
        if not file_path:
            return
        cursor = self.input_md.textCursor()
        cursor.insertText(f"![alt]({file_path})")
        cursor.movePosition(
            QTextCursor.MoveOperation.Left,
            QTextCursor.MoveMode.MoveAnchor,
            len(file_path) + 1,
        )
        self.input_md.setTextCursor(cursor)

    def quotation(self):
        cursor = self.input_md.textCursor()
        if cursor.hasSelection():
            cursor.insertText(f"> {cursor.selectedText()}")
        else:
            cursor.insertText("> ")

    def inline_code(self):
        self._wrap_selection("`")

    def block_code(self):
        cursor = self.input_md.textCursor()
        cursor.insertText("```\n\n```")
        cursor.movePosition(
            QTextCursor.MoveOperation.Up, QTextCursor.MoveMode.MoveAnchor, 1
        )
        self.input_md.setTextCursor(cursor)

    def line_break(self):
        self.input_md.textCursor().insertText("  \n")

    def line(self):
        self.input_md.textCursor().insertText("\n---\n")

    def insert_header(self, index):
        cursor = self.input_md.textCursor()
        level = index + 1
        prefix = "#" * level + " "
        if cursor.hasSelection():
            cursor.insertText(f"{prefix}{cursor.selectedText()}")
        else:
            cursor.insertText(prefix)

    def insert_list(self, index):
        cursor = self.input_md.textCursor()
        if index == 0:
            cursor.insertText("- \n- \n- ")
        elif index == 1:
            cursor.insertText("1. \n2. \n3. ")

    def local_css(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "CSSファイルを選択", "", "CSS (*.css);;All Files (*)"
        )
        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                css_content = f.read()
        except OSError as e:
            QMessageBox.warning(self, "CSS読み込みエラー", str(e))
            return

        item_index = self.select_style.count()
        self.select_style.addItem(f"カスタム: {os.path.basename(file_path)}")
        self.custom_styles[item_index] = ("inline", css_content)
        self.select_style.setCurrentIndex(item_index)
        self.update_preview()

    def online_css(self):
        url, ok = QInputDialog.getText(self, "オンラインCSS", "CSSのURLを入力してください")
        if not ok or not url:
            return

        item_index = self.select_style.count()
        self.select_style.addItem(f"カスタム: {url}")
        self.custom_styles[item_index] = ("url", url)
        self.select_style.setCurrentIndex(item_index)
        self.update_preview()
