import xml.etree.ElementTree as ET;

class XMLReader:
    CUBE_TAG = "{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube";

    CURRENCIES: dict[str, str];

    def __init__(self) -> None:
        pass;

    def read(self, file_path="currencies.xml") -> dict[str, str]:
        root = ET.parse(file_path).getroot();

        self.CURRENCIES = {"EUR": "1"}
        self.CURRENCIES.update({cube.attrib["currency"]: cube.attrib["rate"] for cube in root.iter(self.CUBE_TAG) if "currency" in cube.attrib and "rate" in cube.attrib});

        return self.CURRENCIES;