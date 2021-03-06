# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import io
import json
import subprocess
from goodtables import datatable
from goodtables import exceptions
from goodtables import compat
from tests import base


class TestDataTable(base.BaseTestCase):

    def setUp(self):
        super(TestDataTable, self).setUp()

    def tearDown(self):
        super(TestDataTable, self).tearDown()

    def test_404_raises(self):

        data_source = 'https://okfn.org/this-url-cant-possibly-exist-so-lets-test-404/'

        self.assertRaises(exceptions.DataSourceHTTPError,
                          datatable.DataTable, data_source)

    def test_html_raises(self):

        data_source = 'https://www.google.com/'

        self.assertRaises(exceptions.DataSourceIsHTMLError,
                          datatable.DataTable, data_source)


    def test_excel_from_file(self):

        data_source =  os.path.join(self.data_dir, 'hmt', 'BIS_monthly_spend_December_2012.xls')
        data = datatable.DataTable(data_source, format='excel')

        self.assertTrue(data.headers)

    def test_excel_from_url(self):

        data_source = 'https://github.com/okfn/goodtables/raw/master/examples/hmt/BIS_monthly_spend_December_2012.xls'
        data = datatable.DataTable(data_source, format='excel')

        self.assertTrue(data.headers)

    def test_wrong_encoding_raises(self):

        data_source = os.path.join(self.data_dir, 'hmt','BIS_spending_over__25_000_July_2014.csv')
        encoding = 'UTF-8'  # should be 'ISO-8859-2'

        self.assertRaises(exceptions.DataSourceDecodeError, datatable.DataTable,
                          data_source, encoding=encoding)
