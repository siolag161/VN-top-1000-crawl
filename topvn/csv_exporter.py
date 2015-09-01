
'''customize the output csv file's column order'''

from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class TopVNCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        export_fields = settings.get('FIELDS_TO_EXPORT', [])
        if export_fields:
            kwargs['fields_to_export'] = export_fields
        super(TopVNCsvItemExporter, self).__init__(*args, **kwargs)

