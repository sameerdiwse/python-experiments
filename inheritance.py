class mobile_phone:
    def __init__(self, ScreenType, NetworkType, dual_sim, front_camera, rear_camera, RAM, Storage):
        self.screen_type = ScreenType
        self.network_type = NetworkType
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.RAM = RAM
        self.storage = Storage

    def get_camera(self):
        return self.front_camera

class samsung_mobile(mobile_phone):
    def __init__(self, ScreenType, NetworkType, dual_sim, front_camera, rear_camera, RAM, Storage):
        mobile_phone.__init__(self, ScreenType, NetworkType, dual_sim, front_camera, rear_camera, RAM, Storage)





class apple_mobile(mobile_phone):
    pass


samsung = samsung_mobile('touch', '4g', 'yes-dual', '32MP', '64MP', '33GB', '122GB External')
apple = apple_mobile('retina', '5g', 'no-dual', '20MP', '48MP', '64GB', '256GB Internal')

print(f'{samsung.get_camera()} samsung camera')
