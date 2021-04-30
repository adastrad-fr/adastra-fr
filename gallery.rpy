#CG Gallery
# Codebase https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=48056
init-1:
    image introspection = "images/illustrations/introspection.png"
    image adastranl = "images/illustrations/adastranl.png"
    image sleep = "images/illustrations/sleep.png"
    image backoff1 = "images/illustrations/backoff1.png"
    image backoff2 = "images/illustrations/backoff2.png"
    image backoff3 = "images/illustrations/backoff3.png"
    image alexandcassius = "images/illustrations/alexandcassius.png"
    image alexandcassiuskiss = "images/illustrations/alexandcassiuskiss.png"
    image amicusandneferu1 = "images/illustrations/amicusandneferu1.png"
    image amicusandneferu2 = "images/illustrations/amicusandneferu2.png"
    image amicusandneferu3 = "images/illustrations/amicusandneferu3.png"
    image dinner1 = "images/illustrations/dinner1.png"
    image dinner2 = "images/illustrations/dinner2.png"
    image dinner3 = "images/illustrations/dinner3.png"
    image dinner4 = "images/illustrations/dinner4.png"
    image watching = "images/illustrations/watching.png"
    image amiscene1 = "images/illustrations/amiscene1.png"
    image amiscene2 = "images/illustrations/amiscene2.png"
    image amiscene3 = "images/illustrations/amiscene3.png"
    image nefandcat1 = "images/illustrations/nefandcat1.png"
    image nefandcat2 = "images/illustrations/nefandcat2.png"
    image archives1 = "images/illustrations/archives1.png"
    image archives2 = "images/illustrations/archives2.png"
    image archives3 = "images/illustrations/archives3.png"
    image archives4 = "images/illustrations/archives4.png"
    image poisoned = "images/illustrations/poisoned.png"
    image finalspace = "images/illustrations/finalspace.png"
    image finalspace2 = "images/illustrations/finalspace2.png"
    image wemadeit1 = "images/illustrations/wemadeit1.png"
    image wemadeit2 = "images/illustrations/wemadeit2.png"
    image wemadeit3 = "images/illustrations/wemadeit3.png"
    image wemadeit4 = "images/illustrations/wemadeit4.png"
    image ss1 = "images/illustrations/ss1.png"
    image ss2 = "images/illustrations/ss2.png"
    image ss3 = "images/illustrations/ss3.png"
    image 2ss = "images/illustrations/2ss.png"
    image 2ss2 = "images/illustrations/2ss2.png"
    image 2ss3 = "images/illustrations/2ss3.png"
    image adastra = "images/illustrations/adastra.png"
    image farewell1 = "images/illustrations/farewell1.png"
    image farewell2 = "images/illustrations/farewell2.png"
    image farewell3 = "images/illustrations/farewell3.png"
    image farewell4 = "images/illustrations/farewell4.png"
    image amicusend = "images/illustrations/amicusend.png"
    image scippio = "images/illustrations/scippio.png"

init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["introspection", "adastranl", "sleep", "backoff1", "backoff2", "backoff3", "alexandcassius", "alexandcassiuskiss", "amicusandneferu1", "amicusandneferu2", "amicusandneferu3", "dinner1", "dinner2", "dinner3", "dinner2","dinner4", "watching", "amiscene1", "amiscene2", "amiscene3", "nefandcat1", "nefandcat2", "archives1", "archives2", "archives3", "archives4", "poisoned", "finalspace", "finalspace2", "wemadeit1", "wemadeit2", "wemadeit3", "wemadeit4", "ss1", "ss2", "ss3", "2ss", "2ss2", "2ss3", "adastra", "farewell1", "farewell2", "farewell3", "farewell4", "amicusend", "scippio"]
    #how many rows and columns in the gallery screens?
    gal_rows = 2
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 356
    thumbnail_y = 200
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))

screen gallery():
    tag menu

    use game_menu(_("Gallery"), scroll="viewport"):
        hbox:
            style_prefix "galleryhbox"
            grid gal_cols gal_rows:
                style_prefix "galleryhbox"
                spacing 70
                xoffset 45
                $ i = 0
                $ next_cg_page = cg_page + 1            
                if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                    $ next_cg_page = 0
                for gal_item in gallery_cg_items:
                    $ i += 1
                    if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                        add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/lockedCG.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                    null

            frame:
                xpos -650
                ypos 490
                background None
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("gallery")]

style galleryhbox_button_text:
    idle_color "ffffff50"
    hover_color "c9af8f"
    selected_hover_color "c9af8f"
    selected_color "ffffff50"

