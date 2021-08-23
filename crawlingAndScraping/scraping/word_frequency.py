import sys
import logging
from collections import Counter
from pathlib import Path
from typing import List, Iterator, TextIO

import MeCab

tagger = MeCab.Tagger('')
tagger.parse('')


def main():
    """
    コマンドライン引数で指定したディレクトリ内のファイルを読み込んで、頻出単語を表示する
    """

    input_dir = Path(sys.argv[1])

    # dict
    frequency = Counter()

    # 戻り値はテキストファイル
    for path in sorted(input_dir.glob('*/wiki_*')):
        logging.info(f'Processing{path}...')

        with open(path) as file:
            # frequency 同士を足すとマージしたことになるらしい
            frequency += count_words(file)

    for word, count in frequency.most_common(30):
        print(word, count)


def count_words(file: TextIO) -> Counter:
    """
    WikiExtractorが出力したファイルに含まれるすべての記事から単語の出現回数を数える
    """

    frequency = Counter()
    # ログの出力用
    num_docs = 0

    # ファイルをテキストの配列にしてる
    for content in iter_doc_contents(file):

        words = get_words(content)

        # ここで登録してる
        # 多分ここで名詞と出現回数のdictを登録してる
        frequency.update(words)
        num_docs += 1

    logging.info(f'Found{len(frequency)} words from {num_docs} documents')
    print(frequency)
    return frequency


def iter_doc_contents(file: TextIO) -> Iterator[str]:
    """
    ファイルオブジェクトを読み込んで記事の中身（docタグ内のテキスト）を
    純に返すジェネレーター関数
    """

    # ファイルのすべての列を順番に処理
    for line in file:
        if line.startswith('<doc '):
            buffer = []
        elif line.startswith('</doc>'):
            content = ''.join(buffer)
            yield content
        else:
            buffer.append(line)


# ここで めかぶを使うのかな？
def get_words(content: str) -> List[str]:
    """
    文字列内に出現する名刺のリストを取得する関数
    """

    words = []
    node = tagger.parseToNode(content)

    while node:

        pos, pos_sub1 = node.feature.split(',')[:2]

        if pos == '名詞' and pos_sub1 in ('固有名詞', '一般'):
            words.append(node.surface)
        node = node.next

    return words


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
