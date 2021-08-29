#!/Users/insightshiga/.pyenv/shims/python

from datetime import datetime
import matplotlib
import pandas as pd
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'MigMix 1P'
import matplotlib.pyplot as plt


def main():
    #為替データの読み込み
    df_exchange = pd.read_csv(
                                  'exchange.csv',
                                  encoding    = 'cp932',
                                  header      = 1,
                                  names       = ['date', 'USD', 'rate'],
                                  index_col   = 0,
                                  parse_dates = True
                             )
    #国債金利データの読み込み
    df_jgbcm = pd.read_csv(
                              'jgbcm_all.csv',
                              encoding   = 'cp932',
                              header      = 1,
                              index_col   = 0,
                              parse_dates = True,
                              date_parser = parse_japanese_date,
                              na_values   = ['-']
                          )
    # 有効求人倍率データの読み込み
    df_jobs = pd.read_excel(
                               '第3表.xls',
                               skiprows   = 3,
                               skipfooter = 3,
                               usecols    = 'W,Y:AJ',
                               index_col  = 0
                           )

    df_jobs.columns = [c.split('.')[0] for c in df_jobs.columns]
    s_jobs          = df_jobs.stack()
    s_jobs.index    = [parse_year_and_month(y, m) for y, m in s_jobs.index]
    min_date        = datetime(1973, 1, 1)
    max_date        = datetime.now()

    # 為替
    plt.subplot(3, 1, 1)
    plt.plot(
                df_exchange.index,
                df_exchange.USD,
                label='ドル・円'
            )
    plt.xlim(min_date, max_date)
    plt.ylim(50, 250)
    plt.legend(loc='best')

    # 国際金利
    plt.subplot(3, 1, 2)
    plt.plot(df_jgbcm.index, df_jgbcm['1年'], label='1年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['5年'], label='5年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['10年'], label='10年国債金利')
    plt.xlim(min_date, max_date)
    plt.legend(loc='best')

    # 有効求人倍率
    plt.subplot(3, 1, 3)
    plt.plot(s_jobs.index, s_jobs, label='有効求人倍率(季節調整値)')
    plt.xlim(min_date, max_date)
    plt.ylim(0.0, 2.0)
    plt.axhline(y=1, color='gray')
    plt.legend(loc='best')
    plt.savefig('historical_data.png', dpi=300)


def parse_japanese_date(s:str)-> datetime:
    """
    和暦をdatetimeに変換
    """
    base_years = {
                    'S': 1925,
                    'H': 1988,
                    'R': 2018
                 }
    era = s[0]
    year, month, day = s[1:].split('.')
    year = base_years[era] + int(year)
    return datetime(year, int(month), int(day))


def parse_year_and_month(year: str, month: str) -> datetime:
    """
    (X年 Y月)の組をdatetimeオブジェクトに変換する
    """
    year = int(year[:-1])
    month = int(month[:-1])
    year += (1900 if year >= 63 else 2000)
    return datetime(year, month, 1)

if __name__ == '__main__':
    main()
