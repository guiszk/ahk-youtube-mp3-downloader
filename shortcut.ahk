#!d:: { ; Win + Alt + D
    try {
        query := InputBox("Enter query", "ahk-youtube-mp3-downloader")
    } catch {
        return ; User pressed Cancel
    }
 
    if (link = "")
        return ; Empty input
 
    Run 'C:\Users\your-username\Documents\ahk-youtube-mp3-downloader\ytsearch.py "' query.Value '"' ; set this to where you downloaded ytsearch.py
}
