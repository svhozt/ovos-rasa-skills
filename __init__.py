from ovos_workshop.skills.ovos import MycroftSkill
from ovos_workshop.decorators import intent_handler
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


class RasaSkill(MycroftSkill):
    def __init__(self):
        super(RasaSkill, self).__init__("RasaSkill")
        # Update this URL to point to your Rasa server
        self.rasa_client = RasaSocketClient("http://host.docker.internal:5005")

    @intent_handler('ask_rasa.intent')
    def handle_ask_rasa_intent(self, message):
        user_utterance = message.data.get('utterance')
        rasa_response = self.rasa_client.send_to_rasa(user_utterance)
        self.speak(rasa_response)


def create_skill():
    return RasaSkill()

