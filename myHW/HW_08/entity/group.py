from base import Base

class Group(Base):
    def __init__(self, id = 0, group_nm = None, members = None):
        super(Group,self).__init__()
        self.group_nm = group_nm
        self.members = members
    def __str__(self):
        return "id:{} name:{} {}".format(self.id,self.group_nm, self.members)
    def __unicode__(self):
        return unicode("{} {}".format(self.id,self.group_nm))
    def to_unicode(self):
        return self.__unicode__()
