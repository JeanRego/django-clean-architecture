from ..AbstractPayPalResponse import AbstractPayPalResponse


class RefundCapturedPaymentResponse(AbstractPayPalResponse):

    def is_successful(self):
        return self._data.get('status') == 'COMPLETED'

    def is_pending(self):
        return self._data.get('status') in ['CREATED', 'SAVED', 'APPROVED', 'ACTION_REQUIRED']

    def redirect_url(self) -> str | None:
        return None
