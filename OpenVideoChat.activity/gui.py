import gtk
from gettext import gettext as _

from sugar.activity.activity import ActivityToolbox
from sugar.graphics.toolbutton import ToolButton

class Gui( gtk.VBox ):
    def __init__(self, activity):
        gtk.VBox.__init__(self)

        self.activity = activity

        # Add movie window
        self.movie_window = gtk.DrawingArea()
        self.pack_start( self.movie_window )

        # Add Chat section
        ##################

        # Chat expander allows chat to be hidden/shown
        chat_expander = gtk.Expander(_("Chat"))
        chat_expander.set_expanded( True )
        self.pack_start( chat_expander, False )

        chat_holder = gtk.VBox()
        chat_expander.add(chat_holder)

        # Create entry and history view for chat
        self.chat_history = gtk.Label("Chat History Here")

        # Send button to complete feel of a chat program
        self.chat_entry = gtk.Entry()
        send_but = gtk.Button( _("Send") )

        # Wrap button and entry in hbox so they are on the same line
        chat_entry_hbox = gtk.HBox()
        chat_entry_hbox.pack_start( self.chat_entry )
        chat_entry_hbox.pack_end( send_but, False )

        # Add chat history and entry to expander
        chat_holder.pack_start( self.chat_history )
        chat_holder.pack_start( chat_entry_hbox, False )

        # Show gui
        self.build_toolbars()
        self.show_all()

    def build_toolbars(self):
        self.settings_bar = gtk.Toolbar()

        self.settings_buttons = {}


        self.settings_buttons['test'] = ToolButton('view-spiral')
        self.settings_buttons['test'].set_tooltip(_("TEST ICON"))
        #self.settings_buttons['test'].connect("clicked", self.view_change_cb, 'new')
        self.settings_bar.insert(self.settings_buttons['test'], -1)

        self.toolbox = ActivityToolbox(self.activity)
        self.toolbox.add_toolbar(_("Settings"), self.settings_bar)

        self.activity.set_toolbox(self.toolbox)
        self.toolbox.show_all()