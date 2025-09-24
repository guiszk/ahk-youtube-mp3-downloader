#!d:: { ; Win + Alt + D
    try {
        link := InputBox("Enter query", "ytsearch")
    } catch {
        return ; User pressed Cancel
    }
 
    if (link = "")
        return ; Empty input
 
    Run '~/Documents/ahk-youtube-mp3-downloader/ytsearch.py "' link.Value '"' ; set this to where you downloaded ytsearch.py
}
