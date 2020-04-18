
###### This is the class for game state atributtes. #########

init -10 python:
    class GameState(NoRollback):
        player = ""
        save_name = ""
        chapter = 0
        glossary_items = []
        glossary_items_unread = []
        portrait_done = False
        astell_is_nice = False
        wollstonecraft_is_seen = False
        asmau_is_seen = False
        newspaper_is_read = False
        maze_coords = [36, 0]
        maze_objects = []
