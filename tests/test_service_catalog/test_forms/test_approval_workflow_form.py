from service_catalog.forms.approval_workflow_form import ApprovalWorkflowForm
from service_catalog.models import ApprovalWorkflow
from tests.test_service_catalog.base import BaseTest


class TestApprovalWorkflowForm(BaseTest):

    def setUp(self):
        super(TestApprovalWorkflowForm, self).setUp()

    def test_create_approval_workflow(self):
        data = {
            'name': 'test_approval_workflow',
            'operation': self.create_operation_test,
            'scopes': [self.test_quota_scope]
        }
        form = ApprovalWorkflowForm(data)
        self.assertTrue(form.is_valid())

    def test_clean(self):
        existing_approval = ApprovalWorkflow.objects.create(name="test",
                                                           operation=self.create_operation_test)
        existing_approval.scopes.set([self.test_quota_scope])

        data = {
            'name': 'test_approval_workflow',
            'operation': self.create_operation_test,
            'scopes': [self.test_quota_scope]
        }
        form = ApprovalWorkflowForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("has already an approval workflow", form["scopes"].errors[0])


    def test_add_scope_to_scopes(self):
        existing_approval = ApprovalWorkflow.objects.create(name="test",
                                                           operation=self.create_operation_test)
        existing_approval.scopes.set([self.test_quota_scope])

        data = {
            'name': 'test_approval_workflow',
            'operation': self.create_operation_test,
            'scopes': [self.test_quota_scope,self.test_quota_scope2]
        }
        form = ApprovalWorkflowForm(instance=existing_approval,data=data)
        self.assertTrue(form.is_valid())
