from ovos_workshop.skills.ovos import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_utils.intents import IntentBuilder
import socketio


class RasaSocketClient:
    def __init__(self, rasa_url):
        self.sio = socketio.Client()
        self.response = None

        @self.sio.event
        def connect():
            print("Connected to Rasa")

        @self.sio.event
        def disconnect():
            print("Disconnected from Rasa")

        @self.sio.event
        def bot_uttered(data):
            self.response = data['text']

    def send_to_rasa(self, message):
        self.response = None
        self.sio.emit('user_uttered', {'message': message})
        while self.response is None:
            pass
        return self.response


class RasaSkill(OVOSSkill):
    def initialize(self, *args, **kwargs):
        """The __init__ method is called when the Skill is first constructed.
        Note that self.bus, self.skill_id, self.settings, and
        other base class settings are only available after the call to super().

        This is a good place to load and pre-process any data needed by your
        Skill, ideally after the super() call.
        """
        super().__init__(*args, **kwargs)
    # def __init__(self):
    #     super(RasaSkill, self).__init__("RasaSkill")
    #     # Update this URL to point to your Rasa server
        self.rasa_client = RasaSocketClient("http://host.docker.internal:5005")

    @intent_handler(IntentBuilder('TalkToRasa').require('TalkToRasa'))
    def handle_ask_rasa_intent(self, message):
        user_utterance = message.data.get('utterance')
        rasa_response = self.rasa_client.send_to_rasa(user_utterance)
        self.speak(rasa_response)


