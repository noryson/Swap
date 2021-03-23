class Session:
    _expired: bool = None

    def expire(self) -> None:
        self._expired = True

    def revalidate(self) -> None:
        self._expired = False