# Intro to AI

---
Instructor: Dr. Sen Lin
Email: slin50@central.uh.edu
TA: Anjir Chowdhury (aachowd4@cougarnet.uh.edu), Zheng Wang (zwang214@cougatnet.uh.edu)

---

## Defining AI
AI behavior can be categorized in four different ways:

- Systems that think like humans
    decision-making, problem solving, etc (Bellman, 1978)

- Systems that think rationally
    persive, reason and act (Winston, 1992)

- Systems that act like humans
    do things that people are better at (very specific things) (Rich and Knight, 1991)

- Systems that act rationally
    explain and emulate intelligent behavior in terms of computational processes (Schalkoff, 1990)

**Modern Definition**

- CS, engingineering and math branch that aims to create machines and software capable of performing tasks that usually require human intelligence

- centers on simulation of human intelligence using computers

- not a monolith

## Big names in AI founding

**Alan Turing**
Turing machine and test: if an ai system is not distinguishable from human being, it is defenitely intelligent

**Claude Shannon**
Boolean algebra and digital circuits

## Highs and lows of AI trends

There have been a lot of summers (high points) and winders (low points) for ai. Main reasons why AI has gone low is because of a lack of funding from research not giving any  new progress of findings. Every couple of years there is a new dicovery and there is a new wave of hype around AI. Currently we are on one of the summers with the big developments that transformers have done for the LLMs. (are we about to go on a ai winter? how long till next discovery and advancement?)

## What are new advances and driving forces

### Heirarchical Representation Learning

- if we know A how much can we know about B
- If we understand the underlying features of data and understant the world in terms of a heirachy of concepts then we would be able to predict anything.
- Usually hand engineered features are time consuming, brittle, and not scalable in practice

### Driving forces and success

1. big data: larger datasets and easier collection & storage
2. Hardware: betters GPUs with ability to have larger model sizes
3. Software: improved techniques and toolboxes

### Search

search algorithms: search space reduction, ordering solutions intelligently, simplifiecation of computations

route finding based on different objectives and actions

### Object detection

prediction of where an object is and what it is

this is related to image generation, and speech recognition

### Text generation

- use model that will statistically predict the next most likely word, taking into a count the previous words used and context
- very hyped type of ai atm with the big advancements in LLMs

## AI Paradigms

### Modeling

- Transform complex real-world problems into formal mathematical objects (models)
- simplifies world
- modeling is lossy: the real world is rich, which generally can not be captured in its entirety

There can be multiple types of models:

**Relfex**
- performs fixed sequence of computations on a given input
- feed-forward (no backtracking)
- too simple for tasks that require more forethought
- Ex: linear classifiers, deep neural networks

**State**
- model the state of a world and transitions between states which are triggered by actions
- similar to a behaviour tree?
- think in terms of states, actions, and cost/rewards
- Applications: games, robotics, natural language processing
- other problems that take use of state based models are: search problems (you control everything), arkov decision problems (against nature), adversarial games (against opponents)

**Variable**
- think in terms of variables, factors and weights
- the dependency structure is given by the graph structure, which formally defines a joint probability distribution over all variables.
- Ex: bayesian networks (tracking cars from sensors), constraint satisfaction problems (sudoku, scheduling)

**Logic**
- think of a virtual assistant
- needs to remember context what it has been told and answer questions that require drawing inferences from its knowledge

### Interface

- given a model, interface seeks to answer questions with respect to the model
- find efficient algorithms that can answer the questions
- ansewr questions against the model

### Learning

- when the model commbined with data learns to predict outcomes
- build empty model + data + learning -> model with learnt parameters
- construct model from data
