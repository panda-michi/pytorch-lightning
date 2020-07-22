"""Root package info."""

__version__ = '0.8.6-dev'
__author__ = 'William Falcon et al.'
__author_email__ = 'waf2107@columbia.edu'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright (c) 2018-2020, %s.' % __author__
__homepage__ = 'https://github.com/PyTorchLightning/pytorch-lightning'
# this has to be simple string, see: https://github.com/pypa/twine/issues/522
__docs__ = "PyTorch Lightning is the lightweight PyTorch wrapper for ML researchers." \
           " Scale your models. Write less boilerplate."
__long_docs__ = """
Lightning is a way to organize your PyTorch code to decouple the science code from the engineering.
 It's more of a style-guide than a framework.

In Lightning, you organize your code into 3 distinct categories:

1. Research code (goes in the LightningModule).
2. Engineering code (you delete, and is handled by the Trainer).
3. Non-essential research code (logging, etc. this goes in Callbacks).

Although your research/production project might start simple, once you add things like GPU AND TPU training,
 16-bit precision, etc, you end up spending more time engineering than researching.
 Lightning automates AND rigorously tests those parts for you.

Overall, Lightning guarantees rigorously tested, correct, modern best practices for the automated parts.

Documentation
-------------
- https://pytorch-lightning.readthedocs.io/en/latest
- https://pytorch-lightning.readthedocs.io/en/stable
"""

import importlib.util
import logging as python_logging


_logger = python_logging.getLogger("lightning")
_logger.addHandler(python_logging.StreamHandler())
_logger.setLevel(python_logging.INFO)

# This variable is injected in the __builtins__ by the build
# process. It is used to enable importing subpackages of skimage when
# the binaries are not built
__LIGHTNING_SETUP__ = "__LIGHTNING_SETUP__" in dir(__builtins__)

if __LIGHTNING_SETUP__:  # pragma: no-cover
    import sys
    sys.stdout.write(f'Partial import of `{__name__}` during the build process.\n')
    # We are not importing the rest of the lightning during the build process, as it may not be compiled yet
else:
    import torch
    APEX_AVAILABLE = importlib.util.find_spec("apex") is not None
    BOLTS_AVAILABLE = importlib.util.find_spec("pytorch_lightning.bolts") is not None
    HOROVOD_AVAILABLE = importlib.util.find_spec("horovod") is not None
    NATIVE_AMP_AVALAIBLE = hasattr(torch.cuda, "amp") and hasattr(torch.cuda.amp, "autocast")
    TORCHTEXT_AVAILABLE = importlib.util.find_spec("torchtext") is not None
    TORCHVISION_AVAILABLE = importlib.util.find_spec("torchvision") is not None
    XLA_AVAILABLE = importlib.util.find_spec("torch_xla") is not None

    from pytorch_lightning.core import LightningModule, data_loader
    from pytorch_lightning.callbacks import Callback
    from pytorch_lightning.trainer import Trainer
    from pytorch_lightning.utilities.seed import seed_everything
    from pytorch_lightning import metrics
    from pytorch_lightning.core.step_result import TrainResult, EvalResult

    __all__ = [
        'Trainer',
        'LightningModule',
        'Callback',
        'data_loader',
        'seed_everything',
        'metrics',
        'EvalResult',
        'TrainResult'
    ]

    # necessary for regular bolts imports. Skip exception since bolts is not always installed
    if BOLTS_AVAILABLE:
        from pytorch_lightning import bolts
    # __call__ = __all__

# for compatibility with namespace packages
__import__('pkg_resources').declare_namespace(__name__)
