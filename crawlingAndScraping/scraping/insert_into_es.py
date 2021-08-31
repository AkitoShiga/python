import sys
import hashlib
import json
import logging
from elasticsearch import Elasticsearch

def main():
    """
    メインとなる処理
    """
    # Elasticsearchのクライアントを作成する
    # 第一引数でノードのリストを指定できる。デフォルトではlocalhostの9200ポートに接続するため省略可能
    es = Elasticsearch(['localhost:9200'])
    create_pages_index(es)

    for line in sys.stdin:
        page = json.loads(line) # 読み込んだ行をJSONとしてパース
        # ドキュメントIDとしてURLのSHA-1ダイジェストを使用
        doc_id = hashlib.sha1(page['url'].encode('utf-8')).hexdigest()
        # pageインデックスにインデックス化する
        es.index(index='pages', doc_type='_doc', id=doc_id, body=page)


def crate_pages_index(es: Elasticsearch):
    """
    ElasticsearchにPageインデックスを作成する
    """
    # キーワード引数bodyでJSONに相当するdictを作成する
    # ignore=400はインデックスが存在する場合でもエラーに市内という意味
    es.indices.create(index='pages', ignore=400, body={
        # settingsという項目でkuromoji_analyzerというアナライザーを定義する
        # アナライザーは転置インデックスの作成方法を指定するもの
        "settings": {
            "analysys": {
                "analyzer": {
                }
            }
        }
        })
