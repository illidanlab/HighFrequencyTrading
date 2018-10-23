# HighFrequencyTrading
This is a repository of trading simulations using Zipline:
    https://github.com/quantopian/zipline

Jupyter Notebooks are required.
    http://jupyter.org/

After you installed Zipline, all Data are saved in:

    ZIPLINE_ROOT=~/.zipline

My Quandl API key: 

    LWERJtLX_5Yxy_a7cws5

How to Ingesting Data:
    https://www.zipline.io/bundles.html#ingesting-data

    QUANDL_API_KEY=<yourkey> zipline ingest [-b <bundle>]

How to Clean Old Data:

    # clean everything older than <date>
    $ zipline clean [-b <bundle>] --before <date>
    
    # clean everything newer than <date>
    $ zipline clean [-b <bundle>] --after <date>
    
    # keep everything in the range of [before, after] and delete the rest
    $ zipline clean [-b <bundle>] --before <date> --after <after>
    
    # clean all but the last <int> runs
    $ zipline clean [-b <bundle>] --keep-last <int>

