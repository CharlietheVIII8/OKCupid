import requests


class Photo:
    GENERATED_PHOTOS_API_KEY = 'h839ZfTUYsDmet4_iY6Adg'

    def __init__(self, gender, age):
        parameters = {
            'emotion': 'joy',
            'gender': 'male' if gender == 'Man' else 'female',
            'age': 'young-adult' if age <= 23 else 'adult',
            'per_page': 1
        }
        response = requests.get(
            'https://api.generated.photos/api/v1/faces?api_key={}'.format(self.GENERATED_PHOTOS_API_KEY),
            params=parameters)
        output = response.json()
        self.photo = output['faces']['urls'][4]['512']
        r = requests.get(self.photo)
        open('photos/'.format(self.photo), 'wb').write(r.content)
        self.confidence = output['faces']['meta']['confidence'][0]
        self.age = output['faces']['meta']['age'][0]
        self.ethnicity = output['faces']['meta']['ethnicity'][0]
        self.eye_color = output['faces']['meta']['eye_color'][0]
        self.hair_color = output['faces']['meta']['hair_color'][0]
        self.hair_length = output['faces']['meta']['hair_length'][0]
        self.emotion = output['faces']['meta']['emotion'][0]
