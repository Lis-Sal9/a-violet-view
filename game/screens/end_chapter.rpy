
init -1 python:
    CHAPTERS = ["P", "1", "2a", "2b", "2c", "3", "E"]

    def addChapterCompleted(chapter_completed):
        global game_state
        if chapter_completed not in game_state.chapters_completed:
            game_state.chapters_completed.append(chapter_completed)

    def isGameCompleted():
        for chapter in CHAPTERS:
            if chapter not in game_state.chapters_completed:
                return False
        return True

label end_chapter(chapter_completed):
    $ addChapterCompleted(chapter_completed)
    $ game_completed = isGameCompleted()
    stop music fadeout 0.5
    if game_completed:
        return
    else:
        call screen library
