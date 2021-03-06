
###### This is the class for game state atributtes. #########

init -10 python:
    class GameState(NoRollback):
        player = ""
        save_name = ""
        chapters_completed = []
        glossary_items = []
        glossary_items_unread = []
        portrait_done = False
        astell_is_nice = False
        wollstonecraft_is_seen = False
        asmau_is_seen = False
        newspaper_is_read = False
        maze_coords = [36, 0]
        maze_objects = []
        mill_are_nice = False
        coverture_is_found = False
        maze_is_seen = False
        contraception_is_found = False
        suffrage_map_done = False
        gallery_items = []
        gallery_items_unread = []
        campoamor_is_seen = False
        langham_library_is_seen = False
        crosswords_done = False
        pizzey_is_seen = False
        eunuch_is_found = False
        vaginal_orgasm_is_found = False
        witch_is_seen = False
        find_differences_done = False
        nyrw_is_seen = False
        answer_phone = False
        series_done = False
        serie_with_susan = False
        published_article = 0
        eco_is_seen = False
        killjoy_is_seen = False


        def clear(self):
            self.player = ""
            self.save_name = ""
            self.chapters_completed = []
            self.glossary_items = []
            self.glossary_items_unread = []
            self.portrait_done = False
            self.astell_is_nice = False
            self.wollstonecraft_is_seen = False
            self.asmau_is_seen = False
            self.newspaper_is_read = False
            self.maze_coords = [36, 0]
            self.maze_objects = []
            self.mill_are_nice = False
            self.coverture_is_found = False
            self.maze_is_seen = False
            self.contraception_is_found = False
            self.suffrage_map_done = False
            self.gallery_items = []
            self.gallery_items_unread = []
            self.campoamor_is_seen = False
            self.langham_library_is_seen = False
            self.crosswords_done = False
            self.pizzey_is_seen = False
            self.eunuch_is_found = False
            self.vaginal_orgasm_is_found = False
            self.witch_is_seen = False
            self.find_differences_done = False
            self.nyrw_is_seen = False
            self.answer_phone = False
            self.series_done = False
            self.serie_with_susan = False
            self.published_article = 0
            self.eco_is_seen = False
            self.killjoy_is_seen = False
