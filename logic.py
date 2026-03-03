import markdown

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QColor, QFont, QSyntaxHighlighter, QTextCharFormat, QTextCursor
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import QFileDialog, QInputDialog, QMainWindow, QMessageBox

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

        self.update_preview()

    def _render_html(self, text):
        body = markdown.markdown(
            text, extensions=["extra", "codehilite", "toc", "fenced_code", "tables"]
        )
        if self.select_style.currentIndex() == 1:
            css = (
                "<link rel='stylesheet' "
                "href='https://cdnjs.cloudflare.com/ajax/libs/"
                "github-markdown-css/5.1.0/github-markdown.min.css'>"
            )
            return (
                f"<html><head>{css}</head>"
                f"<body class='markdown-body'>{body}</body></html>"
            )
        return body

    def update_preview(self):
        self.view_md.setHtml(self._render_html(self.input_md.toPlainText()))

    def _maybe_save_before_destructive_action(self):
        if not self.input_md.document().isModified():
            return True
        response = QMessageBox.question(
            self,
            "保存確認",
            "現在の変更を保存しますか？",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )
        if response == QMessageBox.Yes:
            self.save_file()
            return True
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
            self, "ファイルを開く", "", "Markdown (*.md);;All Files (*)"
        )
        if not file_path:
            return
        with open(file_path, "r", encoding="utf-8") as f:
            self.input_md.setPlainText(f.read())
        self.current_file = file_path
        self.setWindowTitle(f"MarkStudio - {file_path}")
        self.input_md.document().setModified(False)

    def save_file(self):
        if not self.current_file:
            self.save_file_as()
            return
        with open(self.current_file, "w", encoding="utf-8") as f:
            f.write(self.input_md.toPlainText())
        self.input_md.document().setModified(False)

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "名前を付けて保存", "", "Markdown (*.md);;All Files (*)"
        )
        if not file_path:
            return
        self.current_file = file_path
        self.save_file()
        self.setWindowTitle(f"MarkStudio - {file_path}")

    def print_file(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.Accepted:
            self.view_md.print(printer)

    def close_application(self):
        if not self._maybe_save_before_destructive_action():
            return
        self.close()

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
        url, ok = QInputDialog.getText(self, "リンク挿入", "URLを入力:")
        if not ok or not url:
            return
        cursor = self.input_md.textCursor()
        if cursor.hasSelection():
            cursor.insertText(f"[{cursor.selectedText()}]({url})")
        else:
            cursor.insertText(f"[表示テキスト]({url})")
            cursor.movePosition(
                QTextCursor.MoveOperation.Left,
                QTextCursor.MoveMode.MoveAnchor,
                len(url) + 1,
            )
            self.input_md.setTextCursor(cursor)

    def image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "画像を挿入",
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
