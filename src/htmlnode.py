class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            prop_str = ""
            for key, value in self.props:
                prop_str += f' {key}="{value}"'
            return prop_str
        return None

    def __repr__(self) -> str:
        pass
