import re

from pygments.lexer import RegexLexer, include, bygroups, using, \
    this, inherit, default, words
from pygments.util import get_bool_opt
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace


class CarbonLexer(RegexLexer):
    """
    For Boo source code.
    """

    name = 'Carbon'
    url = 'https://github.com/carbon-language/carbon-lang'
    aliases = ['carbon']
    filenames = ['*.carbon']
    mimetypes = ['text/x-carbon']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'(#|//).*$', Comment.Single),
            (r'/[*]', Comment.Multiline, 'comment'),
            (r'[]{}:(),.;[]', Punctuation),
            (r'(\\)(\n)', bygroups(Text, Whitespace)),
            (r'\\', Text),
            (r'(in|is|and|or|not)\b', Operator.Word),
            (r'/(\\\\|\\[^\\]|[^/\\\s])/', String.Regex),
            (r'@/(\\\\|\\[^\\]|[^/\\])*/', String.Regex),
            (r'=~|!=|==|<<|>>|[-+/*%=<>&^|]', Operator),
            (r'abstract|addr|alias|and|api|as|'
             r'enum|event|final|get|interface|internal|of|override|'
             r'auto|break|case|constraint|continue|default|'
             r'else|extends|external|final|for|friend|'
             r'if|impl|import|interface|is|let|library|'
             r'match|not|observe|or|override|package|partial|private|'
             r'protected|return|returned|then|var|virtual|where|while|xor\b', Keyword),
            (r'fn(?=\s+\(.*?\))', Keyword),
            (r'(fn)(\s+)', bygroups(Keyword, Whitespace), 'funcname'),
            (r'(class)(\s+)', bygroups(Keyword, Whitespace), 'classname'),
            (r'(namespace)(\s+)', bygroups(Keyword, Whitespace), 'namespace'),
            (r'bool|i8|i16|i32|i64|i128|i256|'
             r'f16|f32|f64|f128|'
             r'String|'
             r'u8|u16|u32|u64|u128|u256\b', Keyword.Type),
            (r'"""(\\\\|\\"|.*?)"""', String.Double),
            (r'"(\\\\|\\[^\\]|[^"\\])*"', String.Double),
            (r"'(\\\\|\\[^\\]|[^'\\])*'", String.Single),
            (r'[a-zA-Z_]\w*', Name),
            (r'(\d+\.\d*|\d*\.\d+)([fF][+-]?[0-9]+)?', Number.Float),
            (r'[0-9][0-9.]*(ms?|d|h|s)', Number),
            (r'0\d+', Number.Oct),
            (r'0x[a-fA-F0-9]+', Number.Hex),
            (r'\d+L', Number.Integer.Long),
            (r'\d+', Number.Integer),
        ],
        'comment': [
            ('/[*]', Comment.Multiline, '#push'),
            ('[*]/', Comment.Multiline, '#pop'),
            ('[^/*]', Comment.Multiline),
            ('[*/]', Comment.Multiline)
        ],
        'funcname': [
            (r'[a-zA-Z_]\w*', Name.Function, '#pop')
        ],
        'classname': [
            (r'[a-zA-Z_]\w*', Name.Class, '#pop')
        ],
        'namespace': [
            (r'[a-zA-Z_][\w.]*', Name.Namespace, '#pop')
        ]
    }
