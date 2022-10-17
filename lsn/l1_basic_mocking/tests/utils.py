from unittest import TestCase, mock
from unittest.mock import sentinel


class OOPOnlyTestCase(TestCase):
    def setUp(self) -> None:
        original_patch = mock._patch
        original_patch_object = mock.patch.object
        self.original_patch = original_patch
        self.original_patch_object = original_patch_object

        def _patch(*args, **kwargs):
            is_object = kwargs.pop("is_object", False)
            if not is_object:
                raise Exception(
                    "Using mock.patch directly is not allowed for this exercise, please use mock.patch.object instead")
            return original_patch(*args, **kwargs)

        def _object(target, attribute, new=sentinel.DEFAULT, spec=None,
                    create=False, spec_set=None, autospec=None,
                    new_callable=None, **kwargs):
            getter = lambda: target
            return _patch(
                getter, attribute, new, spec, create,
                spec_set, autospec, new_callable, kwargs, is_object=True
            )

        mock._patch = _patch
        mock.patch.object = _object
        # mock.patch = LimitedPatch()

    def doCleanups(self) -> None:
        mock._patch = self.original_patch
        mock.patch.object = self.original_patch_object
