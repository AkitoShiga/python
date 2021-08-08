class Rule:
    """[summary]
    すべてのルールの基底クラス
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    """[summary]
    見出しとは最長70文字で、最終文字が :,.,。のどれでもない単一の行
    """
    type = 'heading'
    def condition(self, block):
        return (
            not '\n' in block
            and len(block) <= 70
            and not (block[-1]) == ':'
            or block[-1] == '.'
            or block[-1] == '='
        )

class TitleRule(HeadingRule):
    """
    表題とは文書の最初のブロックで、かつ見出しであるもの
    """
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
    """
    リスト項目とは - で始まるパラグラフ。
    書式付の一環として、この - は削除する。
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    """
    リストは、リスト項目ではないブロックとリスト項目の間から始まり、
    連続したリスト項目の最後のものが終わるところまで
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    """[summary]
    どこのルールにも当てはまらないブロック
    """
    type = 'paragraph'
    def condition(self, block):
        return True