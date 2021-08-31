import sys
import logging
import cv2

logging.basicConfig(level=logging.INFO)

try:
    input_path = sys.argv[1] # 入力
    output_path = sys.argv[2] # 出力
except IndexError:
    # コマンドライン引数が足りない場合は使い方を表示して終了する
    print('Usage: python detect_faces.py INPUT_PATH OUTPUT_PATH', file=sys.stderr)
    exit(1)

# 特微量ファイルのパスを定して分類器オブジェクトを作成する
# cv2.data.haarcascadesはデータディレクトリのパス。公式のPythonバインディングには存在しない
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

image = cv2.imread(input_path)
if image is None:
    logging.error(f'Image "{input_path}" not found')

# 顔を検出
faces = classifier.detectMultiScale(image)
logging.info(f'Found {len(faces)} faces.')

# 検出された顔のリストについて反復処理をする
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), color=(255, 255, 255), thickness=2)


cv2.imwrite(output_path, image)

