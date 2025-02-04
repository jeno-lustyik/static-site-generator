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
            for key, value in self.props.items():
                prop_str += f' {key}="{value}"'
            return prop_str
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return f'{self.value}'

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("ParentNodes must have child nodes.")
        children_value = ""
        for child in self.children:
            children_value += child.to_html()

        return f"<{self.tag}>{children_value}</{self.tag}>"
