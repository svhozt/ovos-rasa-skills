from ovos_utils import classproperty
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


class OVOSRasaSkill(OVOSSkill):
      
    #def initialize(self):
    def __init__(self, *args, **kwargs, skill_id: str = "ovos-rasa-skill"):  ##HW
        super().__init__(*args, **kwargs)  ##HW
        self.skill_id = skill_id
     

    # def __init__(self):
    #     super(RasaSkill, self).__init__("RasaSkill")
    #     # Update this URL to point to your Rasa server
        self.rasa_client = RasaSocketClient("http://host.docker.internal:5005")

        if self.skill_id and bus:
            self._startup(bus, self.skill_id)
            
    def initialize(self):
        
    @property
    @intent_handler(IntentBuilder('askrasa').require('TalkToRasa'))
    def handle_ask_rasa_intent(self, message):
        user_utterance = message.data.get('utterance')
        rasa_response = self.rasa_client.send_to_rasa(user_utterance)
        self.speak(rasa_response)


