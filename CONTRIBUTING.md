Any kind of contribution is welcome as long as the methodology below is followed.

# A. Methodology

## 1. Code Contributions
Any contribution that was made with code is considered *code contribution*.

### a. Branching
Below are some conventions on branching.

#### i. Outbranching
This project has two permanent and one semi-permanent branches which are 
called `master` and `stable` and any `milestone/*` type. `master` branch
contains the latest stable version of the project in case anybody might
want to clone the library while `stable` branch has cutting-edge changes.
`milestone/*` typed branches can be created by only main contributors,
which includes cutting edge codebase just like `stable` yet it is planned
to be merged to stable in the milestone release.

That is why, for outsiders to contribute code, they must outbranch the
`stable` branch, make changes and send PR. This also includes for a code
contributor to follow up the changes on `stable` branch. If the contributor
is a main contributor, they might outbranch one of `milestone/*` typed
branches.

Any contribution in code that does follow the methodology;

 - will be merged in the next patch ASAP if it doesn't break the architecture
 of code,
 - or will be merged in the next minor or major release if it is marked in
 a milestone.

#### ii. Branch Naming Conventions
Branch naming conventions can be considered *should* yet a *strong should*.
Branch names have a two-sided pattern which includes (i) the type of branch
and (iii) the topic of branch.

    type/topic

Type names *should* contain 4 characters maximum. In case it is favorable to
have more than 4 characters, this rule might be avoided. It is also better
to only have one word as type. The common types are as below:

 - **fix**: Fixing an issue.
 - **hotfix**: Fixing a critical issue. This branches are considered to be
 merged immediately.
 - **feat**: Adding a feature.
 - **milestone**: This type can only be created by main contributors.

Topic is about whatever the branch resolves in the codebase. However, it
*must* follow the dash-separated conventions as below:

    this-is-dash-separated-topic

It is a good practice to keep topic as short as possible.

Considering type and topic, below are some examples which are considered
valid and invalid branch names (invalid ones should be reconsidered by
the contributors, those are not strictly banned):

    #########
    # Valid #
    #########
    fix/white-space
    hotfix/mem-leak
    feat/button-color # this is for real
    milestone/0.5.0a
    
    ###########
    # Invalid #
    ###########
    hot-fix/so-long-that-makes-you-cancer
    i have whitespaces # self-explanatory

### b. Coding Conventions
 - **Test your code**. Testing might not clean bugs on your code, but
 ensures that the code you have written works as intended.
 - **Update changelog** if license enforces to do so. Still, it is a
 great practice even if it doesn't.
 - **Follow conventions on the target language/framework**.

### c. Pull Request Conventions

#### i. Rationale
A pull-request text should have a section called *rationale*, in which
it is written *why* the change is needed in codebase. Even if it is hard
for contributor to provide a well-formed and well-formatted reason, the
pull-request contributor *must* answer *why* at least. A well-formed
and well-formatted example:

    # Rationale
    According to issue #666, the community needs this feature...
    I used this kind of architecture because...

Or, keep it short;

    Fixes the critical issue on #666.

#### ii. Addition-Change-Deletion

Give information about what has been added, changed or removed from codebase
and definitely tell its *backwards compability*, how the former tests are
affected.

If former tests are affected and fails, you should change the code for those
tests to pass, better keeping the backwards compability. If BC is not kept
and the codebase is affected drastically, the PR might be merged in next
milestone or never at all.

It is a good practice to communicate main developers if you need to change
the tests because it usually means you change the behavior when you change
the tests.

You can either used a well-formed and well-formatted bullet points or you
can use plain English as long as you are clear on what you have done. An
example can be seen as below:

    - Added A.
    - Removed B.
      - Changed D. # subpoint here means D was affected by B's removal.
    - Changed C.
      - Changed E. # subpoint here means E was affected by C's change.

It is also project the changes on documentation. However, in case you will
not change the documentation, you need to be clear about the ACDs on code
as in example above so that the issues regarding to documentation
will be opened by maintainers after merge.