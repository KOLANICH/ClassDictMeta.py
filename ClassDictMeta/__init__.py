import typing
from collections import OrderedDict


class ClassDictMeta(type):
	cls = dict

	def __new__(cls: typing.Type["ClassDictMeta"], className: str, parents: tuple, attrs: typing.Dict[str, typing.Any], *args, **kwargs) -> dict:
		newAttrs = type(attrs)(attrs)
		return cls.cls((k, v) for k, v in newAttrs.items() if k[0] != "_")


class OrderedClassDictMeta(ClassDictMeta):
	cls = OrderedDict
