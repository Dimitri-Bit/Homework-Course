class TV:
    def __init__(self, channel_number=0, channel_name="", channel_list=list(), sound=0):
        self.channel_number = channel_number
        self.channel_name = channel_name
        self.channel_list = channel_list
        self.sound = sound

    def get_channel_number(self):
        return self.channel_number
    
    def set_channel_number(self, number):
        if number > 0 and number <= len(self.channel_list):
            self.channel_number = number
        else:
            print(f"Invalid channel number \"{number}\"")

    def get_channel_name(self):
        return self.channel_name
    
    def set_channel_name(self, name):
        self.channel_name = name

    def get_channel_list(self):
        return self.channel_list
    
    def set_channel_list(self, list):
        self.channel_list = list

    def get_sound(self):
        return self.sound
    
    def set_sound(self, sound):
        if sound >= 0 and sound <= 10:
            self.sound = sound
        else:
            print("Invalid sound input")

    def add_channel(self, channel_name):
        self.channel_list.append(channel_name)

    def delete_channel(self, channel_name):
        self.channel_list.remove(channel_name)

    def raise_sound(self):
        if self.sound < 10:
            self.sound += 1
        else:
            print("Sound is already at max")

    def channel_name(self, index):
        if index >= 0 and index < len(self.channel_list):
            return self.channel_list[index]

TV = TV()
TV.add_channel("test")
TV.add_channel("test2")
print(TV.get_channel_list())
TV.delete_channel("test2")
print(TV.get_channel_list())