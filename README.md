# LeArNER
<<<<<<< HEAD

## Abstract
Our proposed NER model for legal texts, LeArNER, utilizes minimal annotated data for model training to reduce expenses associated with corpus collection and training. We evaluated our model on a dataset of constitutional legal cases from Taiwan, written in traditional Chinese, and achieved an impressive F1 score of 94.88% for 13 entity types. LeArNER's performance was best achieved with a training sample of only 2000 sentences, highlighting its efficiency and potential for further legal NER research.

## Experiment

### Dataset

### Entity

#### Definitions

* ADMINISTRATIVE ACTION: Administrative activities include regulation enforcement, policy implementation, and decision-making processes related to government operations
* COUNTRY: An area of land that has its own government
* COURT: Courts in any jurisdiction
* DATE: The day, the month, and the year
* DURATION: The length of time
* LAW: Constitutions, statutes
* LEGAL CASE: Court judgments, decisions, and precedent
* LEGAL REFERENCE: Legal proverbs, resolutions of relevant meetings, and Draft Law
* PERSON: A person, including pseudonym
* PRINCIPLE: Legal principles
* PROCEDURE: Court procedures, arbitration procedures or administrative procedures.
* REGULATION: Regulation and administrative rules, including different periods of time, country's regulation
* RIGHT: Legal or fundamental rights

#### Statistics

|  Entity   | Number  |
|  ----  | ----  |
| ADMINISTRATIVE ACTION  | 279 |
| COUNTRY  | 172 |
| COURT | 320 |
| DATE  | 473 |
| DURATION | 203 |
| LAW  | 1999 |
| LEGAL CASES | 505 |
| LEGALREFERENCE  | 103 |
| PERSON | 601 |
| PRINCIPLE  | 399 |
| PROCEDURE | 461 |
| REGULATION  | 274 |
| RIGHT | 677 |

### Results

#### Performance of LeArNER on different court decisions

|  Training data   |  Test data  |  Precision  |  Recall  |  F1  |
|  ----  | ----  | ----  | ----  | ----  |
| TCC decisions 1949-2021  | TCC decisions 1949-2021  | 91.6  | 96.3  | 93.9  |
| TCC decisions 1949-2021  | The Supreme Administrative Court decisions  | 77.3  | 83.2  | 80.1  |

#### Performance of LeArNER on TCC decisions at different times

|  Training data   |  Test data  |  Precision  |  Recall  |  F1  |
|  ----  | ----  | ----  | ----  | ----  |
| 1949-2007  | 2007-2021  | 86.8  | 75.9  | 81.0  |
| 2007-2021  | 1958-2007  | 80.6  | 83.0  | 81.8  |

#### Performance of LeArNER on different pseudonym practices

|  Training data   |  Test data  |  Precision  |  Recall  |  F1  |
|  ----  | ----  | ----  | ----  | ----  |
| TCC decisions 1949-2021  | TCC decisions 1949-2021  | 91.6  | 96.3  | 93.9  |
| TCC decisions 1949-2021  | TCC decisions 2022 (All entity)  | 80.5  | 55.6  | 65.7  |
| TCC decisions 1949-2021  | TCC decisions 2022 (Pseudonym labels removed)  | 84.1  | 88.2  | 86.1  |

