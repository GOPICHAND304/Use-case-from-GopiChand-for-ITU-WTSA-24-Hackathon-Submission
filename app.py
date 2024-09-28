import json
import time
from datetime import datetime

class WomanSafetyXapp:
    def __init__(self):
        self.emergency_detected = False
        self.current_slice = "default"

    def process_e2_input(self, e2_message):
        message = json.loads(e2_message)
        if message['type'] == 'voice_data':
            self.process_voice_data(message['data'])
        elif message['type'] == 'ue_measurement':
            self.process_ue_measurement(message['data'])

    def process_voice_data(self, voice_data):
        emotion = self.detect_emotion(voice_data)
        if self.detect_emergency(emotion, voice_data):
            self.handle_emergency()

    def detect_emotion(self, voice_data):
        # we will Simulate emotion detection
        # In a real implementation, this use a machine learning model
        print("Detecting emotion from voice data...")
        return "distress"  # Simulated result

    def detect_emergency(self, emotion, voice_data):
        # we will Simulate emergency detection
        # In a real implementation, this would use more sophisticated logic
        emergency_keywords = ["help", "emergency", "danger"]
        return emotion == "distress" and any(keyword in voice_data.lower() for keyword in emergency_keywords)

    def handle_emergency(self):
        self.emergency_detected = True
        self.allocate_urllc_slice()
        self.prioritize_resources()
        self.alert_emergency_services()

    def allocate_urllc_slice(self):
        print(f"Allocating URLLC slice at {datetime.now().strftime('%H:%M:%S')}")
        self.current_slice = "URLLC"
        return self.generate_e2_output('slice_allocation', {
            'slice_type': 'URLLC',
            'action': 'allocate'
        })

    def prioritize_resources(self):
        print(f"Prioritizing resources for emergency UE at {datetime.now().strftime('%H:%M:%S')}")
        return self.generate_e2_output('resource_prioritization', {
            'ue_id': 'emergency_ue',
            'priority': 'high'
        })

    def alert_emergency_services(self):
        print(f"Alerting emergency services with location data at {datetime.now().strftime('%H:%M:%S')}")
        # In a real implementation, this would interface with emergency services systems

    def process_ue_measurement(self, measurement_data):
        print(f"Processing UE measurement: {measurement_data}")
        
        if self.emergency_detected and measurement_data['rsrp'] < -100:
            self.prioritize_resources()  # Re-prioritize if signal strength is low

    def generate_e2_output(self, message_type, data):
        return json.dumps({
            'type': message_type,
            'data': data,
            'timestamp': datetime.now().isoformat()
        })

# Example usage
xapp = WomanSafetyXapp()

# Simulate E2 input (voice data)
e2_input_voice = json.dumps({
    'type': 'voice_data',
    'data': 'Help! I need emergency assistance!',
    'timestamp': datetime.now().isoformat()
})
xapp.process_e2_input(e2_input_voice)

# Simulate E2 input (UE measurement)
e2_input_measurement = json.dumps({
    'type': 'ue_measurement',
    'data': {
        'ue_id': 'emergency_ue',
        'rsrp': -95,
        'rsrq': -12
    },
    'timestamp': datetime.now().isoformat()
})
xapp.process_e2_input(e2_input_measurement)
