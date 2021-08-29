#!/Users/insightshiga/.pyenv/shims/python

import sys
from typing import List
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox, LTComponent
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def main():
    """
    コマンドライン引数で指定したPDFファイルからテキストボックスを抽出して中身を表示する
    """
    laparams = LAParams(detect_vertical=True)
    resource_manager = PDFResourceManager()
    # ページを集めるPageAggregaterを生成
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(sys.argv[1], 'rb') as f:
        #PDFPage.get_pagesにファイルを部ジェクトを指定して、PDFPオブジェクトを取得
        for page in PDFPage.get_pages(f):
            interpreter.process_page(page)
            layout = device.get_result()

            # テキストボックスのリストを取得
            boxes = find_textboxes_recursively(layout)
            # 座標の順番でソート
            boxes.sort(key=lambda b: (-b.y1, b.x0))

            for box in boxes:
                print('-' * 10)
                print(box.get_text().strip())


def find_textboxes_recursively(component: LTComponent) -> List[LTTextBox]:
    """
    再帰的にテキストボックスを探してリストを取得する
    """

    if isinstance(component, LTTextBox):
        return [component]

    if isinstance(component, LTContainer):
        boxes = []
        for child in component:
            boxes.extend(find_textboxes_recursively(child))

        return boxes

    return []

if __name__ == '__main__':
    main()
