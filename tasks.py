"""
tasks to kick-off the project
"""

from invoke import task


@task
def formatter(tsk, fix=False):
    """
    python format
    """
    auto_fix = "" if fix else "--check --diff"
    cmd = " && ".join(
        [
            f"python -m black . {auto_fix}",
        ]
    )
    tsk.run(cmd, echo=True, pty=True)


@task
def lint(tsk, fix=False):
    """
    python lint
    """
    flags = "--fix" if fix else ""
    cmd = " && ".join(
        [
            f"ruff *.py {flags} ai21/ tests/",
        ]
    )
    tsk.run(cmd, echo=True, pty=True)


@task(optional=["coverage"], help={"coverage": "[true|false]"})
def test(tsk, coverage=False):
    """
    Run unit tests
    """
    cov = "--cov --cov-report=term-missing" if coverage else ""
    cmd = f"poetry run pytest {cov}"
    tsk.run(cmd, echo=True, pty=True)


@task
def audit(tsk):
    """
    Run audit check on the dependent packages
    """
    cmd = "safety check --full-report"
    tsk.run(cmd, echo=True, pty=True)


@task
def staticcheck(tsk):
    """
    Run static check on the projects files
    """
    cmd = "mypy ai21 tests"
    tsk.run(cmd, echo=True, pty=True)


@task
def isort(tsk):
    """
    Run static check on the projects files
    """
    cmd = "isort ai21 tests"
    tsk.run(cmd, echo=True, pty=True)


@task
def build(tsk):
    """
    generate a package for ai21
    """
    cmd = "poetry build"
    tsk.run(cmd, echo=True, pty=True)


@task
def update(tsk):
    """
    update outdated packages
    """
    cmd = "poetry update"
    tsk.run(cmd, echo=True, pty=True)


@task
def outdated(tsk):
    """
    update outdated packages
    """
    cmd = "poetry show --outdated --top-level"
    tsk.run(cmd, echo=True, pty=True)
