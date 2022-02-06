# std
from itertools import chain
import json
from typing import Optional

# internal
from ..mixins.log_methods import LogMethodsMixin
from ..utils.run import run_terraform
from .arg import fmt_args, ArgType


class Terraform(LogMethodsMixin):

    def __init__(
            self,
            auto_approve: bool = False,
            auto_approve_apply: bool = False,
            auto_approve_destroy: bool = False,
            var: Optional[dict] = None,
            global_call_kwargs: Optional[dict] = None,
            **global_tf_kwargs,
    ):
        self._auto_approve = auto_approve
        self._auto_approve_apply = auto_approve_apply
        self._auto_approve_destroy = auto_approve_destroy
        self._var = var if var else {}
        self._global_tf_kwargs: dict = global_tf_kwargs
        self._global_call_kwargs: dict = global_call_kwargs if global_call_kwargs else {}

    def __call__(self, *args: str, capture: bool = False, call_kwargs: dict = None):
        _call_kwargs = {**self._global_call_kwargs, **call_kwargs} if call_kwargs else {**self._global_call_kwargs}
        return run_terraform(*args, capture=capture, **_call_kwargs)

    def _run(self,
             subcommands: list[str],
             *args: ArgType,
             capture: bool = False,
             call_kwargs: Optional[dict] = None,
             **kwargs):
        _args = subcommands + fmt_args(*args, **kwargs)
        _output = self(*_args, capture=capture, call_kwargs=call_kwargs)
        if isinstance(_output, (bytes, str)):
            if capture and kwargs.get('json'):
                _output = json.loads(_output)
        return _output

    @staticmethod
    def _vars(var: Optional[dict]):
        if var is None:
            return []
        return [('var', key, val) for key, val in var.items()]

    def set_env(self, name: str, value: str):
        if 'env' not in self._global_call_kwargs:
            self._global_call_kwargs['env'] = {}
        self._global_call_kwargs['env'][name] = value

    def unset_env(self, name: str):
        if 'env' in self._global_call_kwargs:
            self._global_call_kwargs['env'].pop(name)

    def set_TF_LOG(self, value: str):
        self.set_env('TF_LOG', value)

    def unset_TF_LOG(self):
        self.unset_env('TF_LOG')

    def set_TF_LOG_PATH(self, value: str):
        self.set_env('TF_LOG_PATH', value)

    def unset_TF_LOG_PATH(self):
        self.unset_env('TF_LOG_PATH')

    def set_TF_INPUT(self, value: str):
        self.set_env('TF_INPUT', value)

    def unset_TF_INPUT(self):
        self.unset_env('TF_INPUT')

    def set_TF_VAR_(self, name: str, value: str):
        self.set_env(f'TF_VAR_{name}', value)

    def unset_TF_VAR_(self, name: str):
        self.unset_env(f'TF_VAR_{name}')

    def set_TF_CLI_ARGS(self, value: str):
        self.set_env('TF_CLI_ARGS', value)

    def unset_TF_CLI_ARGS(self):
        self.unset_env('TF_CLI_ARGS')

    def set_TF_CLI_ARGS_(self, name: str, value: str):
        self.set_env(f'TF_CLI_ARGS_{name}', value)

    def unset_TF_CLI_ARGS_(self, name: str):
        self.unset_env(f'TF_CLI_ARGS_{name}')

    def set_TF_DATA_DIR(self, value: str):
        self.set_env('TF_DATA_DIR', value)

    def unset_TF_DATA_DIR(self):
        self.unset_env('TF_DATA_DIR')

    def set_TF_WORKSPACE(self, value: str):
        self.set_env('TF_WORKSPACE', value)

    def unset_TF_WORKSPACE(self):
        self.unset_env('TF_WORKSPACE')

    def set_TF_IN_AUTOMATION(self):
        self.set_env('TF_IN_AUTOMATION', 'true')

    def unset_TF_IN_AUTOMATION(self):
        self.unset_env('TF_IN_AUTOMATION')

    def set_TF_REGISTRY_DISCOVERY_RETRY(self, value: str):
        self.set_env('TF_REGISTRY_DISCOVERY_RETRY', value)

    def unset_TF_REGISTRY_DISCOVERY_RETRY(self):
        self.unset_env('TF_REGISTRY_DISCOVERY_RETRY')

    def set_TF_REGISTRY_CLIENT_TIMEOUT(self, value: str):
        self.set_env('TF_REGISTRY_CLIENT_TIMEOUT', value)

    def unset_TF_REGISTRY_CLIENT_TIMEOUT(self):
        self.unset_env('TF_REGISTRY_CLIENT_TIMEOUT')

    def set_TF_CLI_CONFIG_FILE(self, value: str):
        self.set_env('TF_CLI_CONFIG_FILE', value)

    def unset_TF_CLI_CONFIG_FILE(self):
        self.unset_env('TF_CLI_CONFIG_FILE')

    def set_TF_IGNORE(self, value: str):
        self.set_env('TF_IGNORE', value)

    def unset_TF_IGNORE(self):
        self.unset_env('TF_IGNORE')

    def auto_approve(self, value: bool = True):
        self._auto_approve = value

    def auto_approve_apply(self, value: bool = True):
        self._auto_approve_apply = value

    def auto_approve_destroy(self, value: bool = True):
        self._auto_approve_destroy = value

    def set_var(self, name: str, value: any):
        self._var[name] = value

    def unset_var(self, name: str):
        self._var.pop(name)

    def init(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Prepare your working directory for other commands"""
        return self._run(['init'], *args, call_kwargs=call_kwargs, **kwargs)

    def validate(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Check whether the configuration is valid"""
        return self._run(['validate'], *args, call_kwargs=call_kwargs, **kwargs)

    def plan(self,
             name: Optional[str] = None,
             *args: ArgType,
             var: Optional[dict] = None,
             call_kwargs: Optional[dict] = None,
             **kwargs):
        """Show changes required by the current configuration"""
        _args = chain(args, self._vars(var), self._vars(self._var), [name])
        return self._run(['plan'], *_args, call_kwargs=call_kwargs, **kwargs)

    def apply(self,
              *args: ArgType,
              var: Optional[dict] = None,
              call_kwargs: Optional[dict] = None,
              **kwargs):
        """Create or update infrastructure"""
        _args = chain(args, self._vars(var), self._vars(self._var))
        if self._auto_approve or self._auto_approve_apply:
            kwargs['auto_approve'] = True
        return self._run(['apply'], *_args, call_kwargs=call_kwargs, **kwargs)

    def destroy(self,
                *args: ArgType,
                var: Optional[dict] = None,
                call_kwargs: Optional[dict] = None,
                **kwargs):
        """Destroy previously-created infrastructure"""
        _args = chain(args, self._vars(var), self._vars(self._var))
        if self._auto_approve or self._auto_approve_destroy:
            kwargs['auto_approve'] = True
        return self._run(['destroy'], *_args, call_kwargs=call_kwargs, **kwargs)

    def console(self, stdin: str, call_kwargs: Optional[dict] = None, **kwargs):
        """Try Terraform expressions at an interactive command prompt"""
        _call_kwargs = call_kwargs if call_kwargs else {}
        return self._run(['console'], call_kwargs={**_call_kwargs, 'stdin': stdin}, **kwargs)

    def fmt(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Reformat your configuration in the standard style"""
        return self._run(['fmt'], *args, call_kwargs=call_kwargs, **kwargs)

    def force_unlock(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Release a stuck lock on the current workspace"""
        return self._run(['force_unlock'], *args, call_kwargs=call_kwargs, **kwargs)

    def get(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Install or upgrade remote Terraform modules"""
        return self._run(['get'], *args, call_kwargs=call_kwargs, **kwargs)

    def graph(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Generate a Graphviz graph of the steps in an operation"""
        return self._run(['graph'], *args, call_kwargs=call_kwargs, **kwargs)

    def import_(self,
                *args: ArgType,
                var: Optional[dict] = None,
                call_kwargs: Optional[dict] = None,
                **kwargs):
        """Associate existing infrastructure with a Terraform resource"""
        _args = chain(args, self._vars(var), self._vars(self._var))
        return self._run(['import'], *_args, call_kwargs=call_kwargs, **kwargs)

    def login(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Obtain and save credentials for a remote host"""
        return self._run(['login'], *args, call_kwargs=call_kwargs, **kwargs)

    def logout(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Remove locally-stored credentials for a remote host"""
        return self._run(['logout'], *args, call_kwargs=call_kwargs, **kwargs)

    def output(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show output values from your root module"""
        return self._run(['output'], *args, call_kwargs=call_kwargs, **kwargs)

    def output_json(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show output values as json from your root module"""
        kwargs['json'] = True
        return self._run(['output'], *args, call_kwargs=call_kwargs, **kwargs)

    def providers(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the providers required for this configuration"""
        return self._run(['providers'], *args, call_kwargs=call_kwargs, **kwargs)

    def providers_lock(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Write provider dependency information into the dependency lock file"""
        return self._run(['providers', 'lock'], *args, call_kwargs=call_kwargs, **kwargs)

    def providers_mirror(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Download the providers required for the current configuration"""
        return self._run(['providers', 'mirror'], *args, call_kwargs=call_kwargs, **kwargs)

    def providers_schema(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Print detailed schemas for the providers used in the current configuration"""
        return self._run(['providers', 'schema'], *args, call_kwargs=call_kwargs, **kwargs)

    def refresh(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Update the state to match remote systems"""
        return self._run(['refresh'], *args, call_kwargs=call_kwargs, **kwargs)

    def show(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the current state or a saved plan"""
        return self._run(['show'], *args, call_kwargs=call_kwargs, **kwargs)

    def show_json(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the current state as json or a saved plan"""
        kwargs['json'] = True
        return self._run(['show'], *args, call_kwargs=call_kwargs, **kwargs)

    def state(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Advanced state management"""
        return self._run(['state'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_list(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """List resources in Terraform state"""
        return self._run(['state', 'list'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_mv(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Move a resource to a different resource instance address in Terraform"""
        return self._run(['state', 'mv'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_pull(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Download and output the remote state"""
        return self._run(['state', 'pull'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_push(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Upload local state file to remote state"""
        return self._run(['state', 'push'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_replace_provider(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Replace the provider for resources in a Terraform state"""
        return self._run(['state', 'replace-provider'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_rm(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Remove a resource from state without destroying it"""
        return self._run(['state', 'rm'], *args, call_kwargs=call_kwargs, **kwargs)

    def state_show(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the attributes of a single resource in the Terraform state"""
        return self._run(['state', 'show'], *args, call_kwargs=call_kwargs, **kwargs)

    def taint(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Mark a resource instance as not fully functional"""
        return self._run(['taint'], *args, call_kwargs=call_kwargs, **kwargs)

    def untaint(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Remove the 'tainted' state from a resource instance"""
        return self._run(['untaint'], *args, call_kwargs=call_kwargs, **kwargs)

    def version(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the current Terraform version"""
        return self._run(['version'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Workspace management"""
        return self._run(['workspace'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace_list(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """List all existing workspaces"""
        return self._run(['workspace', 'list'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace_select(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Switch to an existing workspace"""
        return self._run(['workspace', 'select'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace_new(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Create a new workspace"""
        return self._run(['workspace', 'new'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace_delete(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Delete an existing workspace"""
        return self._run(['workspace', 'delete'], *args, call_kwargs=call_kwargs, **kwargs)

    def workspace_show(self, *args: ArgType, call_kwargs: Optional[dict] = None, **kwargs):
        """Show the currently selected workspace"""
        return self._run(['workspace', 'show'], *args, call_kwargs=call_kwargs, **kwargs)
