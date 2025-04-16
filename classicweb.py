import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar,
    QLineEdit, QAction, QMenuBar, QMenu, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pywinstyles
from PyQt5.QtGui import QIcon

class ClassicalWebBrowserPro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Classical Web Browser Pro")
        self.setGeometry(100, 100, 1200, 800)

        # Set application icon
        self.setWindowIcon(QIcon('icon.png'))  # Make sure 'icon.png' is in the same directory

        # Web Engine View
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # Navigation toolbar
        nav_bar = QToolBar("Navigation")
        self.addToolBar(nav_bar)

        back_btn = QAction("◀", self)
        back_btn.triggered.connect(self.browser.back)
        nav_bar.addAction(back_btn)

        forward_btn = QAction("▶", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_btn)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_btn)

        home_btn = QAction("⌂", self)
        home_btn.triggered.connect(self.navigate_home)
        nav_bar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_urlbar)

        # Create the File menu and About action
        self.create_menu()

        # Apply classic Win7 style
        pywinstyles.apply_style(self, style="win7")

    def create_menu(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # Add File menu
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Add About action to the File menu
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        file_menu.addAction(about_action)

    def show_about(self):
        # Display About dialog
        about_message = (
            "Classical Web Browser Pro\n"
            "Version 1.0\n\n"
            "A simple web browser with classic styling using PyQt5 and pywinstyles.\n"
            ""
        )
        QMessageBox.about(self, "About Classical Web Browser Pro", about_message)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, qurl):
        self.url_bar.setText(qurl.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassicalWebBrowserPro()
    window.show()
    sys.exit(app.exec_())

