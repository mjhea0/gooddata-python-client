from gooddataclient.dataset import Dataset
from gooddataclient.columns import ConnectionPoint, Fact, Date, Attribute, Label
import os

class Quotes(Dataset):

    #ids = ConnectionPoint(title='ids')
    ids = Attribute(title='ids', folder='QuotesA')
    company = Label(title='company', folder='QuotesA', reference='symbol')
    symbol = Attribute(title='symbol', folder='QuotesA')
    sector = Attribute(title='sector', folder='QuotesA')
    industry = Attribute(title='industry', folder='QuotesA')
    market = Attribute(title='market', folder='QuotesA')
    #date = Date(title='Date', datetime=True, format='yyyy-MM-dd', folder='QuotesD', schemaReference='QuotesSR')
    date = Fact(title='date', folder='QuotesF')
    openprice = Fact(title='openprice', folder='QuotesF')
    highprice = Fact(title='highprice', folder='QuotesF')
    lowprice = Fact(title='lowprice', folder='QuotesF')
    closeprice = Fact(title='closeprice', folder='QuotesF')
    volume = Fact(title='volume', dataType='INT', folder='QuotesF')
    adjustedcloseprice = Fact(title='adjustedcloseprice', folder='QuotesF')

    class Meta(Dataset.Meta):
        column_order = ('company', 'symbol', 'sector', 'industry', 'market', 'date', 'ids', 'openprice', 'highprice', 'lowprice', 'closeprice', 'volume', 'adjustedcloseprice')
        schema_name = 'quotes'

    def data(self):
        csv_data = open(os.path.join(os.path.dirname(__file__), os.pardir, 'csv_data', 'quotes.csv')).read()
        return csv_data

