from data_service import CovidDataService
from exporter import TypeExporter

covid_data_service = CovidDataService()

countries = covid_data_service.get_countries_data(['chile', 'peru'])

type_exporter = TypeExporter()

type_exporter.generateType(countries)

countries = covid_data_service.get_countries_historic_data(['chile', 'peru'], '2021-01-01', '2021-02-01')

type_exporter.generateType(countries)