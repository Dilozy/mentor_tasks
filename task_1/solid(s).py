import dataclasses


@dataclasses.dataclass
class Report:
    title: str
    content: str

    def to_dict(self):
        return dataclasses.asdict(self)


class PDFProducer:
    def __init__(self, data: dict):
        self.data = data
    
    def generate_pdf(self):
        print("PDF generated")


class StorageWriter:
    def __init__(self, data: dict):
        self.data = data

    def save_to_file(self, filename):
        print(f"Saved {self.data} to {filename}")


if __name__ == "__main__":
    report = Report("new_report", "my new report")
    report_data = report.to_dict()
    pdf_producer = PDFProducer(report_data)
    pdf_producer.generate_pdf()

    data_saver = StorageWriter(report_data)
    data_saver.save_to_file("New Report")
