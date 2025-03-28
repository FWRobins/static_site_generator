class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        dict_string = ""
        for key, value in self.props.items():
            dict_string += f' {key}="{value}"'
        return dict_string
    
    def __eq__(self, other):
        if (self.tag == other.tag
        and self.value == other.value
        and self.children == other.children
        and self.props == other.props):
            return True
        return False
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()}"

