* Identify the key components of the ML Lifecycle.
* Define “concept drift” as it relates to ML projects.
* Differentiate between shadow, canary, and blue-green deployment scenarios in the context of varying degrees of automation.
* Compare and contrast the ML modeling iterative cycle with the cycle for deployment of ML products.
* List the typical metrics you might track to monitor concept drift.

# Course Scope

* C1 Introduction to Machine Learning in Production
* C2 Machine Learning Data Lifesycle in Production
* C3 Machine Learning Modeling Pipelines in Production
* C4 Deploying Machine Learning Models in Production

# C1 Introduction to Machine Learning in Production

## Blueprint

machine learning project modules
![alt text](image-0.png)

machine learning project lifecycle
![alt text](image-1.png)

Three parts are equally important: Code + Hyperparamters + Data >> ML Model

MLOps(Machine Learning Operations): an emerging discipline, and comprises a set of tools and principles to support progress throughthe ML project lifecycle. **Systematic way of thinking**

Stages: Scoping >> Data >> Modeling >> Deployment
Iterative: First deployment v.s. Maintainence

## 1. Scoping

### Scoping process

* Brainstorm business problems(not AI problem)
  * What are the top 3 things you wish were working better?
* Brainstorm AI solutions
* Assess the feasibility (dilligence): is it technically feasible?
  * Use external benchmark to evaluate(literature, other company, competitor)
  ![alt text](image-21.png)
  * Do we have features that are predictive?
  * The history of the project
  * Dilligence on value (Fermi estimates)
  ![alt text](image-22.png)
* Assess potential solutions
* Determinate milestones
  * Key specifications:
    * ML metrics (accuracy, presicion/recall, etc)
    * Software matrics(latency, throughput,etc.given compute resources)
    * Business metrcs(revenue, etc)
* Budget for resources
  * Resources needed(data, personnel, help from other teams)
  * Timeline

**xhu_Note**:

1. Separating problem identification from solution and use each 'method' to solve eacn 'problem' (learned from marker_cleanup_post too)
2. What to achieve > How to achieve
3. Two dimension coordination system is quite useful to help sorting

## 2. Data

### Define Data and Establish Baseline

Data defination: input X and target label Y

* Major type of data problems
  ![alt text](image-14.png)
  * Unstructured adata:
    * May or may not have huge collection of unalbeled exmpales x.
    * Human can label more data
    * Data agumentation more likely to be helpful
  * Structured data:
    * May be more difficult to obtain more data
    * Human labeling may not be possible
  * Small data:
    * Clean labels are critical
    ![alt text](image-15.png)
    * Can manually lookthrough dataset and fix labels
    * Can get all the labelers to talk to each others
  * Big Data:
    * Emphasis data process
    * (Big data sometimes have long tail of rare events in the input where clean labels are critical too < small data problem >)

**xhu note:** different Eng/Proj experiences might only map to one quadrant of above cordination system. (FT ?-> Structured + Big Data)

### Label and organize data

* Improving label consistancy
  * Have multiple labelers label same example
  * Where there is disagree,emt, have MLE, subhect matter export (SME)and /or labeler discuss defination of y to reach
  * If labelers believe that x does NOT contrain enough information, consider changing x
  * Iterate until it is hard to significate improve the data
  * Have a class/label to capture uncertainty: 0 , borderline, 1
  * ![alt text](image-16.png)

* Human level performance (HLP)
  * Why HLP? Estimate Bayes error / irreducible error to help with error analysis and prioritiaztion
  ![alt text](image-17.png)

### Obtaining data

* Get into iteration loop as quickly as possible (Unless you have worked on the problem before and have sense of how much data it is need)
* Ask: How much data can we obtain in k days?
* Brainstorm list of data sources:
  ![alt text](image-18.png)
* Labeling data
  * Options: In-house v.s. outsourced v.s. crowdssourced
  * Don't increase data by more than 10x at a time
  * Label data yourself for a while to get the 'sense'

### Data pipeline (in iteration)

* Make sure the scripts/data is replicable
* POC (proof-of-concept) > Production phases:
  * ![alt text](image-19.png)
* Balanced train/dev/test splits
  * distribute 3 set equally in small data problems
  * random split will be representative
* Example: **keep track of data provenace and lineage** (using meta data is one of the methods)
    ![alt text](image-20.png)

## 3. Modeling

AI system = Code (algorithm/model) + Data
Model-centic AI development v.s. Data-centric AI development

### Key changllenges

* Model development is an iterative process
  * ![alt text](image-5.png)
* Challenges in model development
  * Do well in : training set > dev/test set > business metric/project goals
  * Why low avg error isn't good enough: single std can not reflact on key slices
* Rare classes
  * Skewed data distribution
  * Accuracy in rare classes

### Selecting and training model

* Establish a baseline
  * Establish a baseline level of performace
  * Unstructured and structured data: human good at unstructured v.s. machine good at structured
  * ![alt text](image-6.png)
* Tips for getting started
  * Starting on modeling
    * literacture search to see what's possible (courses, blogs, open-source projects)
    * Find open-source implementations if avaiblable
    * A reasonable algorithm with good data will often outperform a great algorithm with no so good data > lastest != greatest
  * Sanity-check for code and algorithm
    * overfit a small training dataset before the large one

### Error analysis

* Use tags can help catergoize issue
    ![alt text](image-7.png)
* Prioritizing what to work on
  * How much room for improvement there is
  * How frequently that category appears
  * How easy is to improve accuracy in that catergory
  * How important it is to improve in that catergory
* Adding/improving data for specific categories (for target catego)
  * Collect more data
  * Use data aguementation to get more data
  * Importve label accuracy / data quality

Example Analysis

Skewed dataset : large portion of data is '0'
![alt text](image-8.png)
![alt text](image-9.png)

### Performace auditing

Auditing framework

* Check for accuracy, fiarness/bias, and other probelms
  * Brainstore what might go wrong
  * Establish metrics

### Data iteration Loop (during iteration of model)

**Model-centric view:** Take the data you have and develop a model that does as well as possible > Hold the data fixed and iteratively improve the code/mode
**Data-centric view:** The quality of the data is paramount. Use tools to improve the data quality; this will allow multiple models to do well > Hold the code fixed and iteratively improve the data

Example of data augmentation analysis
![alt text](image-10.png)

* Data augmentaiton
  * Goal: Create 'realistic' examples that algotiythm does poorly on but humans (or other baseline) can do well on
* Data iteration
  * ![alt text](image-11.png)
  * for unstructure data: If the model is sufficiently large (less bias), adding data will not hurts accuracy
  * for structure data: Adding features. (collebrative filter v.s. content filter aka cold-start filter)
* Experiment tracking (systematic)
  * ![alt text](image-12.png)

![alt text](image-13.png)

## 4. Deployment

### Key challenges

* Concept drift & Data drift
  * Concept drift: X-> Y mapping drift
  * Data drift: training set/test set etc. gradual change / sudden shock
* Software engineering issues
  * Realtime or Batch
  * Cloud vs. Edge/Browser
  * Coupute resources (CPU/GPU/memory)
  * Latency, thoughput(QPS: query per seconds - e.g. 500ms)
  * Security and privacy

### Deployment patterns

* Common deployment cases:
  * New oriduct/capaibility
  * Automate/assist with manual task
  * Replace previous ML system

* Common deployment methods:
  * Canary deployment : Gradual ramp up with monitoring or Rollback
  * Blue green deployment: Switch to new model directly but can swtich back
  * Degree of automation:
  Human only >> Shadow mode >> AI assistance >> Partial automation >> Full automation
![alt text](image-2.png)

### Monitoring + Maintainance

![alt text](image-3.png)
![alt text](image-4.png)

Ref:

* <https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf>
* <http://arxiv.org/abs/2011.09926>
* <http://arxiv.org/abs/2010.02013>

# C2 Machine Learning Engineering for Production (MLOps) Specialization

![alt text](image-26.png)
![alt text](image-23.png)

## C2W1 Collecting,Labeling and Validating Data

* Production ML = ML development + software development
  ![alt text](image-24.png)
  ![alt text](image-25.png)
* Managing the entire life cycle of data
  * Labeling
  * Feature space coverage
  * Minimal dimensionality
  * Maximum predictive data
  * Fairness
  * Rare conditions
* Modern software development (Criterias)
  * Scalability
  * Extensibility
  * Configuration
  * Consistency & reproducibility
  * Safety & security
  * Modularity
  * Testability
  * Monitoring
* Challenges in production grade ML
  * Build itergrated ML system
  * Continuous operate it in production
  * Handle continuously changing data
  * Optimize compute resource costs

### ML Pipelines

![alt text](image-27.png)
![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)

### Collecting Data

data collect > ingest > prepare

* Importance of data quality
* Data pipeline: data collection, ingestion and preparation
* Data collection and monitoring
![alt text](image-31.png)

Key points:
  ![alt text](image-33.png)
  ![alt text](image-34.png)

**xhu NOTE**

* Representational harms include perpetuating harmful stereotypes about or minimizing the existence of a social group, such as a racial, ethnic, gender, or religious group. Machine learning algorithms often commit representational harm when they learn patterns from data that have algorithmic bias.
* Rater categorise: generalist , experts & targer users

### Labeling Data

* Model performance decays over time, and model retraining helps improve or maintain performance.
* Data labeling is a key part of supervised learning and needs to be approached based on the specific problem and domain.
![alt text](image-35.png)

![alt text](image-36.png)
![alt text](image-37.png)

* Direct Labeling v.s. Derived Labeling (Human raters)

**xhu note**
Direct Labeling (aka Process Feedback) labels come from monitoring predictions, not from a "rater" as in this example. But what id we don't have data to log?:

* Use a heuristic for a first launch, then train a system based on logged data.
* Use logs from a similar problem to bootstrap your system.
* Use human raters to generate data by completing tasks.
* ref:<https://developers.google.com/machine-learning/data-prep/construct/collect/label-sources>

### Validating Data

#### Data Issues

* drift and skel
  * data and concept drift
  * schema skel
  * distribution skek

| Concept | Description |
|-------------|-------------|
| Drift       | Changes in data over time, such as data collected once a day |
| Skew        | Difference between two static versions or different sources, such as training set and serving set |
![alt text](image-38.png)
![alt text](image-39.png)

#### Detecting data issues

* detecing schema skew
  * Training and serving data do not conform to the same schema
* deteching distribution skew
  * dataset shift -> covariate or concept shift
  ![alt text](image-40.png)

**data requires continuous evaluation**
![alt text](image-41.png)

TensorFlow Data Validation
![alt text](image-42.png)

<https://github.com/cdfoundation/sig-mlops/blob/main/roadmap/2022/MLOpsRoadmap2022.md>

## C2W2 Feature Engineering, Transformation and Seletion

### Feature Engineering

#### Introduction

* Squeezing the most out of data
  * Making data usefulbefore training a model
  * Representing data in forms that help models learn
  * Increasing predictive quality
  * Reducing dimentionalitywith feathre engineering
* The art of feature engineering
  * ![alt text](image-43.png)
* How feature engineering is done ina typical ML pipeline
  * ![alt text](image-45.png)
* Feature engineering process
  * ![alt text](image-44.png)

#### Preprocessing Operations

* Main preprocessing operations
  * Data cleansing, Feature tuning, Representation transofmration, Feature extractation, Feature construction
* Mapping raw data into features (Vectorizel)
  * ![alt text](image-46.png)
* Mapping numeric values
* Mapping catergorical values
  * ![alt text](image-47.png)
* Empirical knowledge of data
  * Text  - stemming, lemmatization, TF-IDF embedding lookup
  * Imges- clipping, resizing, cropping, blur, Canny filters, Sober filters
  ![alt text](image-48.png)

#### Techniques

* Feature Scaling
  * Converts values from natural range into a prescribed range. e.g. (0,255) to (-1,1)
  * Benefits: coverge faster, lower NaN, model learns the right weights
* Normalization and Standardization
  * ![Normalization](image-49.png)
  * ![Standardization](image-50.png)
* Bucketizing / Binning
* Other techniques
  * Dimensionality reduction in embeddig
  * (TensorFlow embedding projector for high dimension data visualize)
  * Feature corsses: Combines multiple features together into a new feature(space)/encode same into in fewer features, e.g A, B -> A x B
  * Feature coding: transforming categorical to a continuous variables
  ![alt text](image-51.png)

### Feature Transform in scale

![alt text](image-52.png)

#### Preprocessing Data at Scale

  ![alt text](image-53.png)

* Inconsistancies in feature engineering (important)
  * traning & serving code paths are different
  * diverse delopments scenarios: mobile - TF lite, server - TF Serving, Web -TF JS
  * risk of introducing training-serving skew
  * skel will lower the performace of your serving model
* Preprocssing granularity
  * ![alt text](image-54.png)
* Pre-procssing training dataset
    |                            | Pre-processing training dataset | Transforming within the model |
    |----------------------------|---------------------------------|-------------------------------|
    | Pros                       | - Run-once                       | - Easy iteration              |
    |                            | - Compute on the entire dataset | - Transformation guarantees   |
    | Cons                       | - Transformations reproduced at serving | - Slower iteration |
    |                            | - Ling model latency            | - Expensive transforms       |
    |                            | - Transformations per batch: skew |                               |
* Optimizing instance-level transformations
  * indirectly affect traning efficiency
  * typically accelerators sit idle while the CPUs transform
  * Solutions:
    * Prefetching transforms for better accelerator efficiency
* Sum of Challanegs
  * Balancing the predictive performace
  * Full-pass transformations on traning data
  * Optimizing instance0level transforations for better traning efficiency
  ![alt text](image-55.png)

#### TensorFlow Transform

* Benefits of using TensorFlow Transform
  ![alt text](image-61.png)
* Applied feature transformations
* tf.Transform Analyzers
  ![alt text](image-56.png)
  ![alt text](image-57.png)
  ![alt text](image-58.png)
  ![alt text](image-59.png)
  ![alt text](image-60.png)
  ![alt text](image-62.png)

**xhu Note**

<https://www.tensorflow.org/tfx/guide/tft_bestpractices>

### Feature Selection

#### Feature Spaces

* Introductions to Feature Space
  * N dimesional space defined by N features
  * Not including the target label
      X = [x1, x2, x3, ..., xN]
  * Feature space coverage:
    * Same numerical ranges
    * Same classes
    * Similar characteristics for image data
    * Similar vocabulary, syntax and sematics for NLP data
  * ![alt text](image-63.png)

#### Feature Selection

* Why?
  * identify featues that best represent the data
  * remove featues that don't influence the outcome
  * reduce the size of the feature space
  * resuce the resource requirements and model complexity (IO, storage, and inference costs)
* How?
  * Unsupervised
    * Feature-target variable relationship NOT considered
    * Remove redundant features(correlation)
  * Supervised
    * Feature-target variable relationship considered
    * Select features that are most relevant to the target variable

* Supervised Feature Selection Methods:
  ![alt text](image-66.png)
  ![alt text](image-67.png)
  * Filter Methods: e.g.Pearson correlation
      Filter methods suffer from inefficiencies as they need to look at all the possible feature subsets.
      ![alt text](image-64.png)
  * Wrapper Methods
      Wrapper methods are based  on the greedy algorithm and thus solutions are slow to compute.
      ![alt text](image-65.png)
  * Embedded Methods

**xhu Note**

<https://www.tensorflow.org/tfx/guide#tfx_pipelines>

## C2W3 Data Journey and Data Storage

### Data Journey

#### The data journy

* Raw features and labels
* Input-output map
* ML model to learn the map
  ![alt text](image-68.png)

#### Data provenace

  ![alt text](image-69.png)

#### Data lineage

  ![alt text](image-70.png)

#### Data versioning

  ![alt text](image-71.png)

### ML metadata

Metadata: Tracking artifacts and pipeline changes (Using ML metadata to track changes)
Ordinary ML data pipeline

* Data Validation -> Data Transformation
![alt text](image-72.png)

|         Units                   | Types           | Relationships |
|----------------------------|-----------------|-----------------|
| Artifact                       | ArtifactType   | Event            |
| Execution                     | ExecutionType | Attribution   |
| Context                        | ContextType   | Association    |

![alt text](image-73.png)
![alt text](image-74.png)

#### ML Data

* Architecture and nomenclature
* Tracking metadata flowing between components in pipeline
![alt text](image-75.png)

![alt text](image-76.png)

```html
Data model ref: https://www.tensorflow.org/tfx/guide/mlmd#data_model

The Metadata Store uses the following data model to record and retrieve metadata from the storage backend.

* ArtifactType describes an artifact's type and its properties that are stored in the metadata store. You can register these types on-the-fly with the metadata store in code, or you can load them in the store from a serialized format. Once you register a type, its definition is available throughout the lifetime of the store.
* An Artifact describes a specific instance of an ArtifactType, and its properties that are written to the metadata store.
An ExecutionType describes a type of component or step in a workflow, and its runtime parameters.
* An Execution is a record of a component run or a step in an ML workflow and the runtime parameters. An execution can be thought of as an instance of an ExecutionType. Executions are recorded when you run an ML pipeline or step.
* An Event is a record of the relationship between artifacts and executions. When an execution happens, events record every artifact that was used by the execution, and every artifact that was produced. These records allow for lineage tracking throughout a workflow. By looking at all events, MLMD knows what executions happened and what artifacts were created as a result. MLMD can then recurse back from any artifact to all of its upstream inputs.
* A ContextType describes a type of conceptual group of artifacts and executions in a workflow, and its structural properties. For example: projects, pipeline runs, experiments, owners etc.
* A Context is an instance of a ContextType. It captures the shared information within the group. For example: project name, changelist commit id, experiment annotations etc. It has a user-defined unique name within its ContextType.
* An Attribution is a record of the relationship between artifacts and contexts.
* An Association is a record of the relationship between executions and contexts.
```

### Evolving Data

#### Schema Development

* Schema includes:
  * Feature name
  * Feature type: float, int, string, etc.
  * Required: True/False
  * Valency: Min, Max, etc.(features with multiple values)
  * Domain: Categorical, Numerical, Range, etc.
  * Default value
      ![alt text](image-77.png)
      ![alt text](image-78.png)
      ![alt text](image-79.png)
      ![alt text](image-80.png)
      ![alt text](image-81.png)
* Looking at schema versions to track data evolution
* Schema can drive other automated processes

#### Schema Environment

* Multiple schema versions -> Version control
* Maintraining verieties of schema

### Enterprise Data Storage

#### Feature Stores

* A feature store is a central repository for storing documented, curated and access controlled features. Feature stores are valuable centralized feature repositories that reduce redundant work. They are also valuable because they enable teams to share data and discover data that is already available
  ![alt text](image-82.png)
  ![alt text](image-83.png)
* Online v.s. Offline
  ![alt text](image-84.png)
  ![alt text](image-85.png)
* Key aspects
  * Managing feature data from a single person to large enterprises
  * Scalable and performant access to feature data in training and serving
  * Provide consistant and point-in-time correct access to feature data
  * Enable discovery, documentation, and insights into your features

#### Data Warehouse

Data warehouses are repositories that aggregate data from one or more sources

* Some attributes
  * Aggregates data source
  * Processed and analyzed
  * Read optimized
  * Not real time
  * Follows schema
* Key features
  * Subject oriented
  * Integrated
  * Not volatile (previous data is not changed)
  * Time variant
* Advantages
  * Enhanced ability to analyze data
  * Time access to data
  * Enhanced data quality and consistency
  * High return on investment
  * Increased query and system performance
* Comparison with databases
  ![alt text](image-86.png)

#### Data Lakes

A data lake is a system or repository of data stored in its natural and raw format, which is usually in the form of blobs or files.

* Comparison with datawarehouse
  ![alt text](image-87.png)

**xhu Note**

| Terminology     | Description                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Feature Store   | A central repository for storing documented, curated, and access-controlled features, specifically for ML. |
| Data Warehouse  | A subject-oriented repository for structured data optimized for fast read (system used for reporting and data analysis, and is considered a core component of business intelligence) |
| Data Lake       | A repository of data stored in its natural and raw format.                                                |

## C2W4 Advanced Labeling, Augmentation and Data Preprocessing

### Advanced Labeling

Outline:

* Semi-supervised learnig
* Active learning
* Weak supervision with Snorkel

Why?

* Manual labeling is expensive
* Unlabeled data is usually abundant and cheap
* Unlabeled data contrains useful information that can improve model

* Semi-supervised Learning
  *Label propagation
  ![alt text](image-88.png)

* Active Learning
  ![alt text](image-89.png)
  ![alt text](image-90.png)
  ![alt text](image-91.png)
  ![alt text](image-92.png)
* Weak supervision
  Weak supervision is baout leveraging higher-kevek abd/or noisier input from subject matter exports (SMSEs)
  * Unlabeled data, without ground-truth labels
  * One or more weak supervision sources
    * A list of heuristic that can automate labeling
    * Typically provided by SMEs
  * Noisy labels have certrain probability of being correct, not 100%
  * Objective: learn a generative model to determine weights of weak supervision sources
  * Snorkel
    ![alt text](image-93.png)

**xhu Note**
![alt text](image-94.png)

* Semi-supervised learning:
  * Applied the best of supervised and unsupervised approaches
  * Using a small amount of labeled data and boosts model accuracy
* Active Learning:
  * Selects the most informative data points s(for SME, e.g.human) to label
  * Improves predictive accuracy
* Weak Supervision:
  * Uses heuristics to apply noisy labels to unlabeled examples
  * Snorkel is handy frameowkr for weak supervision

### Data Augmentation

![alt text](image-95.png)

* It generates artificial data by creating new examples which are variants of the original data
* It increases the diversity and number of examples in the traning data
* Provides means to improves accuracy, generalization, and avoiding overfitting

# C3 Machine Learning Modeling Pipelines in Production

## C3W1 AutoML

### AutoML

Popular Cloud Offerings:

* Amazon SageMaker Autopilot (Database-ish. sutiabel for multiple use cases for large datasets)
  * Automatically trains and tunes the best machine learning models for classification or regression based on your data
  * Key features:
    * Quick Iteration
    * High quality models
    * Performace ranked
    * Selected features
    * Notebooks for reproducibility
  ![alt text](image-96.png)
* Microsoft Azure Automated Machine Learning
  * Quick customization: model + control settings
  * Automated Feature Engineering
  * Data Visualization
  * Intelligent stopping
  * Experiment summaries
  * Matric visualization
  * Model Interpretability
  * Pattern Discovrty
* Google Cloud AutoML
  * Accessible to beginners
  * Train High-quality models
  * Neatural Architecture Search
  * Transfer Learning
  * GUI based
  * Pipeline life-cycle
  * Data labeling
  * Data cleaning

![alt text](image-97.png)

Papers：
<https://arxiv.org/pdf/1611.01578>
<https://arxiv.org/pdf/1603.01670>
<https://arxiv.org/pdf/1808.05377>

## C3W2 Model Resource Management Techniques

### Dimentionality Reduction

Why is high-dimensional data a problem?

* More dimensions -> more features
* Risk of overfitting
* Distances grown more similar
* No clear boundaries between clusters
* Concentration phenomenon for Euclidean distance

Why are mode feautres a problem?

* Redundant / irrelevant features
* More noise added than signal
* Hard to interpret and visualize
* Hard to store and process data
![alt text](image-98.png)
![alt text](image-99.png)

Why reduce dimentionality?

* Storage
* Computational
* Consistency
* Visualization

Major techniques for dimensionality reduction

* Engineering
  * Feature Engineering
  ![alt text](image-100.png)
* Selection

Approches of conduction dimensionality reduction

* Mannually dimensionality reducton
* Algorithmic dimensionality reducton
  * Linear dimentionality reduction: project n-dimensional data into a k-dimensional subspace (k<<n)
  ![alt text](image-101.png)
    * Principal component analysis (PCA)
    ![alt text](image-102.png)
  * More dimensionality reduction algorithms
    ![alt text](image-103.png)
    * Singular value decomposition (SVD)
    * Independent component analysis (ICA)
      ![alt text](image-104.png)
    * Non-negative Matrix Factorization (NMF)

**xhu Note**
Data Science integrates all data generation, data preprocessing and data analysis (mining) techniques. Dimensionality reduction is only a preprocessing step.

1. Principal Component Analysis (PCA) on numerical data.
2. Single Value Decomposition (SVD) on image data
3. Non-negative Matrix Factorization (NMF) on text data.

### Quantization & Pruning

* Trends in adoption o smart devices
* Factors dirving this trend
  * Demands move ML capabilities from cloud to on-devices
  * Cost-effitiveness
  * Compliance with privacy regulations

![alt text](image-105.png)
![alt text](image-106.png)
![alt text](image-107.png)

#### Quantization

involves transforming a model into an equivalent representation that uses parameters and computations at a lower precision

e.g. quantizing img
![alt text](image-108.png)

Why quantize neural networks?

* Neural networks -> more parameters -> take up more space
* Shrinking model file size
* Reduce computational resources
* Make models run faster and use less power with low-precision

Benefits of quantization

* Faster compute
* Low memory bandwidth
* Low power
* Integer operations supported across CPU/DSP/NPUs
![alt text](image-110.png)

Trade-offs
![alt text](image-109.png)

* Accuracy

Post-training Quantization

Theoratically can do quantization during or after training

* Post-training quantization: a conversion technique that can reduce model size while also improving CPU and hardware accelerator latency with little degradation in model accuracy -> quantize an already trained TensorFlow model
  * Float16 is especially useful when you plan to use a GPU > best balanced?
  ![alt text](image-111.png)
  * Alternatively, consider using quantization aware training if the loss of accuracy is too great

```python
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]

tflite_quat_model = convert.convert()
```

Quantization Aware Training(QAT)

* Inserts fake quantization nodes in the forward pass
* Rewrites the graph to emulate quantized inference
* Reduce the loss of acuracy due to quantization
* Resulting model contrains all data to be quantized according to spec

![alt text](image-112.png)
![alt text](image-113.png)

```python
import tensorflow_model_optimization as tfmot

model = tf.keras.models.Sequential([
  ...
])

# Quantize the entire model
quantize_model = tfmot.quantization.keras.quantize_model(model)

# Continue with training as usual
quantize_model.compile(...)
quantize_model.fit(...)


# Quantize the parts of the model
quantize_annotate_layer = tfmot.quantization.keras.quantize_annotate_layer
model = tf.keras.models.Sequential([
  ...,
])

quantize_model = tfmot.quantization.keras.quantize_apply(model)

```

Reference
<https://blog.tensorflow.org/2020/04/quantization-aware-training-with-tensorflow-model-optimization-toolkit.html>

#### Pruning

to remove parts of the model that did not contribute substantially to producing accurate results > zeroing out insignificant (i.e. low magnitude) weights
![alt text](image-114.png)

```python
# Get the pruning method
prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude

# Compute end step to finish pruning after 2 epochs.
batch_size = 128
epochs = 2
validation_split = 0.1 # 10% of training set will be used for validation set. 

num_images = train_images.shape[0] * (1 - validation_split)
end_step = np.ceil(num_images / batch_size).astype(np.int32) * epochs

# Define pruning schedule.
pruning_params = {
      'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(initial_sparsity=0.50,
                                                               final_sparsity=0.80,
                                                               begin_step=0,
                                                               end_step=end_step)
}

# Pass in the trained baseline model
model_for_pruning = prune_low_magnitude(baseline_model, **pruning_params)

# `prune_low_magnitude` requires a recompile.
model_for_pruning.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model_for_pruning.summary()
```

Model sparsity

* Larger models -> more parameters -> more memory -> less efficient
* Sparse models -> less parameters -> less memory -> more efficient

What's special about pruning?

* Better storage and/or transmission
* Gain speedups in CPU and some ML accelerators
* Can be used in tandem with quantization to get additional benefits
* Unlock performance improvements

* The Lottery Ticket Hypothesis <https://arxiv.org/abs/1803.03635>
![alt text](image-115.png)
![alt text](image-116.png)

**xhu Note**
Although pruning can make additional benefits such as improved transmission and gains speed increases in the CPU, there are still significant limitations of this method to solve architectures on a larger scale.

## C3W2 High-Performance Models

### Distributed Training

![alt text](image-117.png)

* Types of distributed training
  * Data parallelism: In data parallelism, the model is replicated on different accelerators (GPU/CPU) and data is split between them
  ![alt text](image-118.png)
  ![alt text](image-119.png)
  * Model parallelism: When models are too large to fit on a single device then they can be divided into partitions, assigning different partitions to different acceleators

* Distribution Strategy. API e.g. tf.distribute.Strategy
  * **One Device Strategy**: This strategy is used when you want to run on a single device - no distribution. Typical usage of this strategy is testig your code on a single device before scaling to multiple devices / distribute codes.
  * **Mirrored Strategy**: This strategy is used when you want to run on multiple GPUs on one machine
    * Creates a replica per GPU <> Variables are mirrored
    * Weight updating is done using efficient cros-device communication algorithms (all-reducr algorithms)
  * **Parameter Server Strategy**: This strategy is used when you want to run on multiple machines. Some machines are designated as workers and some as parameter servers
    * Parameter servers store variables so that workers can perform computtions on them
    * Implements asynchronous data parallelism by default
  * Multi-Worker Mirrored Strategy: This strategy is used when you want to run on multiple machines with multiple GPUs on each machine
  * Central Storage Strategy
  * TPU Strategy

![alt text](image-120.png)

### High Performance Models

#### High Performance Ingestion

Why input pipelines?

Accelerators are a key part of high-performance modeling, training, and inference, but accelerators are also expensive, so it's important to use them efficiently > That means keeping them busy, which requires you to supply them with enough data fast enough.

* Full utilization of hardware resources

![alt text](image-121.png)
![alt text](image-122.png)
![alt text](image-123.png)

How to optimize pipline performance?

* Prefetching
  ![alt text](image-124.png)
* Parallelizing data extraction and transformation
  * Parallelize data extraction
    * Perfer local storage as it takes significantly less time than read data from remote storage
    * Maximize the aggregate badwidth of the remote storage by reading more files
    ![alt text](image-125.png)
  * Parallelize data transformation
    * Post data loading, the inputs may need preprocessing
    * Element-wise preprocessing can be parallelized accross CPU cores
    * The optimal value for the level of parallelism depends on:
      * Size of the data
      * Cost of the transformation
      * Number of CPU cores
    * Use tf.data.experimental.AUTOTUNE to automatically tune the level of parallelism
* Caching
  * In memory: tf.data.Dataset.cache()
  * Disk: tf.data.Dataset.cache(filename=)
  ![alt text](image-126.png)
* Reduce memory

#### High Performance Modelling

![alt text](image-127.png)
![alt text](image-128.png)
![alt text](image-129.png)
