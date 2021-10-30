from poium import Page, Element

class GooglePage(Page):
    """Google Page 元素"""
    Search_bar = Element(name='q', timeout=5, describe="搜尋欄")
    Search_button = Element(name='btnK', timeout=5, describe="搜尋按钮")