import base64
import webbrowser
rickroll = "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ=="
rickroll = base64.b64decode(rickroll).decode("utf-8")
webbrowser.open(rickroll)