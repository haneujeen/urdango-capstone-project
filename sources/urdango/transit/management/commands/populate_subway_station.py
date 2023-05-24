from django.core.management.base import BaseCommand
from transit.models import SubwayStation
import requests

from transit.models import SubwayLine


class Command(BaseCommand):
    help = 'Populate SubwayStation model with data from the Seoul subway API'

    def handle(self, *args, **options):
        API_URL = "http://openapi.seoul.go.kr:8088/6b644e596768616e3131334147767a72/json/SearchSTNBySubwayLineInfo/1/2"
        response = requests.get(API_URL)

        if response.status_code == 200:
            data = response.json()
            list_total_count = int(data['SearchSTNBySubwayLineInfo']['list_total_count'])

            API_URL = f"http://openapi.seoul.go.kr:8088/6b644e596768616e3131334147767a72/json/SearchSTNBySubwayLineInfo/1/{list_total_count}"
            response = requests.get(API_URL)

            if response.status_code == 200:
                data = response.json()
                stations = data['SearchSTNBySubwayLineInfo']['row']
                print("Total count:", list_total_count)

                for subway in data['SearchSTNBySubwayLineInfo']['row']:
                    name = subway['STATION_NM']
                    name_eng = subway.get('STATION_NM_ENG', None)  # get English name if it exists
                    line = subway['LINE_NUM']
                    # location = Point(float(subway['XPOINT_WGS']), float(subway['YPOINT_WGS']))

                    SubwayStation.objects.get_or_create(
                        code=subway['STATION_CD'],
                        name=name,
                        name_eng=name_eng,  # use English name when creating SubwayStation
                        line=SubwayLine.objects.get_or_create(name=line)[0],
                        # location=location,
                    )

            else:
                self.stderr.write('Failed to fetch data from Seoul subway API')

        else:
            self.stderr.write('Failed to fetch total count from Seoul subway API')
