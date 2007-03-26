#!/usr/bin/python
#
# Copyright (C) 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__author__ = 'api.laurabeth@gmail.com (Laura Beth Lincoln)'


import unittest
from elementtree import ElementTree
import gdata
import gspreadsheet

SPREADSHEETS_FEED = """<feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
    xmlns:gs="http://schemas.google.com/spreadsheets/2006">
  <id>http://spreadsheets.google.com/feeds/spreadsheets/private/full</id>
  <updated>2006-11-17T18:23:45.173Z</updated>
  <title type="text">Available Spreadsheets</title>
  <link rel="alternate" type="text/html"
    href="http://spreadsheets.google.com/ccc?key=key"/>
  <link rel="http://schemas.google.com/g/2005#feed"
    type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/worksheets/key/private/full"/>
  <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/worksheets/key/private/full"/>
  <author>
    <name>Fitzwilliam Darcy</name>
    <email>fitz@gmail.com</email>
  </author>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>1</openSearch:itemsPerPage>
  <entry>
    <id>http://spreadsheets.google.com/feeds/spreadsheets/private/full/key</id>
    <updated>2006-11-17T18:24:18.231Z</updated>
    <title type="text">Groceries R Us</title>
    <content type="text">Groceries R Us</content>
    <link rel="http://schemas.google.com/spreadsheets/2006#worksheetsfeed"
      type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/worksheets/key/private/full"/>
    <link rel="alternate" type="text/html"
      href="http://spreadsheets.google.com/ccc?key=key"/>
    <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/spreadsheets/private/full/key"/>
    <author>
      <name>Fitzwilliam Darcy</name>
      <email>fitz@gmail.com</email>
    </author>
  </entry>
</feed>
"""

WORKSHEETS_FEED = """<feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
    xmlns:gs="http://schemas.google.com/spreadsheets/2006">
  <id>http://spreadsheets.google.com/feeds/worksheets/key/private/full</id>
  <updated>2006-11-17T18:23:45.173Z</updated>
  <title type="text">Groceries R Us</title>
  <link rel="alternate" type="text/html"
    href="http://spreadsheets.google.com/ccc?key=key"/>
  <link rel="http://schemas.google.com/g/2005#feed"
    type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/worksheets/key/private/full"/>
  <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/worksheets/key/private/full"/>
  <author>
    <name>Fitzwilliam Darcy</name>
    <email>fitz@gmail.com</email>
  </author>
  <openSearch:totalResults>1</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>1</openSearch:itemsPerPage>
  <entry>
    <id>http://spreadsheets.google.com/feeds/worksheets/key/private/full/od6</id>
    <updated>2006-11-17T18:23:45.173Z</updated>
    <title type="text">Sheet1</title>
    <content type="text">Sheet1</content>
    <link rel="http://schemas.google.com/spreadsheets/2006#listfeed"
      type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/list/key/od6/private/full"/>
    <link rel="http://schemas.google.com/spreadsheets/2006#cellsfeed"
      type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full"/>
    <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/worksheets/key/private/full/od6"/>
    <gs:rowCount>100</gs:rowCount>
    <gs:colCount>20</gs:colCount>
  </entry>
</feed>
"""

CELLS_FEED = """<feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
    xmlns:gs="http://schemas.google.com/spreadsheets/2006">
  <id>http://spreadsheets.google.com/feeds/cells/key/od6/private/full</id>
  <updated>2006-11-17T18:27:32.543Z</updated>
  <title type="text">Sheet1</title>
  <link rel="alternate" type="text/html"
    href="http://spreadsheets.google.com/ccc?key=key"/>
  <link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full"/>
  <link rel="http://schemas.google.com/g/2005#post" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full"/>
  <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full"/>
  <author>
    <name>Fitzwilliam Darcy</name>
    <email>fitz@gmail.com</email>
  </author>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>1</openSearch:itemsPerPage>
  <gs:rowCount>100</gs:rowCount>
  <gs:colCount>20</gs:colCount>
  <entry>
    <id>http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C1</id>
    <updated>2006-11-17T18:27:32.543Z</updated>
    <category scheme="http://schemas.google.com/spreadsheets/2006"
      term="http://schemas.google.com/spreadsheets/2006#cell"/>
    <title type="text">A1</title>
    <content type="text">Name</content>
    <link rel="self" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C1"/>
    <link rel="edit" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C1/bgvjf"/>
    <gs:cell row="1" col="1" inputValue="Name">Name</gs:cell>
  </entry>
  <entry>
    <id>http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C2</id>
    <updated>2006-11-17T18:27:32.543Z</updated>
    <category scheme="http://schemas.google.com/spreadsheets/2006"
      term="http://schemas.google.com/spreadsheets/2006#cell"/>
    <title type="text">B1</title>
    <content type="text">Hours</content>
    <link rel="self" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C2"/>
    <link rel="edit" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/cells/key/od6/private/full/R1C2/1pn567"/>
    <gs:cell row="1" col="2" inputValue="Hours">Hours</gs:cell>
  </entry>
</feed>
"""

LIST_FEED = """<feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
    xmlns:gsx="http://schemas.google.com/spreadsheets/2006/extended">
  <id>http://spreadsheets.google.com/feeds/list/key/od6/private/full</id>
  <updated>2006-11-17T18:23:45.173Z</updated>
  <title type="text">Sheet1</title>
  <link rel="alternate" type="text/html"
    href="http://spreadsheets.google.com/ccc?key=key"/>
  <link rel="http://schemas.google.com/g/2005#feed"
    type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/list/key/od6/private/full"/>
  <link rel="http://schemas.google.com/g/2005#post"
    type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/list/key/od6/private/full"/>
  <link rel="self" type="application/atom+xml"
    href="http://spreadsheets.google.com/feeds/list/key/od6/private/full"/>
  <author>
    <name>Fitzwilliam Darcy</name>
    <email>fitz@gmail.com</email>
  </author>
  <openSearch:totalResults>2</openSearch:totalResults>
  <openSearch:startIndex>1</openSearch:startIndex>
  <openSearch:itemsPerPage>2</openSearch:itemsPerPage>
  <entry>
    <id>http://spreadsheets.google.com/feeds/list/key/od6/private/full/cokwr</id>
    <updated>2006-11-17T18:23:45.173Z</updated>
    <category scheme="http://schemas.google.com/spreadsheets/2006"
      term="http://schemas.google.com/spreadsheets/2006#list"/>
    <title type="text">Bingley</title>
    <content type="text">Hours: 10, Items: 2, IPM: 0.0033</content>
    <link rel="self" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/list/key/od6/private/full/cokwr"/>
    <link rel="edit" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/list/key/od6/private/full/cokwr/2ehkc2oh7d"/>
    <gsx:name>Bingley</gsx:name>
    <gsx:hours>10</gsx:hours>
    <gsx:items>2</gsx:items>
    <gsx:ipm>0.0033</gsx:ipm>
  </entry>
  <entry>
    <id>http://spreadsheets.google.com/feeds/list/key/od6/private/full/cyevm</id>
    <updated>2006-11-17T18:23:45.173Z</updated>
    <category scheme="http://schemas.google.com/spreadsheets/2006"
      term="http://schemas.google.com/spreadsheets/2006#list"/>
    <title type="text">Charlotte</title>
    <content type="text">Hours: 60, Items: 18000, IPM: 5</content>
    <link rel="self" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/list/key/od6/private/full/cyevm"/>
    <link rel="edit" type="application/atom+xml"
      href="http://spreadsheets.google.com/feeds/list/key/od6/private/full/cyevm/64rl27px3zyn"/>
    <gsx:name>Charlotte</gsx:name>
    <gsx:hours>60</gsx:hours>
    <gsx:items>18000</gsx:items>
    <gsx:ipm>5</gsx:ipm>
  </entry>
</feed>

"""
class ColCountTest(unittest.TestCase):
  
  def setUp(self):
    self.col_count = gspreadsheet.ColCount()
    
  def testToAndFromString(self):
    self.col_count.text = '20'
    self.assert_(self.col_count.text == '20')
    new_col_count = gspreadsheet.ColCountFromString(self.col_count.ToString())
    self.assert_(self.col_count.text == new_col_count.text)


class RowCountTest(unittest.TestCase):
  
  def setUp(self):
    self.row_count = gspreadsheet.RowCount()
    
  def testToAndFromString(self):
    self.row_count.text = '100'
    self.assert_(self.row_count.text == '100')
    new_row_count = gspreadsheet.RowCountFromString(self.row_count.ToString())
    self.assert_(self.row_count.text == new_row_count.text)


class CellTest(unittest.TestCase):
  
  def setUp(self):
    self.cell = gspreadsheet.Cell()
    
  def testToAndFromString(self):
    self.cell.text = 'test cell'
    self.assert_(self.cell.text == 'test cell')
    self.cell.row = '1'
    self.assert_(self.cell.row == '1')
    self.cell.col = '2'
    self.assert_(self.cell.col == '2')
    self.cell.inputValue = 'test input value'
    self.assert_(self.cell.inputValue == 'test input value')
    self.cell.numericValue = 'test numeric value'
    self.assert_(self.cell.numericValue == 'test numeric value')
    new_cell = gspreadsheet.CellFromString(self.cell.ToString())
    self.assert_(self.cell.text == new_cell.text)
    self.assert_(self.cell.row == new_cell.row)
    self.assert_(self.cell.col == new_cell.col)
    self.assert_(self.cell.inputValue == new_cell.inputValue)
    self.assert_(self.cell.numericValue == new_cell.numericValue)
    

class CustomTest(unittest.TestCase):

  def setUp(self):
    self.custom = gspreadsheet.Custom()
    
  def testToAndFromString(self):
    self.custom.text = 'value'
    self.custom.column = 'column_name'
    self.assert_(self.custom.text == 'value')
    self.assert_(self.custom.column == 'column_name')
    new_custom = gspreadsheet.CustomFromString(self.custom.ToString())
    self.assert_(self.custom.text == new_custom.text)
    self.assert_(self.custom.column == new_custom.column)
    

class SpreadsheetsWorksheetTest(unittest.TestCase):

  def setUp(self):
    self.worksheet = gspreadsheet.SpreadsheetsWorksheet()
    
  def testToAndFromString(self):
    self.worksheet.row_count = gspreadsheet.RowCount(text='100')
    self.assert_(self.worksheet.row_count.text == '100')
    self.worksheet.col_count = gspreadsheet.ColCount(text='20')
    self.assert_(self.worksheet.col_count.text == '20')
    new_worksheet = gspreadsheet.SpreadsheetsWorksheetFromString(
        self.worksheet.ToString())
    self.assert_(self.worksheet.row_count.text == new_worksheet.row_count.text)
    self.assert_(self.worksheet.col_count.text == new_worksheet.col_count.text)


class SpreadsheetsCellTest(unittest.TestCase):

  def setUp(self):
    self.entry = gspreadsheet.SpreadsheetsCell()
    
  def testToAndFromString(self):
    self.entry.cell = gspreadsheet.Cell(text='my cell', row='1', col='2', 
        inputValue='my input value', numericValue='my numeric value')
    self.assert_(self.entry.cell.text == 'my cell')
    self.assert_(self.entry.cell.row == '1')
    self.assert_(self.entry.cell.col == '2')
    self.assert_(self.entry.cell.inputValue == 'my input value')
    self.assert_(self.entry.cell.numericValue == 'my numeric value')
    new_cell = gspreadsheet.SpreadsheetsCellFromString(self.entry.ToString())
    self.assert_(self.entry.cell.text == new_cell.cell.text)
    self.assert_(self.entry.cell.row == new_cell.cell.row)
    self.assert_(self.entry.cell.col == new_cell.cell.col)
    self.assert_(self.entry.cell.inputValue == new_cell.cell.inputValue)
    self.assert_(self.entry.cell.numericValue == new_cell.cell.numericValue)
    
    
class SpreadsheetsListTest(unittest.TestCase):

  def setUp(self):
    self.row = gspreadsheet.SpreadsheetsList()
    
  def testToAndFromString(self):
    self.row.custom.append(gspreadsheet.Custom(column='column_1', 
        text='my first column'))
    self.row.custom.append(gspreadsheet.Custom(column='column_2', 
        text='my second column'))
    self.assert_(self.row.custom[0].column == 'column_1')
    self.assert_(self.row.custom[0].text == 'my first column')
    self.assert_(self.row.custom[1].column == 'column_2')
    self.assert_(self.row.custom[1].text == 'my second column')
    new_row = gspreadsheet.SpreadsheetsListFromString(self.row.ToString())
    self.assert_(self.row.custom[0].column == new_row.custom[0].column)
    self.assert_(self.row.custom[0].text == new_row.custom[0].text)
    self.assert_(self.row.custom[1].column == new_row.custom[1].column)
    self.assert_(self.row.custom[1].text == new_row.custom[1].text)
    
class SpreadsheetsSpreadsheetsFeedTest(unittest.TestCase):

  def setUp(self):
    #self.item_feed = gspreadsheet.SpreadsheetSpreadsheetsFeed()
    self.feed = gspreadsheet.SpreadsheetsSpreadsheetsFeedFromString(
        SPREADSHEETS_FEED)

  def testToAndFromString(self):
    self.assert_(len(self.feed.entry) == 1)
    for an_entry in self.feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsSpreadsheet))
    new_feed = gspreadsheet.SpreadsheetsSpreadsheetsFeedFromString(
        str(self.feed))
    for an_entry in new_feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsSpreadsheet))
      
class SpreadsheetsWorksheetsFeedTest(unittest.TestCase):

  def setUp(self):
    #self.item_feed = gspreadsheet.SpreadsheetWorksheetsFeed()
    self.feed = gspreadsheet.SpreadsheetsWorksheetsFeedFromString(
        WORKSHEETS_FEED)

  def testToAndFromString(self):
    self.assert_(len(self.feed.entry) == 1)
    for an_entry in self.feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsWorksheet))
    new_feed = gspreadsheet.SpreadsheetsWorksheetsFeedFromString(
        str(self.feed))
    for an_entry in new_feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsWorksheet))
      
class SpreadsheetsCellsFeedTest(unittest.TestCase):

  def setUp(self):
    #self.item_feed = gspreadsheet.SpreadsheetCellsFeed()
    self.feed = gspreadsheet.SpreadsheetsCellsFeedFromString(
        CELLS_FEED)

  def testToAndFromString(self):
    self.assert_(len(self.feed.entry) == 2)
    for an_entry in self.feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsCell))
    new_feed = gspreadsheet.SpreadsheetsCellsFeedFromString(str(self.feed))
    self.assert_(isinstance(new_feed.extension_elements[0], 
        gspreadsheet.RowCount))
    self.assert_(new_feed.extension_elements[0].text == '100')
    self.assert_(isinstance(new_feed.extension_elements[1], 
        gspreadsheet.ColCount))
    self.assert_(new_feed.extension_elements[1].text == '20')
    for an_entry in new_feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsCell))
      
class SpreadsheetsListFeedTest(unittest.TestCase):

  def setUp(self):
    #self.item_feed = gspreadsheet.SpreadsheetListFeed()
    self.feed = gspreadsheet.SpreadsheetsListFeedFromString(
        LIST_FEED)

  def testToAndFromString(self):
    self.assert_(len(self.feed.entry) == 2)
    for an_entry in self.feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsList))
    new_feed = gspreadsheet.SpreadsheetsListFeedFromString(str(self.feed))
    for an_entry in new_feed.entry:
      self.assert_(isinstance(an_entry, gspreadsheet.SpreadsheetsList))
    
if __name__ == '__main__':
  unittest.main()
