from django.contrib.auth.models import User

from profiles.models import Profile, NotificationFilter
from profiles.models.user_role_binding import UserRoleBinding
from tests.test_profile.base_test_profile import BaseTestProfile


class TestUserRoleBinding(BaseTestProfile):

    def setUp(self):
        super(TestProfile, self).setUp()
        role = Role.objects.create()
        user_role_binding = UserRoleBinding.objects.create(
            role=role,
            user=self.superuser,
            content_type=Request,
            object_id=self.test_request.id,
        )

    def test_delete_object_in_binding():
