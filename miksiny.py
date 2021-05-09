# В Python так называемые миксины — это классы, которые живут в обычном дереве наследования, но они остаются небольшими, чтобы избежать создания иерархий, которые слишком сложны для понимания программистом. В частности, миксины не должны иметь общих предков, кроме объекта, с другими родительскими классами.

class ComparableMixin(object):
    """This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods."""
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self <= other and (self != other)
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other