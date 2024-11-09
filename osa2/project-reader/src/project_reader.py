from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        try:
            toml_data = toml.loads(content)
        except toml.TomlDecodeError as e:
            print(f"Error decoding TOML content: {e}")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        data = toml_data.get('tool', {}).get('poetry', {})
        
        return Project(data.get('name', 'Default name'), data.get('description', 'Default description'), data.get('group', {}).get('dev', {}).get('dependencies', {}), data.get('group', {}).get('dev', {}).get('dependencies', {}), data.get('authors', {}), data.get('license', ''))

