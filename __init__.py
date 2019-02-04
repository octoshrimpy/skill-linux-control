#~ skill-linux-control - A Mycroft skill to control the linux environment where
#~ Mycroft is running, using your voice
#~
#~ Copyright (C) 2018  octoshrimpy
#~ Github - https://github.com/octoshrimpy

#~ This program is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ This program is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with this program.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import intent_handler
from mycroft import MycroftSkill
from mycroft.util.log import LOG

__author__ = 'octoshrimpy'

class LinuxControl(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(OpenSteamSkill, self).__init__(name="OpenSteamSkill")

    # declaration and programming of skill commands

    # reboot
    @intent_handler(IntentBuilder("RebootIntent").require("RebootKeyword"))
    def handle_reboot_intent(self, message):
        self.speak_dialog("finished.action")

    # shutdown
    @intent_handler(IntentBuilder("ShutDownIntent").require("ShutDownKeyword"))
    def handle_shut_down_intent(self, message):
        self.speak_dialog("finished.action")

    # open steam
    @intent_handler(IntentBuilder("OpenSteamIntent").require("OpenSteamKeyword"))
    def handle_reboot_intent(self, message):
        self.speak_dialog("finished.action")

    def stop(self):
        pass


def create_skill():
    return LinuxControl()



class FinishedBootingSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(FinishedBootingSkill, self).__init__(name="FinishedBootingSkill")

    def initialize(self):
        self.add_event("mycroft.skills.initialized", self.handle_boot_finished)
        LOG.debug('add event handle boot finished')

    def handle_boot_finished(self):
        self.speak_dialog('finished.booting')
        LOG.debug('finished booting')

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return FinishedBootingSkill()
