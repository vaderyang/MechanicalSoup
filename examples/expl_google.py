import re
import vsoup

# Connect to Google
browser = vsoup.WebBrowser.New("Chrome on Windows")
browser.open("https://www.google.com/")

# Fill-in the form
browser.select_form('form[action="/search"]')
browser["q"] = "Vader"
browser.submit_selected(btnName="btnG")

# Display links
for link in browser.links():
    target = link.attrs['href']
    # Filter-out unrelated links and extract actual URL from Google's
    # click-tracking.
    if (target.startswith('/url?') and not
            target.startswith("/url?q=http://webcache.googleusercontent.com")):
        target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
        print(link.text + " | " +target)
