import webbrowser
import clipboard

if len(sys.argv) >1:
    address = "  ".join(sys.argv [1:] )
else:
    address = clipboard.paste()
webbrowser.open('http://www.google.com/maps/place/' + address)