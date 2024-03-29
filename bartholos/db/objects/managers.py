from bartholos.db.autoproxy.managers import AutoProxyManager, AutoProxyObjectManager


class ObjectDBManager(AutoProxyObjectManager):
    pass


class ObjectManager(ObjectDBManager, AutoProxyManager):
    pass


class ZoneDBManager(AutoProxyObjectManager):
    pass


class ZoneManager(ZoneDBManager, AutoProxyManager):
    pass
