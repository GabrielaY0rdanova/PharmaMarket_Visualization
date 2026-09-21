from pathlib import Path
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "PharmaMarket_Visualization.twbx"


def workbook_xml() -> str:
    with zipfile.ZipFile(WORKBOOK) as archive:
        twb_names = [name for name in archive.namelist() if name.lower().endswith(".twb")]
        if len(twb_names) != 1:
            raise AssertionError(f"Expected one .twb file, found {twb_names}")
        return archive.read(twb_names[0]).decode("utf-8")


class WorkbookContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml = workbook_xml()

    def test_packaged_workbook_contains_extract(self):
        with zipfile.ZipFile(WORKBOOK) as archive:
            self.assertTrue(any(name.lower().endswith(".hyper") for name in archive.namelist()))

    def test_story_and_dashboards_exist(self):
        self.assertIn("dashboard name='PharmaMarket Analysis'", self.xml)
        self.assertIn("class='dashboard' hidden='true' name='Market Structure Overview'", self.xml)
        self.assertIn("class='dashboard' hidden='true' name='Pricing &amp; Market Competition'", self.xml)

    def test_package_price_chart_uses_accurate_labels(self):
        self.assertIn("Package Price Segmentation", self.xml)
        self.assertIn("Number of Package Options", self.xml)
        self.assertNotIn("Number of Medicines", self.xml)

    def test_expected_calculated_fields_exist(self):
        captions = (
            "Brands Per Generic",
            "Competition Level",
            "Competition %",
            "Medicines Per Manufacturer",
            "Portfolio Size",
            "Portfolio Size %",
            "Price Segment",
            "Price Segment %",
        )
        for caption in captions:
            self.assertIn(f"caption='{caption}'", self.xml)

    def test_expected_relationship_tables_exist(self):
        tables = (
            "medicine",
            "generic",
            "drug_class",
            "manufacturer",
            "dosage_form",
            "medicine_package_size",
            "medicine_package_container",
        )
        for table in tables:
            self.assertIn(f"name='{table}'", self.xml)


if __name__ == "__main__":
    unittest.main()
