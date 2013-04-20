class NoSuchJobError(Exception):
    pass


class InvalidJobOperationError(Exception):
    pass


class NoQueueError(Exception):
    pass


class InvalidQueueName(Exception):
    pass


class MulipleQueueConnectionsError(Exception):
    pass


class UnpickleError(Exception):
    def __init__(self, message, raw_data, inner_exception=None):
        super(UnpickleError, self).__init__(message, inner_exception)
        self.raw_data = raw_data


class DequeueTimeout(Exception):
    pass


class StopRequested(Exception):
    pass


class InvalidBetween(Exception):
    pass


class InvalidInterval(Exception):
    pass

class InvalidWeekdays(Exception):
    pass

