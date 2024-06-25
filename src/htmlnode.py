class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children #list
        self.props = props #dict of attributes

    def to_html(self):
        raise NotImplementedError("Not overwritten by child class")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for node in self.props:
            props_string += f'{node}="{self.props[node]}" '
        return props_string.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
