from selenium import webdriver


class TrainerRoad(object):
    def __init__(self, athlete, driver=None):
        if driver == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.get(
            'https://www.trainerroad.com/career/{a}'.format(a=athlete))

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.driver.close()
        self.driver.quit()

    def ride_image_url(self, ride_name):
        images = self.driver.find_elements_by_tag_name('img')
        for image in images:
            if image.get_attribute('alt') == ride_name:
                return image.get_attribute('src')
        return None
