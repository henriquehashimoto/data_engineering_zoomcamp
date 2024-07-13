# Week 2 - Workflow Orchestration

# Content

## [Video 1 - What is Orchestration?][video_1]
- [Slides][slides_1]

### What is Orchestration?

- Orchestration is the process of dependency management, facilitated through automation.
- A large part of data engineering is extracting, transforming, and loading data between multiple sources. An engineer's goal is to automate as many processes as possible. 
- A data orchestrator helps in this regard by managing scheduling, triggering, monitoring, and resource allocation for DE workflows.


**Every workflow requires sequential steps:**

Steps = tasks = blocks (mage lingo)

Workflows = DAGs (directed acyclic graphs) or Pipeline


### Features of a good Orchestrator

**A good orchestrator handles**: 

- workflow management
- automation
- error handling - conditional logic, branching, retry
- data recovery
- monitoring and alerting
- resource optimization
- observability
- debugging
- compliance and auditing
- and prioritizes developer experience and facilitates seamless development
- flow state
- feedback loops - ability to iterate quickly
- cognitive load

---

## [Video 2 - What is Mage][video2]

- Mage is an open-source pipeline tool for orchestrating, transforming, and integrating data

- Mage is an orchestration tool in the same vein as Airflow. What makes it different is that unlike Airflow is a general orchestration tool which is often used to run data pipelines, **Mage is an orchestration tool purpose built for data pipelines.**

- It accomplishes this by making the development experience seamless by having most of the common building blocks built in, so that developers can focus on business logic instead of reinventing the wheel with every pipeline.

### What Mage offers

**Hybrid Environment:**

- Use the GUI or develop completely outsideee of the tool and sync

**Improved Developer Experience:**

- Blocks can be used as a testable, reusable piece of code
- Code and test in parallel
- Reduce the dependencies on different tools nad the need to swtich between them

**Build in Engineering Best Practives:** 

- In line testing and debugging
- Fully-featured observability capability including integration with dbt for complete visibility of your pipelines


### Core Components

**Projects:**

- Are the basis for all work done in Mage (like a GitHub repo)
- Contain the code for pipelines, blocks, and other assets
- A Mage instance has one or more projects

**Pipelines:**

- Workflow that perform some operation
- Are made up of blocks
- Are represented by a YAML

**Blocks:**

- SQL, Python, or R files that can be executed independently or as part of a pipeline
- Can be used to perform a variety of actions from simple data transformations to complex ML models
- Are defined globally. Changing a block in one place will change the block everywhere it is used, but blocks can be detached to separate instances if needed.
- Components of a block:
    - Imports
    - Decorators
    - Function that returns dataframe
    - Assertions
    - tests that run on the output dataframe of the block
    - you can have zero to many assertions


[video_1]: https://www.youtube.com/watch?v=Li8-MWHhTbo&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=18&ab_channel=Mage
[slides_1]: https://docs.google.com/presentation/d/17zSxG5Z-tidmgY-9l7Al1cPmz4Slh4VPK6o2sryFYvw/edit?pli=1#slide=id.p
[video2]: https://www.youtube.com/watch?v=AicKRcK3pa4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=18&ab_channel=Mage
