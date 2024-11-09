class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _tee_lista(self, dependencies):
        #print(dependencies)
        return "\n".join(f"- {item}" for item in dependencies) if dependencies else "-"
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}"
            f"\n"
            f"\nAuthors: \n{self._tee_lista(self.authors)}"
            f"\n"
            f"\nDependencies: \n{self._tee_lista(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n{self._tee_lista(self.dev_dependencies)}"
        )
