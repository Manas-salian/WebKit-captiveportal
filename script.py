import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')  # match your system version

from gi.repository import Gtk, WebKit2

class WebViewApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Login to Wireless Network")
        self.set_default_size(800, 600)

        # Create a WebView
        webview = WebKit2.WebView()

        # Load your desired URL
        webview.load_uri("http://example.com")

        # Add the WebView to the window
        self.add(webview)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    app = WebViewApp()
    Gtk.main()
