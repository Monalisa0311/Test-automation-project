class DeviceSimulator:
    def get_video_resolution(self):
        return "1920x1080"

    def get_video_fps(self):
        return 58

    def get_dropped_frames(self):
        return 3

    def get_playback_status(self):
        return "PLAYING"

    def get_audio_video_sync(self):
        return 35
    
    def is_app_crashed(self):
        return False

    def is_app_responsive(self):
        return True
    
    def get_cpu_usage(self):
        return 75

    def get_memory_usage(self):
        return 450

    def get_battery_level(self):
        return 65

    def get_device_temperature(self):
        return 42

    def connect_device(self, connected=True):

        if not connected:
            raise ConnectionError("Device is not connected")

        return "Device connected successfully"