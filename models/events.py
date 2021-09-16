from models.event import*

event_1 = Event("15/09/2021", "Hispanic Heritage Month", 1000, "Glasgow", "Heritage Appreciation", True)
event_2 = Event("10/09/2022", "TRNSMT", 2000, "Glasgow Green", "Festival", False)
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)