## Arti fi cial Intelligence Index Report 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000000_c6ec2f8165962bd018633d07074eaf41cfb78512dd53037fa2fcdda5ff3e6b52.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000001_23acef5ec9d7e4fa2bc47b734cc808da8578bc8d91748aea27d76aedc4f31dd0.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000002_2ef37eac1d46d33cf738050ed266e05091775c5ea224676eb6a41aeb01cb00f1.png)

## Chapter 2: Technical Performance

Overview

84

Chapter Highlights

85

## 2.1 Overview of AI in 2024

87

Timeline: Signi fi cant Model and Dataset Releases

87

State of AI Performance

93

Overall Review

93

Closed vs. Open-Weight Models

94

US vs. China Technical Performance

96

Improved Performance From Smaller Models

98

Model Performance Converges at the Frontier

99

Benchmarking AI

100

## 2.2 Language

## 103

| Understanding                                        |   104 |
|------------------------------------------------------|-------|
| MMLU: Massive Multitask Language Understanding       |   104 |
| Generation                                           |   105 |
| Chatbot Arena Leaderboard                            |   105 |
| Arena-Hard-Auto                                      |   107 |
| WildBench                                            |   108 |
| Highlight: o1, o3, and Inference- Time Compute       |   110 |
| MixEval                                              |   112 |
| RAG: Retrieval Augment Generation                    |   113 |
| Berkeley Function Calling Leaderboard                |   113 |
| MTEB: Massive Text Embedding Benchmark               |   115 |
| Highlight: Evaluating Retrieval Across Long Contexts |   117 |
| 2.3 Image and Video                                  |   119 |
| Understanding                                        |   119 |

VCR: Visual Commonsense Reasoning 119

MVBench

120

Generation

122

Chatbot Arena: Vision

123

Highlight: The Rise of Video Generation

124

## 2.4 Speech

126

Speech Recognition

126

LSR2: Lip Reading Sentences 2

126

## 2.5 Coding

128

| HumanEval             |   128 |
|-----------------------|-------|
| SWE-bench             |   129 |
| BigCodeBench          |   130 |
| Chatbot Arena: Coding |   131 |

## 2.6 Mathematics

132

| GSM8K                                   |   132 |
|-----------------------------------------|-------|
| MATH                                    |   133 |
| Chatbot Arena: Math                     |   134 |
| FrontierMath                            |   134 |
| Highlight: Learning and Theorem Proving |   136 |

## 2.7 Reasoning

137

General Reasoning

137

MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI

137

GPQA: A Graduate-Level Google-Proof Q&amp;A Benchmark

138

ARC-AGI

139

Humanity's Last Exam

141

Planning

143

PlanBench

143

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000003_4ad1321e55f50d6f7d0842da3bf083125f2096368e2d323ba074c40c9428ee29.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000004_4ad1321e55f50d6f7d0842da3bf083125f2096368e2d323ba074c40c9428ee29.png)

## Chapter 2: Technical Performance (cont'd)

| 2.8 AI Agents    |   144 |
|------------------|-------|
| VisualAgentBench |   144 |
| RE-Bench         |   145 |
| GAIA             |   147 |

| 2.9 Robotics and Autonomous Motion        |   148 |
|-------------------------------------------|-------|
| Robotics                                  |   148 |
| RLBench                                   |   148 |
| Highlight: Humanoid Robotics              |   150 |
| Highlight: DeepMind's Developments        |   151 |
| Highlight: Foundation Models for Robotics |   154 |
| Self-Driving Cars                         |   155 |
| Deployment                                |   155 |
| Technical Innovations and New Benchmarks  |   156 |
| Safety Standards                          |   157 |

## ACCESS THE PUBLIC DATA

## CHAPTER 2: Technical Performance

## Overview

The Technical Performance section of this year's AI Index provides a comprehensive overview  of  AI  advancements  in  2024.  It  begins  with  a  high-level  summary  of  AI technical progress, covering major AI-related launches, the state of AI capabilities, and key trends-such as the rising performance of open-weight models, the convergence of  frontier  model  performance,  and  the  improving  quality  of  Chinese  LLMs.  The chapter then examines the current state of various AI capabilities, including language understanding and generation, retrieval-augmented generation, coding, mathematics, reasoning, computer vision, speech, and agentic AI. New this year are signi fi cantly expanded analyses of performance trends in robotics and self-driving cars.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000005_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000006_3b940fee27103d3a632f077cd979b46b173072d478a9956145bcc95f477ee6d6.png)

## Chapter Highlights

1.  AI  masters  new  benchmarks  faster  than  ever. In  2023,  AI  researchers  introduced  several  challenging  new benchmarks, including MMMU, GPQA, and SWE-bench, aimed at testing the limits of increasingly capable AI systems. By 2024, AI performance on these benchmarks saw remarkable improvements, with gains of 18.8 and 48.9 percentage points on MMMU and GPQA, respectively. On SWE-bench, AI systems could solve just 4.4% of coding problems in 2023-a fi gure that jumped to 71.7% in 2024.
2. Open-weight models catch up. Last year's AI Index revealed that leading open-weight models lagged signi fi cantly behind their closed-weight counterparts. By 2024, this gap had nearly disappeared. In early January 2024, the leading closedweight model outperformed the top open-weight model by 8.04% on the Chatbot Arena Leaderboard. By February 2025, this gap had narrowed to 1.70%.
3. The gap between Chinese and US models closes. In 2023, leading American models signi fi cantly outperformed their Chinese counterparts-a trend that no longer holds. At the end of 2023, performance gaps on benchmarks such as MMLU, MMMU, MATH, and HumanEval were 17.5, 13.5, 24.3, and 31.6 percentage points, respectively. By the end of 2024, these di ff erences had narrowed substantially to just 0.3, 8.1, 1.6, and 3.7 percentage points.
4. AI model performance converges at the frontier. According to last year's AI Index, the Elo score di ff erence between the top and 10th-ranked model on the Chatbot Arena Leaderboard was 11.9%. By early 2025, this gap had narrowed to just 5.4%. Likewise, the di ff erence between the top two models shrank from 4.9% in 2023 to just 0.7% in 2024. The AI landscape is becoming increasingly competitive, with high-quality models now available from a growing number of developers.
5. New reasoning paradigms like test-time compute improve model performance. In 2024, OpenAI introduced models like o1 and o3 that are designed to iteratively reason through their outputs. This test-time compute approach dramatically improved performance, with o1 scoring 74.4% on an International Mathematical Olympiad qualifying exam, compared to GPT4o's 9.3%. However, this enhanced reasoning comes at a cost: o1 is nearly six times more expensive and 30 times slower than GPT-4o.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000007_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000008_3b940fee27103d3a632f077cd979b46b173072d478a9956145bcc95f477ee6d6.png)

## Chapter Highlights (cont'd)

6. More challenging benchmarks are continually proposed. The saturation of traditional AI benchmarks like MMLU, GSM8K, and HumanEval, coupled with improved performance on newer, more challenging benchmarks such as MMMU and GPQA, has pushed researchers to explore additional evaluation methods for leading AI systems. Notable among these are Humanity's Last Exam, a rigorous academic test where the top system scores just 8.80%; FrontierMath, a complex mathematics benchmark where AI systems solve only 2% of problems; and BigCodeBench, a coding benchmark where AI systems achieve a 35.5% success rate-well below the human standard of 97%.

7. High-quality AI video generators demonstrate signi fi cant improvement. In 2024, several advanced AI models capable of generating high-quality videos from text inputs were launched. Notable releases include OpenAI's SORA, Stable Video 3D and 4D, Meta's Movie Gen, and Google DeepMind's Veo 2. These models produce videos of signi fi cantly higher quality compared to those from 2023.

8. Smaller models drive stronger performance. In 2022, the smallest model registering a score higher than 60% on MMLU was PaLM, with 540 billion parameters. By 2024, Microsoft's Phi-3-mini, with just 3.8 billion parameters, achieved the same threshold. This represents a 142-fold reduction in over two years.
9.  Complex  reasoning  remains  a  problem. Even  though  the  addition  of  mechanisms  such  as  chain-of-thought reasoning has signi fi cantly improved the performance of LLMs, these systems still cannot reliably solve problems for which provably correct solutions can be found using logical reasoning, such as arithmetic and planning, especially on instances larger than those they were trained on. This has a signi fi cant impact on the trustworthiness of these systems and their suitability in high-risk applications.
10. AI agents show early promise. The launch of RE-Bench in 2024 introduced a rigorous benchmark for evaluating complex tasks for AI agents. In short time-horizon settings (two-hour budget), top AI systems score four times higher than human experts, but as the time budget increases, human performance surpasses AI-outscoring it two to one at 32 hours. AI agents already match human expertise in select tasks, such as writing Triton kernels, while delivering results faster and at lower costs.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000009_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

The Technical Performance chapter begins with a highlevel overview of signi fi cant model releases in 2024 and reviews the current state of AI technical performance.

## 2.1 Overview of AI in 2024

## Timeline: Signi fi cant Model and Dataset Releases

As chosen by the AI Index Steering Committee, here are some of the most notable model and dataset releases of 2024.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000010_f5246e7a20aa044a9a46e509194fe97072abf7307be723bd179eba1d0ce16ebe.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000011_d00b65d99d76b2a01372ee00951f30c07b025976a1b490ee536f3617c09c53d1.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000012_5989602349b78220553134545e5adb40e7f7dfb55f8048d28340b6dbc76a0ba3.png)

| Date         | Name           | Category       | Creator(s)                                                          | Signi fi cance                                                                                                                                                                                                                                                                                                         | Image                                   |
|--------------|----------------|----------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Jan 19, 2024 | Stable LM 2    | LLM            | Stability AI                                                        | Stability's latest language model builds on the original Stable LM, o ff ering enhanced performance. With only 1.6 billion parameters, it is designed to run e ffi ciently on portable devices such as laptops and smartphones.                                                                                        | Figure 2.1.1 Source: Wikipedia, 2025    |
| Feb 8, 2024  | Aya Dataset    | Dataset        | Cohere for AI, Beijing Academy of AI, Cohere, Binghamton University | Acollection of 513 million prompt- completion pairs spanning 114 languages, released as part of Cohere's Aya initiative. This paper and its accompanying dataset represent signi fi cant milestones in multilingual instruction tuning.                                                                                | Figure 2.1.2 Source: Cohere, 2025       |
| Feb 15, 2024 | Gemini 1.5 Pro | LLM            | Google DeepMind                                                     | Google's Gemini model set a new benchmark with its 1M token context window, far exceeding GPT-4 Turbo's 128K token limit.                                                                                                                                                                                              | Figure 2.1.3 Source: Google, 2024       |
| Feb 20, 2024 | SDXL-Lightning | Text-to- image | ByteDance                                                           | Developed by ByteDance, the creators of TikTok, this model was among the fastest text-to-image systems at its release, generating high-quality synthetic images in under a second. Its speed was achieved through progressive adversarial distillation, unlike other models that rely on di ff usion-based techniques. | Figure 2.1.4 Source: Hugging Face, 2025 |
| Mar 4, 2024  | Claude 3       | LLM            | Anthropic                                                           | Anthropic's latest LLM outperforms GPT-4 and Gemini on nearly all industry benchmarks, reduces incorrect prompt refusals, and delivers signi fi cantly higher accuracy.                                                                                                                                                | Figure 2.1.5 Source: Anthropic, 2025    |

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000013_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000014_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

2.1 Overview of AI in 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000015_1f72b3dfa9ef0634cf049fcf124288a333b3d888b52343d782243d9d64d670f9.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000016_55f2ded0b482612ce9eb93c12506b605f33b213de638fb3c3b0dce55d9ff5e01.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000017_2b6a733d373b855040b86c093075c2b437dc890661dbeb5c27c7b470b80b63c5.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000018_282c37d97040e21751d4c224b4621acd9e296253b28577aaf14e33c03d358275.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000019_a68dcd40710aa8f7fd9eda42aefb4ba7b25c8ebfec0ffd04169911ef8ebd28cc.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000020_f90ba0f34660711dbffb675fca766245d28de6ceb986a8cae82856d28bba88c9.png)

| Mar 7, 2024   | In fl ection-2.5   | LLM                             | In fl ection AI   | In fl ection's fl agship product, 'Pi,' featured an exceptional model with GPT-4-level performance while using only 40% of its computing resources. Just two weeks after the model's release, Microsoft acquired In fl ection for $650 million.                       | Figure 2.1.6 Source: In fl ection, 2025   |
|---------------|--------------------|---------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Mar 19, 2024  | Moirai and LOTSA   | Model/ dataset                  | Salesforce        | Salesforce unveils Moirai, a foundation model for universal forecasting, alongside LOTSA-a diverse, large- scale time series dataset with 27 billion observations spanning nine domains.                                                                              | Figure 2.1.7 Source: Salesforce, 2025     |
| Mar 27, 2024  | DBRX               | LLM                             | Databricks        | Databricks' open-source mixture-of- experts (MoE) LLM is a fi ne-grained model, surpassing similar small MoE models like Mixtral and Grok. This transformer decoder-only model features 132B parameters (36B active per input) and was trained on 12 trillion tokens. | Figure 2.1.8 Source: Databricks, 2025     |
| Apr 2, 2024   | Stable Audio 2     | Text-to- song and song-to- song | Stability AI      | The latest version of Stable Audio, Stability's AI-powered song generator, now supports audio-to-audio functionality. Users can upload songs and manipulate them using natural language prompts for seamless customization.                                           | Figure 2.1.9 Source: Stability AI, 2025   |
| Apr 17, 2024  | Llama 3            | LLM                             | Meta              | The Llama 3 series debuts with 8B and 70B parameter text-based models, ranking among the highest performing models of their size to date.                                                                                                                             | Figure 2.1.10 Source: Meta, 2025          |
| May 13, 2024  | GPT-4o             | Multimodal                      | OpenAI            | GPT-4o is a new multimodal model capable of processing inputs in any combination of text, audio, images, and video, and generating outputs in the same formats. It responds to audio in as little as 320 milliseconds, matching human response times.                 | Figure 2.1.11 Source: OpenAI, 2024        |

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000021_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

2.1 Overview of AI in 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000022_9c4dd07165d030b80f117094d506041ab42c0f897ad0d4fb98e6a427480d2274.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000023_f1b03aa5c9874e5d2d52e3f544ad415ebb7039590ff79497a9dfa81459e7ced8.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000024_8d5cf9fd17223b47d503c687084df850ecddc13d1243b3935f5c63ff7784c4e4.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000025_b9ce294a94df05f621888cf4228838b2ebe0c16d83895250531ac8a8b4bfc75b.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000026_adafa1c4182c24c67b53a2c77c84c2525818121f22d6689b1dec081ce45238f5.png)

| Jun 7, 2024   | Qwen2          | LLM                                | Alibaba                                      | Qwen2, developed by China's Alibaba, is a series of advanced base and instruction-tuned models. These models rival competitors like Llama 3-70B and Mixtral-8x22B in performance across numerous benchmarks.                                                                                  | Figure 2.1.12 Source: Qwen, 2024         |
|---------------|----------------|------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| Jun 17, 2024  | Runway Gen-3   | Text-to- video and image-to- video | Runway                                       | Runway's upgraded video generation model sets a new standard for the fi eld, particularly excelling in creating photorealistic humans with vivid and expressive emotionality.                                                                                                                 | Figure 2.1.13 Source: Runway, 2024       |
| Jul 23, 2024  | Llama 3.1 405B | LLM                                | Meta                                         | Meta has released its largest model to date, the fi nal in the Llama 3.1 family, featuring 405B parameters. Upon its release, it became the most capable openly available foundation model, rivaling many closed models across a variety of benchmarks.                                       | Figure 2.1.14 Source: Meta, 2024         |
| Aug 12, 2024  | Falcon Mamba   | LLM                                | Technology Innovation Institute in Abu Dhabi | Apowerful new 7B parameter model, built on the Mamba State Space Language Model (SSLM) architecture, enables Falcon-one of the few government-created AI models-to dynamically adjust parameters and fi lter out irrelevant inputs, making it more e ffi cient than transformer-based models. | Figure 2.1.15 Source: Hugging Face, 2025 |
| Aug 13, 2024  | Grok-2         | Text-to-text and text-to- image    | xAI                                          | Developed by xAI, Grok is an advanced text- and image-generation model that excels in image creation, advanced reasoning, and problem-solving. Its launch was particularly notable, as it quickly rivaled the performance of leading models despite xAI being founded only in March 2023.     | Figure 2.1.16 Source: xAI, 2025          |

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000027_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## 2.1 Overview of AI in 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000028_d033c6f307ad8101d77b7d0d4bcf124b554e5e9e58011ffc683c2e3e6b55cc8f.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000029_cb45a2268e9e83659ff2b23b4bd1426ea79ad2f730310562f1cba0aa40efae2f.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000030_828edf083268e5e1823101122dd0831fe92bd437c8252a35b7346c13522aecd4.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000031_23aeccd30d4f59fbfbff62f756f9a140cc7b489e9f635478e389f23ab24f6df2.png)

| Aug 15, 2024   | Imagen 3                | Text-to- image          | Google Labs   | Google's updated AI image generator achieves the highest Elo score on the GenAI-Bench image benchmark, setting a new standard for quality in AI- generated visuals.                                                                            | Figure 2.1.17 Source: Google, 2025   |
|----------------|-------------------------|-------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Aug 22, 2024   | Jamba 1.5               | LLM                     | AI21 Labs     | The fi rst LLM to combine state-space models with transformers, delivering high-quality results for text-based applications. This hybrid approach signi fi cantly enhances speed while preserving the quality of outputs.                      | Figure 2.1.18                        |
| Aug 29, 2024   | SynthID v2              | Tool                    | Google        | SynthID v2 is the updated version of SynthID, Google's watermarking and identi fi cation software. It now supports AI-generated content across images, video, audio, and text, and o ff ers enhanced tracking and veri fi cation capabilities. | Figure 2.1.19 Source: Google, 2025   |
| Sep 11, 2024   | NotebookLM Podcast Tool | Text-to- podcast        | Google Labs   | The second end-to-end AI podcast generator to hit the market, following Synthpod, went viral. It gained popularity among students leveraging NotebookLM for studying and tech employees using it to listen to AI-generated summaries.          | Figure 2.1.20 Source: Google, 2025   |
| Sep 12, 2024   | o1-preview              | Language, math, biology | OpenAI        | OpenAI's fi rst model in the 'o series' is designed for advanced reasoning and tackling complex tasks. It is signi fi cantly more powerful than GPT, particularly in math, science, and coding.                                                | Figure 2.1.21 Source: OpenAI, 2025   |
| Sep 17, 2024   | NVLM (D, H, X)          | Vision, language        | Nvidia        | Nvidia released three open-access models for vision-language tasks, achieving top scores on OCRBench (for optical character recognition) and VQAv2 (for natural language understanding).                                                       | Figure 2.1.22                        |

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000032_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## 2.1 Overview of AI in 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000033_33f84e8dbc729cca45b883ddb8606d2277db1e982c52f543e6d60847b89c622b.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000034_6929928315009565f3628f975c73eee1065d91c7dbbcfa908420e1a8eef2ae41.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000035_9e601eedc27934044fe4b22c00d84ce4dc6960a6da9519eb85095e459aad9cf9.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000036_9db7b0f9a325f9b40be4a9bc5cf8b88c40657e22a42d7b779aaafa611bd63a27.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000037_3a392eaa730699b118fa670c38b79441daef5015a88f2825757615d2f4dbb303.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000038_a73a1197549c438773daf91fc7d16b23172340fba504f16f89bac6f097b5e74a.png)

| Sep 19, 2024   | Qwen2.5                | LLM                | Alibaba         | Qwen2.5, the latest series of foundation models from Chinese e-commerce giant Alibaba, includes a range of e ffi cient smaller models and specialized coding and math models designed for targeted functionality.                                     | Figure 2.1.23 Source: Qwen, 2025    |
|----------------|------------------------|--------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Oct 16, 2024   | Ministral              | LLM                | Mistral         | Ministral is a pair of compact models (3B and 8B parameters) that outperformed Gemma and Llama models of similar size across all major industry-recognized benchmarks.                                                                                | Figure 2.1.24 Source: Mistral, 2025 |
| Oct 22, 2024   | Anthropic Computer Use | Agentic Capability | Anthropic       | Anthropic Computer Use is a groundbreaking computer control feature for Claude 3.5 Sonnet users, allowing Claude to move the cursor, type, and autonomously complete tasks on the user's computer in real time.                                       | Figure 2.1.25                       |
| Oct 28, 2024   | Apple Intelligence     | iPhone feature     | Apple           | Apple's suite of AI-powered features includes Image Playground (for image creation), Genmoji (for custom emoji creation), Siri integration with ChatGPT, and more.                                                                                    | Figure 2.1.26 Source: Apple, 2025   |
| Dec 3, 2024    | Nova Pro               | Multimodal         | Amazon          | Nova Pro is the most powerful model in Amazon Web Services' Nova family, capable of processing both visual and textual information. It especially excels at analyzing fi nancial documents.                                                           | Figure 2.1.27 Source: Amazon, 2025  |
| Dec 11, 2024   | Gemini 2               | LLM                | Google DeepMind | The improved version of Gemini, Google's LLM, now includes computer control along with image and audio generation capabilities. It is twice as fast as Gemini 1.5 Pro and o ff ers signi fi cantly enhanced performance in coding and image analysis. | Figure 2.1.28 Source: Google, 2025  |

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000039_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## 2.1 Overview of AI in 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000040_f5ca267d28e6264fb93a48f2fb203b356173102309163dfddd63b90e9807493c.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000041_749b5996b305814a5bd6607384e2aa093420797d122d6be8f53f9e93ec1dc971.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000042_f2498d1b2913b38b80872b10e31b65f468d987163a0c5604ff427b4774faccd7.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000043_3a4405b9945d4bf3d8da8932fa9846d507d8fcfcaf20b4d76ca2996b193112cd.png)

| Dec 12, 2024   | Sora        | Text-to- video   | OpenAI   | OpenAI's highly anticipated video generation model can create videos up to 20 seconds long at 1080p resolution for ChatGPT Pro users (and fi ve seconds at 720p for ChatGPT Plus users). Sora demos had been circulating at tech meetups since early 2024, but OpenAI delayed the o ffi cial release to improve model safety.              | Figure 2.1.29 Source: OpenAI, 2025       |
|----------------|-------------|------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| Dec 13, 2024   | GlobalMMLU  | Dataset          | Cohere   | Amultilingual evaluation set featuring professionally translatedMMLU questions across 42 languages, designed to serve as a more global AI benchmark. It evaluates AI performance in diverse languages while addressing Western biases in the original MMLUdataset, where an estimated 28% of questions rely on Western cultural knowledge. | Figure 2.1.30 Source: Singh et al., 2025 |
| Dec 20, 2024   | o3 (beta)   | Multimodal       | OpenAI   | OpenAI's newest frontier model, released for safety testing by AI researchers, outperforms all previous models in SWE, competition code, competition math, PhD-level science, and research math benchmarks. It also set a new record on the ARC-AGI benchmark, achieving 87.5% on theARC Prize team's private holdout set.                 | Figure 2.1.31 Source: VentureBeat, 2025  |
| Dec 27, 2024   | DeepSeek-V3 | LLM              | DeepSeek | DeepSeek V3, an open-source model developed with signi fi cantly fewer computing resources than state-of-the- art models, outperforms leading models on benchmarks like MMLUand GPQA.                                                                                                                                                      | Figure 2.1.32 Source: Dirox, 2025        |

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## State of AI Performance

In this section, the AI Index o ff ers a high-level view into major AI trends that occurred in 2024.

## Overall Review

Last year's AI Index highlighted that AI had already surpassed human  performance  across  many  tasks,  with  only  a  few exceptions, such as competition-level mathematics and visual commonsense  reasoning.  Over  the  past  year,  AI  systems have continued to improve, exceeding human performance on several of these previously challenging benchmarks.

Figure  2.1.33  illustrates  the  progress  of  AI  systems  relative to human baselines for eight AI benchmarks corresponding to  11  tasks  (e.g.,  image  classi fi cation  or  basic-level  reading comprehension). 1   The AI Index team selected one benchmark to represent each task. This year, the AI Index team added newly  released  benchmarks,  such  as  GPQA  Diamond  and MMMU, to showcase the progress of AI systems in tackling extremely challenging cognitive tasks.

## Select AI Index technical performance benchmarks vs. human performance

Source: AI Index, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000044_4d6af4e2e6211ca75d469264b4965f608563238477db9ff4552b8b45e0a26a99.png)

Figure 2.1.33 2

1  An AI benchmark is a standardized test used to evaluate the performance and capabilities of AI systems on speci fi c tasks. For example, ImageNet is a canonical AI benchmark that features a large collection of labeled images, and AI systems are tasked with classifying these images accurately. Tracking progress on benchmarks has been a standard way for the AI community to monitor the advancement of AI systems.

2 In Figure 2.1.33, the values are scaled to establish a standard metric for comparing di ff erent benchmarks. The scaling function is calibrated such that the performance of the best model for each year is measured as a percentage of the human baseline for a given task. A value of 105% indicates, for example, that a model performs 5% better than the human baseline

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000045_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

As of 2024, there are very few task categories where human ability surpasses AI. Even in these areas, the performance gap between AI and humans is shrinking rapidly. For example, on MATH,  a  benchmark  for  competition-level  mathematics, state-of-the-art  AI  systems  are  now  7.9  percentage  points ahead  of  human  performance,  a  signi fi cant  improvement from  the  0.3-point  gap  in  2024. 3   Similarly,  on  MMMU,  a benchmark for complex, multidisciplinary, expert-level questions, the best 2024 model, o1, scored 78.2%, only 4.4 points  below the  human  benchmark  of  82.6%.  Conversely, at  the  end  of  2023,  Google  Gemini  scored  59.4%,  further illustrating  the  rapid  advancements  in  AI  performance  on cognitively demanding tasks.

## Closed vs. Open-Weight Models

AI models can be released with di ff erent levels of openness. Certain models, like Google's Med-Gemini, remain entirely closed,  accessible  only  to  their  developers.  Meanwhile, models such as OpenAI's GPT-4o and Anthropic's Claude 3.5 provide limited public access through APIs. However, weights for these models are not released, preventing independent modi fi cation or thorough public scrutiny. In contrast, weights for Meta's Llama 3.3 and Stable Video 4D are fully available, allowing anyone to modify and use them freely. 4

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000046_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Last year's AI Index highlighted a notable performance gap between closed and open-weight LLM models. Figure 2.1.34 illustrates the performance trends of the top closed-weight and open-weight LLMs on the Chatbot Arena Leaderboard, a  public  platform  for  benchmarking  LLM  performance. In  early  January  2024,  the  leading  closed-weight  model outperformed  the  top  open-weight  model  by  8.0%.  By February 2025, this gap had narrowed to 1.7%.

The same trend is evident across other question-answering benchmarks.  In  2023,  closed-weight  models  consistently outperformed  open-weight  counterparts  on  nearly  every major benchmark-MMLU, HumanEval, MMMU, and MATH. However, by 2024, the gap had narrowed signi fi cantly (Figure 2.1.35). For instance, in late 2023, closed-weight models led open  models  on  MMLU  by  15.9  points,  but  by  the  end  of 2024, that di ff erence had shrunk to just 0.1 percentage point. This rapid improvement was largely driven by Meta's summer release  of  Llama  3.1,  followed  by the  launch  of  other  highperforming open-weight models, such as DeepSeek's V3.

Perspectives  on  open  versus  closed-weight  AI  models  are sharply divided. Advocates of open-weight models highlight their potential to reduce market monopolies, spur innovation, improve security and robustness, and enhance transparency within the AI ecosystem. For example, Meta's Llama models have  been  leveraged  to  create  tools  like  Meditron,  power military applications, and drive the development of numerous open-weight models worldwide. However, critics warn that open-weight models pose signi fi cant security risks, including the spread of disinformation and the creation of bioweapons, arguing for a more cautious and controlled approach.

3 The benchmark data in this fi gure, along with those in other sections of this chapter, was collected in early January 2025. Since the publication of the AI Index, individual benchmark scores may have improved.

4 In the software community, 'open source' refers to software released under a license that grants users the right to use, study, modify, and distribute both the software and its source code freely. Open-weight models, though more accessible than closed-weight models, are not necessarily fully open source , as the underlying code or training data is often withheld.

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Performance of top closed vs. open models on LMSYS Chatbot Arena

Source: LMSYS, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000047_7ec069de31bff9eab114c29e9139c8169168e8c339bc08c40f2699b277b6c84e.png)

Figure 2.1.34

## Performance of top closed vs. open models on select benchmarks

Source: AI Index, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000048_66f9a47dde8549187c5c2b0d9403669f697237f6b8a0c12cca1f8a64580c93c7.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000049_526bdab64a6b74e62134301d0e7a1b25db40babfabe97dcdeb30481bb817ed49.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000050_454d6ad494d4073fc2260225706c6c60b411ea9d91330e48b322a90bed732e53.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000051_99f921b4cebec7471ac6a9ceb7103de38331817aafb3f9ce30bd05f2b6c447a8.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000052_564a1c4f91a1bb2611abee644ea1c4e15cbd19904ac74b1c0ace04d8301aca95.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000053_2f80ecc35d33ecf55380422de83f565128c12fb4693eee9a739aee98cec21bdc.png)

Figure 2.1.35

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## US vs. China Technical Performance

The United States has historically dominated AI research and model development, with China consistently ranking second. Recent evidence, however, suggests the landscape is rapidly changing and that China-based models are catching up to their U.S. counterparts.

In 2023, leading American models signi fi cantly outperformed their  Chinese counterparts. On the LMSYS Chatbot Arena, the  top  U.S.  model  outperformed  the  best  Chinese  model by  9.3%  in  January  2024.  By  February  2025,  this  gap  had narrowed  to  just  1.7%  (Figure  2.1.36).  At  the  end  of  2023, on  benchmarks  such  as  MMLU,  MMMU,  MATH,  and HumanEval, the performance gaps were 17.5, 13.5, 24.3, and 31.6  percentage  points,  respectively  (Figure  2.1.37).  By  the end  of  2024,  these  di ff erences  had  narrowed  signi fi cantly to  just  0.3,  8.1,  1.6,  and  3.7  percentage  points.  The  launch of DeepSeek-R1 garnered attention for another reason: The company reported achieving its results using only a fraction of the hardware resources typically required to train such a model.  Beyond  impacting  U.S.  stock  markets,  DeepSeek's R1  launch  raised  doubts  about  the  e ff ectiveness  of  U.S. semiconductor export controls.

## Performance of top United States vs. Chinese models on LMSYS Chatbot Arena

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000054_84140217978f48772e5bdfe002883f421e3206ff8970ef868a15ee117ec301e7.png)

Figure 2.1.36

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000055_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Performance of top United States vs. Chinese models on select benchmarks

Source: AI Index, 2025 | Chart: 2025 AI Index report

United States

China

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000056_c7f4785ad5dbec304e8dad777b2b1e286fa9f83cbcb6337e084139c585a5b9b7.png)

100%

Mathematical reasoning: MATH

80%

60%

40%

20%

0%

Accuracy

2022

2023

2024

Overall accuracy

Pass@1

100%

80%

60%

40%

20%

0%

100%

80%

60%

40%

20%

0%

2022

2022

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000057_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

General reasoning: MMMU

2023

Coding: HumanEval

2023

2024

2024

Figure 2.1.37

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Improved Performance From Smaller Models

Recent  AI  progress  has  been  driven  by  scaling-the  idea that increasing model  size and  training data  improves performance.  While  scaling  has  signi fi cantly  boosted  AI capabilities,  a  notable  recent  trend  is  the  emergence  of smaller high-performing models. Figure 2.1.38 illustrates the reduction in size of the smallest model that scores above 60% on  MMLU, a widely used language model benchmark. For context, early models powering ChatGPT, such as GPT-3.5 Turbo, scored around 70% on MMLU. In 2022, the smallest model surpassing 60% on MMLU was PaLM, with 540 billion parameters.  By  2024,  Microsoft's  Phi-3  Mini,  with  just  3.8 billion parameters, achieved the same threshold, marking a 142-fold reduction in model size over two years.

2024 was a breakthrough year for smaller AI models. Nearly every major AI developer released compact, high-performing models, including GPT-4o mini, o1-mini, Gemini 2.0 Flash, Llama 3.1 8B, and Mistral Small 3. 5  The rise of small models is signi fi cant for several reasons. It demonstrates increasing algorithmic e ffi ciency, allowing developers to achieve more with  less  data  and  at  lower  training  cost.  These  e ffi ciency gains, combined  with  growing  datasets,  could  lead  to even  higher-performing  models.  Additionally,  inference  on smaller  models  is  typically  faster  and  less  expensive.  Their emergence also lowers the barrier to entry for AI developers and businesses looking to integrate AI into their operations.

## Smallest AI models scoring above 60% on MMLU, 2022-24

Source: Abdin et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000058_1aea03733f83f3b33972c93a10e7a8783851f34f4231be1df6a86908b6dfb1fd.png)

Publication date

Figure 2.1.38

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000059_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Model Performance Converges at the Frontier

In  recent  years,  AI  model  performance  at  the  frontier  has converged,  with  multiple  providers  now  o ff ering highly capable  models.  This  marks  a  shift  from  late  2022,  when ChatGPT's launch-widely seen as AI's breakthrough into  public  consciousness-coincided  with  a  landscape dominated by just two major players: OpenAI and Google. OpenAI,  founded  in  2015,  released  GPT-3  in  2020,  while Google introduced models like PaLM and Chinchilla in 2022.

Since then,  new  players  have  entered the  scene,  including Meta with its Llama models, Anthropic with Claude, High-

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000060_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Flyer's  DeepSeek,  Mistral's  Le  Chat,  and  xAI  with  Grok. As  competition  has  intensi fi ed,  model  performance  has increasingly converged (Figure 2.1.39). According to last year's AI  Index,  the  performance  gap  between  the  highest-  and 10th-ranked models on the Chatbot Arena Leaderboard-a widely used AI ranking platform-was 11.9%. By early 2025, it had narrowed to 5.4%. Similarly, the di ff erence between the top two models fell from 4.9% in 2023 to just 0.7% in 2024. The AI landscape is becoming more competitive, validating 2023  predictions  that  AI  companies  lack  a  technological moat to shield them from rivals.

## Performance of top models on LMSYS Chatbot Arena by select providers

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000061_fe5b1297cd53d7bcc0f5e974855abd7b6f4d73518d438efd059d1e96bad33f30.png)

Figure 2.1.39

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Benchmarking AI

For years, the AI Index has used benchmarks to monitor the technical progress of AI systems over time. While benchmarks remain a key tool in this e ff ort, it is important to acknowledge their  limitations  and  guide  the  community  toward  more e ff ective benchmarking practices.

As noted in last  year's  AI  Index,  many  prominent  AI  benchmarks are reaching saturation. With AI systems advancing rapidly, even newly designed, more challenging tests often  remain relevant for only a few years. Some experts suggest that the era of new academic benchmarks may be coming to an end. To truly assess the capabilities of AI systems, more rigorous and comprehensive evaluations are needed.

Additionally, when model developers release new models, they typically report benchmark scores, which are often accepted at face value by the broader community. However, this approach has fl aws. In some  cases, companies  use nonstandard prompting techniques, making model-to-model comparisons unreliable. For example, when Google launched Gemini Ultra, it  reported  an  MMLU  benchmark  score  using  a  chain-ofthought  prompting  technique  that  other  developers  did  not use.  Additionally,  third-party  researchers  have  documented cases  where  models  perform  worse  in  independent  testing compared with the results fi rst reported by their developers.

There are  critical  aspects  of  intelligence  that  do  not  easily lend themselves to benchmarking. Benchmarks are e ff ective for  evaluating  certain  intelligent  capabilities,  such  as vision and language, where tasks are discrete-e.g., classifying an image  correctly  or  answering  a  multiple-choice  question. However,  developing  benchmarks  is  more  challenging  in areas  of  AI  such  as  multi-agent  systems  and  human-AI interaction  because  of  factors  including  the  variability  in human behaviors and the sheer diversity of correct answers.

In addition, AI advances have traditionally been evaluated in competitions designed to measure human performance, such as  games  and  other  open  challenges  posed  to  humans  or machines. Games such as chess and poker involve signi fi cant

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000062_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

intelligence, and AI systems have improved over the decades to  the  point  of  defeating  the  best  humans  at  increasingly complex games. Games with a physical component or team capabilities are also a good measure of progress for AI, and the robotics community has embarked on challenging game competitions  such  as  RoboCup  for  soccer-playing  robots. Another  area  of  AI  where  competitions  are  used  involves coordination  and  teamwork  where  multi-agent  systems demonstrate advances in distributed reasoning.

Benchmarks  have  been  developed  by  the  AI  community for  a  very  long  time.  Signi fi cant  advances  in AI  have  been possible  because  di ff erent  approaches  and  methods  could be  evaluated  against  the  same  gold  standard  represented by  a  benchmark.  In  machine  learning,  benchmarks  with di ff erent  kinds  of  data  in  diverse  domains  have  enabled signi fi cant advances. Many of these benchmarks are evaluated automatically by a third party without releasing the test data to the AI developers, which makes the evaluations more  trustworthy. One  interesting recent  trend is that various benchmark tasks are addressed by the same model. For  example,  natural  language  was  addressed  for  many years as a collection of separate tasks (e.g., understanding, generation, question answering), each with its own models and each with its own benchmarks. Similarly, speech tasks were benchmarked separately from language understanding or  generation  tasks.  Today,  the  same  model  can  address all  language tasks,  and,  in  some  cases,  a  single  model  can address  language,  images,  and  multimodal  tasks.  This  is  a very  important  AI  advance  concerning  the  integration  of otherwise separate intelligent tasks and capabilities.

The rapid progress of AI systems, evidenced by their consistent outperformance  on  benchmarks,  is  perhaps  best  illustrated by  the  diminishing  relevance  of  the  well-known  and  longstanding challenge for AI: the Turing test. Originally proposed in  Alan  Turing's  1950  paper  'Computing  Machinery  and Intelligence,' the test evaluates a machine's ability to exhibit humanlike intelligence. In it, a human judge engages in a textbased conversation with both a machine and a human; if the

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

judge cannot reliably distinguish between them, the machine is  said  to  have  passed  the  Turing  test.  Recent  evidence suggests that LLMs have advanced so signi fi cantly that people struggle to di ff erentiate the best-performing language models from a human, signaling that modern AI models can pass the Turing test. While the merits and shortfalls of this test have long  been  debated,  it  remains  an  important  historical  and cultural benchmark for machine intelligence. The questioning of its relevance highlights the remarkable progress of LLMs in recent years and the evolving perception of e ff ective computer science benchmarks and AI measurement.

In robotics, many  models have emerged  that address interacting with the physical world and reasoning about natural laws. A number of robotics benchmarks, such as ARMBench, focus on perception tasks. However, other benchmarks, such as  VIMA-Bench,  assess  robot  performance  in  simulated environments where they simultaneously incorporate perception, communication, and deep learning.

Benchmarks can also su ff er from contamination, where LLMs encounter test  questions that were  present  in their training data. A recent study by Scale found signi fi cant contamination in  the  performance  of  many  LLMs  on  GSM8K,  a  widely used mathematics benchmark. Some researchers have sought to combat these contamination issues by introducing benchmarks like LiveBench, which are periodically updated

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000063_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

with  new  questions  from  unfamiliar  sources  that  LLMs  are unlikely to have seen in their training data.

Lastly, research has shown that many benchmarks are poorly constructed. In BetterBench, researchers systematically analyzed 24 prominent benchmarks and identi fi ed systemic de fi ciencies: 14 failed to report statistical signi fi cance, 17 lacked scripts for result replication, and most su ff ered from inadequate documentation, limiting their reproducibility and e ff ectiveness in evaluating models. Despite widespread use, benchmarks like MMLU demonstrated poor adherence to quality standards, while others, such as GPQA, performed signi fi cantly better. To address these issues, the paper proposed a 46-criteria framework covering all phases of benchmark development-design, implementation, documentation, and maintenance (Figure 2.1.40). It also introduced a publicly accessible repository to enable continuous updates and improve benchmark comparability. Figure 2.1.41, from BetterBench, assesses many prominent benchmarks on their usability and design. These fi ndings underscore the need for standardized benchmarking to ensure reliable AI evaluation and to prevent misleading conclusions about model performance. Benchmarks have the potential to shape policy decisions and in fl uence procurement decisions within organizations highlighting the importance of consistency and rigor in evaluation.

## Five stages of the benchmark lifecycle

Source: Reuel et al., 2024

## RETIREMENT

Figure 2.1.40

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000064_addc6cbffd9e43493b488d9e94e25d7ef12f2ea09e26a7c58dc465806d83e7f8.png)

## Chapter 2: Technical Performance

2.1 Overview of AI in 2024

## Design vs. usability scores across select benchmarks

Source: Reuel et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000065_8d545f981b576e23cb3ef77aafd49d1917645bb311dede5e83052dfc1a5476c7.png)

In this chapter, the AI Index continues to report on benchmarks,  recognizing  their  importance  in  tracking  AI's technical progress. As a standard practice, the Index sources benchmark  scores  from  leaderboards,  public  repositories such  as  Papers  With  Code  and  RankedAGI,  as  well  as company papers, blog posts, and product releases. The Index operates under the assumption that the scores reported by companies are accurate and factual. The benchmark scores in this section are current as of mid-February 2025. However, since the publication of the AI Index, newer models may have been released that surpass current state-of-the-art scores.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000066_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.2 Language

## 2.2 Language

Natural  language  processing  (NLP)  enables  computers  to understand,  interpret,  generate,  and  transform  text.  Current state-of-the-art models, such as OpenAI's GPT-4o, Anthropic's Claude 3.5, and Google's Gemini, are able to generate fl uent and coherent prose and display high levels of language understanding  ability (Figure 2.2.1). Unlike earlier  versions, which were restricted to text input and output, newer language models can now reason across a growing range of input and output  modalities,  including  audio,  images,  and  goal-oriented tasks (Figure 2.2.2).

## Gemini 2.0 in an agentic work fl ow

Source: AI Index, 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000067_2bc2f8a567c9beb656422429f0c8d69fbb3b04f45538730413aa189f2b83abed.png)

## A sample output from GPT-4o

Source: AI Index, 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000068_353c205f074f19c9bfc7035c5638ff4d42501d7ac1256139ebcb02e37bc32bb5.png)

Stanford HAI (Stanford Institute for Human-Centered Artificial Intelligence) is research institute at Stanford University dedicated to advancing Al in ways that enhance the human condition It promotes interdisciplinary collaboration between Al researchers social scientists, policymakers\_ and industry leaders to ensure that Al development and deployment align with human values and societal needs.

Key aspects of Stanford HAI include:

- Research: Conducting studies on Al's impact on society; ethics, and governance.
- Education: Offering courses, fellowships, and training programs on AI.
- Policy &amp; Outreach: Engaging with policymakers and global organizations to shape responsible Al regulations .
- Initiatives: Hosting events, publishing reports (such as the Al Index) , and developing tools like the Global Al Vibrancy Tool.

The institute plays a leading role in global Al discussions, ensuring that Al benefits humanity broadly while addressing its risks and challenges.  You can learn more at Stanford HAI's website

Figure 2.2.1

Figure 2.2.2

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000069_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.2 Language

## Understanding

English  language  understanding  challenges  AI  systems  to understand  the  English  language  in  various  ways,  such  as reading comprehension and logical reasoning.

## MMLU: Massive Multitask Language Understanding

The  Massive  Multitask  Language  Understanding  (MMLU) benchmark assesses model performance in zero-shot or fewshot  scenarios  across  57  subjects,  including the  humanities, STEM,  and  the  social  sciences  (Figure  2.2.3).  MMLU  has emerged as a premier benchmark for assessing LLM capabilities: Many state-of-the-art models like GPT-4o, Claude 3.5,  and  Gemini  2.0  have  been  evaluated  against  MMLU.

## A sample question from MMLU

Source:

Hendrycks et al., 2021

One of the reasons that the government discourages and regulates monopolies is that

- monopoly prices ensure productive efficiency but cost society allocative efficiency. 8 monopoly firms do not engage in significant research and development. consumer surplus is lost with higher prices and lower levels of output.
- (A) producer surplus is lost and consumer surplus is gained.

Figure 2.2.3

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000070_e2d3933b960f78b0b7bbcdd298d195bfa5ee93c72ef58c229fb5209339913230.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000071_66b1c4f30806db675272a66cd1380537fb1677a006e569910786eb0e451ff077.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000072_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

The  MMLU  benchmark  was  created  in  2020  by  a  team  of researchers from UC Berkeley, Columbia University, University of Chicago, and University of Illinois Urbana-Champaign.

The highest recorded score on MMLU, 92.3%, was achieved by  OpenAI's  o1-preview  model  in  September  2024.  For comparison, GPT-4, launched in March 2023, scored 86.4% on  the  benchmark.  Notably,  one  of  the  earliest  models tested  on  MMLU,  RoBERTa,  achieved  just  27.9%  in  2019 (Figure 2.2.4). This latest state-of-the-art result represents a remarkable 64.4 percentage point increase over fi ve years.

## Chapter 2: Technical Performance

2.2 Language

Despite its prominence, MMLU has faced notable criticisms. These include claims that the benchmark contains erroneous or  overly  simplistic  questions,  which  may  not  challenge increasingly advanced systems. In 2024, a team of researchers from the University of Toronto, University of Waterloo, and Carnegie Mellon introduced MMLU-Pro, a more challenging variant  of  MMLU.  This  version  eliminates  noisy  and  trivial questions, expands complex ones, and increases the number of answer choices available to models. Figure 2.2.5 highlights performance trends on MMLU-Pro,  with DeepSeek-R1 posting the highest score to date (84.0%).

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000073_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Generation

In generation tasks, AI models are tested on their ability to produce fl uent and practical language responses.

## Chatbot Arena Leaderboard

Additionally,  concerns  have  been  raised  about  the  testing landscape.  Developers  sometimes  report  MMLU  scores using nonstandard prompting techniques that boost performance but can lead to misleading comparisons. Furthermore, evidence suggests that publicly reported scores by  developers  can  di ff er-sometimes  by  as  much  as fi ve percentage points-from those later evaluated by academic researchers. As such, MMLU performance results should be interpreted with caution.

The rise of capable LLMs has made it increasingly important to  understand  which  models  are  preferred  by  the  general public.  Launched in  2023, the  Chatbot Arena Leaderboard from  LMSYS is  one  of the fi rst  comprehensive  evaluations of public LLM preference. The leaderboard allows users to query  two  anonymous  models  and  vote  for  the  preferred generations (Figure 2.2.6).  By  early  2025, the  platform  had accumulated over 1 million votes, with users ranking one of Google's Gemini models as the community's most preferred choice.

MMLU-Pro: overall accuracy Source: MMLU-Pro Leaderboard, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000074_4bf458c24f608dac3bed5230c19c0e7524a5aebde28c205e5ed49e627d6fce53.png)

## Chapter 2: Technical Performance

2.2 Language

## A sample model response on the Chatbot Arena Leaderboard

Source: Chatbot Arena Leaderboard, 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000075_c0b730e2197fc15c711c91f5f817a79136c66b3fd2cd9c0e3d18f37f1502a489.png)

Figure 2.2.6

Figure 2.2.7 provides a snapshot of the top 10 models on the Chatbot Arena Leaderboard as of January 2025. Interestingly, the performance gap between top leaderboard models has narrowed over time. In 2023, according to data from the 2024

AI  Index,  the  di ff erence  in  Arena  scores  between  the  top model and the 10th-ranked model was 11.9%. 6  By 2025, this gap had decreased to just 5.4%. This convergence highlights a growing parity in the quality of recent LLMs.

## LMSYS Chatbot Arena for LLMs: Elo rating (overall)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000076_94ed18c99250a92117a1bf50c6777ea8a1efafa6c05126a333661c184d7a4567.png)

6 The Arena score is a relative ranking system used by the Arena Leaderboard to compare model performance. For more details on the scoring methodology, refer to the paper introducing the Chatbot Arena Leaderboard.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000077_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.2 Language

## Arena-Hard-Auto

One of the challenges in developing new benchmarks to keep pace with rapidly  improving AI  capabilities  is that  creating high-quality, human-curated benchmarks is often expensive and time-consuming. In response, this year saw the launch of BenchBuilder. Created by a team of UC Berkeley researchers, BenchBuilder leverages LLMs  to create an automated pipeline for curating high-quality, open-ended prompts from large,  crowdsourced  datasets.  BenchBuilder  can  be  used to  update  or  create  new  benchmarks  without  signi fi cant human involvement. This tool was used by the LMSYS team to  develop  Arena-Hard-Auto,  a  benchmark  designed  to evaluate instruction-tuned LLMs (Figure 2.2.8). Arena-HardAuto  includes  500  challenging  user  queries  sourced  from Chatbot Arena.  In  this  benchmark,  GPT-4  Turbo  serves  as the judge that compares model responses against a baseline model (GPT-4-0314).

As of November 2024, the top-scoring models on the ArenaHard-Auto  leaderboard  were o1-mini (92.0), o1-preview (90.4),  and  Claude-3.5-Sonnet  (85.2)  (Figure  2.2.9).  ArenaHard-Auto also features a style control leaderboard, which

## Arena-Hard-Auto with no modi Ǉ cation

Source: LMSYS, 2025 | Chart: 2025 AI Index report

Model

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000078_e890e070b08a6a26726ce98df24ea9b239f490b6aa112d5a1cd11fc33f345891.png)

Figure 2.2.9

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000079_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Arena-Hard-Auto vs. other benchmarks

Source: Li et al., 2024

|                             | Evaluation   | Open-Ended   | Prompt Curation   | Prompt Source   |
|-----------------------------|--------------|--------------|-------------------|-----------------|
| Arena-Hard-Auto             | Automatic    | Yes          | Automatic         | Configurable    |
| MMLU, MATH, GPQA            | Automatic    | No           | Manual            | Fixed           |
| MT-Bench, AlpacaEval        | Automatic    | Yes          | Manual            | Fixed           |
| Live Bench, Live Code Bench | Automatic    | No           | Manual            | Fixed           |
| Chatbot Arena               | Human        | Yes          | Crowd-source      | Crowd           |

Figure 2.2.8

accounts  for  how  the  style  of  an  LLM's  responses  might inadvertently in fl uence user preferences. The top model on the style leaderboard is the November variant of Anthropic's Claude  Sonnet  3.5  (Figure  2.2.10).  Automated  benchmarks like Arena-Hard-Auto have faced criticism for uneven question  distribution,  which  limits  their  ability  to  provide  a comprehensive assessment of LLM capabilities. For instance, over  50%  of  Arena-Hard-Auto  questions  focus  solely  on coding and debugging.

## Arena-Hard-Auto with style control

Source: LMSYS, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000080_e8ce1df23f5b9e5668765ec485f14ea5dafa51d19d13618e5651e97aabb61769.png)

Model

Figure 2.2.10

## Chapter 2: Technical Performance

2.2 Language

## WildBench

WildBench, developed by researchers from the  Allen Institute for  AI  and  the  University  of  Washington,  is  a  benchmark launched  in  2024  to  evaluate  LLMs  on  challenging  realworld  queries.  The  creators  highlight  several  limitations of  existing  LLM  evaluations.  For  example,  MMLU focuses

## Evaluation framework for WildBench

Source: Lin et al., 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000081_bece271c2174ab7546e75a4b24ae0025ad84d6c731328424a407e391f23f16b5.png)

Figure 2.2.11

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000082_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

on academic questions and does not assess open-ended, real-world  problems.  Similarly,  benchmarks  like  LMSYS, which address real-world challenges, rely heavily on human oversight and lack consistency in evaluating all models with the same dataset.

## Chapter 2: Technical Performance

2.2 Language

WildBench addresses many shortcomings of existing benchmarks by providing an automated evaluation framework for  LLMs, incorporating a diverse set of real-world ('in the wild') questions that language models are likely to encounter (Figure 2.2.11). The questions in WildBench are meticulously selected from over 1 million human-chatbot interactions and

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000083_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

are  periodically  updated  to  ensure  relevance. The  creators also maintain a live leaderboard to track model performance over time. Currently, the top-performing model on WildBench is GPT-4o, with an Elo score of 1227.1, narrowly surpassing the second-place model, Claude 3.5 Sonnet, which scored 1215.4 (Figure 2.2.12).

## WildBench: WB-Elo (length controlled)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000084_624606e18caf02b0e44b56217247425fcf79328d472ddd804989fb92441d28b0.png)

## Chapter 2: Technical Performance

2.2 Language

## Highlight:

## o1, o3, and Inference-Time Compute

OpenAI's latest two models, o1 and o3, mark a paradigm shift  in  AI  models'  ability  to  'think'  and  exhibit  signs  of advanced  reasoning.  o1  and  o3  have  shown  impressive results  across  a variety  of tasks,  including  programming, quantum physics, and logic. The models' advanced reasoning  capabilities  are  attributed  to  their  chain-ofthought process and ability to iteratively check answers. This means that the models break complex problems into

## Chain-of-thought thinking in o1

Source: OpenAI, 2024

GPT-4o

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000085_500f8564aa954426e14ef6ef3863a0ef55f65e709e9fb507b1edfe212f023010.png)

User oyfjdnisdr rtqwainr acxz mynzbhhx Think step by step

Use the example above to decode:

oyekaijzdf aaptcg suaokybhai ouow aqht mynznvaatzacdfoulxxz smaller,  more  manageable  steps  before  executing them,

enhancing  the  resulting output quality. For  example, when asked to decipher scrambled text, o1 will specify its thought and reasoning process more thoroughly than GPT4 (Figure 2.2.13). This process, through which AI systems iterate as they answer, has been referred to as inference or test-time computation.

## Decoding Method:

- 1 Pair the letters in the ciphertext.
- 2 Convert each letter to its numerical position in the alphabet (A=1, B-2, Z=26).
- 3 Sum the numerical values of each pair.
- Compute the average of the sum (divide by 2)
- Convert the average back to a letter (I=A, 2=B, 26=Z).

Apply this method to the given ciphertext:

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000086_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Figure 2.2.13

## Chapter 2: Technical Performance

2.2 Language

## Highlight:

## o1, o3, and Inference-Time Compute (cont'd)

Figure 2.2.14 juxtaposes the scores of GPT-4o, OpenAI's previous state-of-the-art model, with o1 and o1-preview on a variety of benchmarks. 7   For example, o1 outperforms GPT4o with a 2.8-point gain on MMLU, 34.5 points on MATH, 26.7 points on GPQA Diamond, and 65.1 points on AIME

2024,  a  notoriously  di ffi cult  mathematics  competition. Finally, o3 demonstrates more complex reasoning than any other AI model known today, posting an 87.5% accuracy rate on the ARC-AGI machine intelligence benchmark and passing the previous record of 55.5%.

## GPT-4o vs. o1-preview vs. o1 on select benchmarks

Source: OpenAI, 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000087_cf2a4838f43cfaf60b9cd13ece061b8837f7c90cd1467fa05fad180ccdad0719.png)

While these models enhance reasoning capabilities, this comes at a price-both a fi nancial and latency cost. For example, GPT-4o costs $2.50 per 1 million input tokens and $10 per 1 million output tokens. Conversely, o1 costs $15 per 1 million input tokens and $60 per 1 million output tokens. 8 Moreover,  o1  is  approximately  40  times  slower than GPT-4o, with 29.7 seconds to fi rst token as opposed to  GPT-4o's  0.72.  The  latency  of  o3,  while  not  publicly available,  is  presumably  even  higher.  o1  and  o3's  strong capabilities  are  likely  to  continue  fueling  powerful  AI systems and agents.

OpenAI fi rst  released  o1-preview  to  ChatGPT  Plus  and Teams users on Sept. 12, 2024, and released the full version of o1 (as well as access to ChatGPT Pro, a $200 monthly subscription enabling access to o1) on Dec. 5, 2024.

7 The o1-preview model is OpenAI's early release of o1, made available before its broader public launch.

8 o3 is currently only available to select researchers and developers via OpenAI's safety testing program.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000088_7fe6dafa2de881df1e9b7fa9025d68e591cff47e2570d38ef628931ff075a239.png)

## Chapter 2: Technical Performance

2.2 Language

## MixEval

MixEval, launched by researchers at the National University of Singapore, Carnegie Mellon University, and the Allen Institute for  AI,  is  another  newly  released  benchmark  designed  to address some of the aforementioned limitations in the current fi eld  of  LLM  evaluation.  MixEval  combines  comprehensive, well-distributed, real-world user queries, similar to those found

## Evaluation framework for MixEval

Source: Ni et al., 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000089_208f490681e9f3914328c5b39372c25e29789607e7b3b260d40a6861b0e3fa09.png)

The highest-scoring model on the MixEval-Hard benchmark is  OpenAI's  o1-preview,  with  a  score  of  72.0.  In  second place is the Claude 3.5 Sonnet-0620 model, followed by the

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000090_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

in Chatbot Arena, with ground-truth-based questions, like those featured  in  MMLU  (Figure  2.2.15).  MixEval  includes  various evaluation  suites,  with  MixEval-Hard  representing  the  more challenging version  of  the  benchmark. This  suite  focuses  on substantially harder queries, making it one of the most e ff ective tools for assessing how models handle complex questions.

Figure 2.2.15

Llama-3  1-405B-Instruct  model, which  scored  66.2  (Figure 2.2.16). All three models were released in 2024.

## MixEval-Hard on chat models: score

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000091_c7535441df5f3acda4ed87cac4abcdb11be384a6f476f93ad605d4f3a067afcb.png)

## Chapter 2: Technical Performance

## RAG: Retrieval Augment Generation (RAG)

An  increasingly  common  capability  being  tested  in  LLMs is retrieval-augmented generation (RAG). This approach integrates LLMs  with retrieval mechanisms  to enhance their  response  generation. The  model fi rst  retrieves  relevant information  from fi les  or  documents  and  then  generates  a response tailored to the user's query based on the retrieved content.  RAG  has  diverse  use  cases,  including  answering precise questions from large databases and addressing customer queries using information from company documents.

models. 2024 also saw the release of numerous benchmarks for  evaluating  RAG  systems,  including  Ragnarok  (a  RAG arena battleground) and CRAG (Comprehensive RAG benchmark). Additionally, specialized RAG benchmarks, such as FinanceBench for fi nancial question answering, have been developed to address speci fi c use cases.

## Berkeley Function Calling Leaderboard

In recent years, RAG has received increasing attention from researchers  and  companies.  For  example,  in  September 2024, Anthropic introduced Contextual Retrieval, a method that signi fi cantly enhances the retrieval capabilities of RAG

The  Berkeley  Function  Calling  Leaderboard  evaluates  the ability  of  LLMs  to  accurately  call  functions  or  tools.  The evaluation suite includes over 2,000  question-functionanswer pairs across multiple programming languages (such as  Python,  Java,  JavaScript,  and  REST  API)  and  spans  a variety of testing domains (Figure 2.2.17).

## Data composition on the Berkeley Function Calling Leaderboard

Source: Yan et al., 2024

## Berkeley Function-Calling Leaderboard Evaluation Data Composition

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000092_1776e5a4c1fab2aba9dde6adcf61ebb8a91d4614a5be878d6e572678c82eb065.png)

Figure 2.2.17 9

| Javascript (AST)          | Chatting Capability             |
|---------------------------|---------------------------------|
| 2.5%                      | 10.0%                           |
| SQL (AST)                 | Simple (Exec)                   |
| 5.0% Java (AST)           | 5.0% Multiple (Exec)            |
| 5.0% REST (Exec)          | 2.5%                            |
| Relevance                 | Parallel (Exec)                 |
|                           | 2.5% Parallel & Multiple (Exec) |
| 12.0%                     | 2.0%                            |
| Parallel & Multiple (AST) | Simple (AST)                    |
| 10.0%                     | 20.0%                           |
| Parallel (AST)            | Multiple (AST)                  |
| 10.0%                     | 10.0%                           |

9 In this context: AST (abstract syntax tree) refers to tasks that involve analyzing or manipulating code at the structural level, using its parsed representation as a tree of syntactic elements. Evaluations labeled with 'AST' likely test an AI model's ability to understand, generate, or manipulate code in a structured manner. Exec (execution-based) indicates tasks that require actual execution of function calls to verify correctness. Evaluations labeled with 'Exec' likely assess whether the AI model can correctly call and execute functions, ensuring the expected outputs are produced.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000093_99f921b4cebec7471ac6a9ceb7103de38331817aafb3f9ce30bd05f2b6c447a8.png)

## Chapter 2: Technical Performance

2.2 Language

The top model on the Berkeley Function Calling Leaderboard is  watt-tool-70b,  a fi ne-tuned  variant  of  Llama-3.3-70BInstruct designed speci fi cally for function calling. It achieved an overall accuracy of 74.31 (Figure 2.2.18). The next-highestscoring  model  was  a  November variant  of  GPT-4o,  with  a score of 72.08. Performance on this benchmark has improved signi fi cantly over the course of 2024, with top models at the end of the year achieving accuracies up to 50 points higher than those recorded early in the year.

## Berkeley Function-Calling: overall accuracy

Model

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000094_9522a62c3e5ca95fb33d0b6b986ee6a51881183a4c4ff2c8742dd64d9f07ed87.png)

Figure 2.2.18

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000095_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.2 Language

## MTEB: Massive Text Embedding Benchmark

The  Massive Text  Embedding  Benchmark  (MTEB),  created by a team at Hugging Face and Cohere, was introduced in late 2022 to comprehensively evaluate how models perform on various embedding tasks. Embedding involves converting data,  such  as  words,  texts,  or  documents,  into  numerical vectors that capture rough semantic meanings and distance between vectors. Embedding is an essential component of RAG. During a RAG task, when users input a query, the model

## Tasks in the MTEB benchmark

Source: Muennigho ff et al., 2023

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000096_edbe7f0912695bc2f93510e7891966ba489ad8219de9611884f8b875e42b93a2.png)

Figure 2.2.19

10 The benchmark covers the following eight tasks: bitext mining, classi fi cation, clustering, pair classi fi cation, reranking, retrieval, semantic textual similarity, and summarization. For details on each task, refer to the MTEB paper .

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000097_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

transforms it into an embedding vector. This transformation enables the  model to then  search for  relevant  information. MTEB  includes  58  datasets  spanning  112  languages  and eight embedding tasks (Figure 2.2.19). 10  For example, in the bitext mining task, there are two sets of sentences from two di ff erent languages, and for every sentence in the fi rst  set, the model is tasked to fi nd the best match in the second set.

## Chapter 2: Technical Performance

## 2.2 Language

As of early 2025, the top-performing embedding model on the MTEB benchmark was Voyage AI's voyage-3-m-exp, with a score of 74.03. Voyage AI is focused on creating high-quality AI embedding models. The voyage-3-m-exp model is a variant of the voyage-3-large, a large foundation model speci fi cally designed  for  embedding  tasks,  and  it  uses  strategies  like Matryoshka Representation Learning and quantization-aware training  to  improve  its  performance.  The  voyage-3-m-exp model narrowly outperformed NV-Embed-v2 (72.31), which held  the  top  spot  for  most  of  2024  (Figure  2.2.20).  When the MTEB benchmark was fi rst introduced in late 2022, the leading model achieved an average score of 59.5. Over the past  two  years,  therefore,  performance  on  the  benchmark has meaningfully improved.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000098_0176d86aa28f83141c209231aa3faca4a6f0a816e52bf79165f72b66ad6205fb.png)

Figure 2.2.20

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000099_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.2 Language

## Highlight:

## Evaluating Retrieval Across Long Contexts

As AI models have advanced, their ability to handle longer contexts has signi fi cantly improved. For example, models like GPT-4 and Llama 2, released in 2023 by OpenAI and Meta,  featured  context  windows  of  8,000  and  4,000 tokens, respectively. In contrast, more recent models such as GPT-4o (May 2024) and Gemini 2.0 Pro Experimental (February 2025) boast context windows ranging from 128 thousand  to  2  million.  These  extended  context  windows allow users to input and process increasingly large amounts of data, enabling more complex and detailed interactions.

As the context windows of LLMs have expanded, evaluating their  performance  in  long-context  settings  has  become increasingly  important.  However,  existing  long-context evaluation methods have been relatively limited. Typically, these evaluations focus on 'needle-in-the-haystack' scenarios, where models are tasked with retrieving speci fi c pieces of information from lengthy texts. While useful, such evaluations provide only a baseline assessment of a model's ability to function e ff ectively in long-context environments.

In 2024, several new evaluation suites were introduced to address the limitations of long-context model assessments and  improve  their  evaluation.  One  such  benchmark  is Nvidia's RULER, which assesses long-context performance by examining retrieval performance and multihop reasoning, aggregation, and question answering. Among the models evaluated on RULER, Gemini-1.5-Pro achieved the highest weighted  performance  average  (95.5),  followed  by  GPT4  (89.0)  and  GLM4(88.0)  (Figure  2.2.21). The  researchers behind  RULER  also  revealed  that  many  models  su ff er performance issues in longer context settings. In fact, the RULER team demonstrated that while most popular LLMs claim context sizes of 32K tokens or greater, only half of them can maintain satisfactory performance at the length of  32K.  This  means  that  their  actual  operational  context windows are shorter than those claimed by their developers (Figure 2.2.22).

## RULER: weighted average score (increasing)

Source: Hsieh et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000100_3ba69b535dd5c76349f0f6d5be7484efbf1d33bda533a4a70a63176bc22dc22a.png)

Figure 2.2.21

RULER: claimed vs. eǄective context length

Source: Hsieh et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000101_4a374ef98238beb5cbc08af356eb0fed68958a6569ef84cc5d7c14e950c07817.png)

Figure 2.2.22

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000102_7fe6dafa2de881df1e9b7fa9025d68e591cff47e2570d38ef628931ff075a239.png)

## Chapter 2: Technical Performance

2.2 Language

## Highlight:

## Evaluating Retrieval Across Long Contexts (cont'd)

HELMET (How to Evaluate Long-Context Models E ff ectively and  Thoroughly), an Intel and Princeton collaboration, is another long-context evaluation benchmark introduced in 2024. The researchers behind HELMET were motivated by the inadequacies of existing benchmarks, which  su ff ered  from  insu ffi cient  coverage of downstream  tasks,  context lengths too short to test  evolving  long-context  capabilities,  and  unreliable metrics (Figure 2.2.23). Even more comprehensive than RULER, HELMET features seven long-context evaluation categories, including synthetic recall, passage re-ranking, and  generation  with  citations.  Figure  2.2.24  illustrates the  average  performance  of  several  notable  models on  the  HELMET  benchmark  across  8K,  32K,  and  128K context  settings.  While  models  like  GPT-4,  Claude  3.5 Sonnet,  and  Llama  3.1-70B  struggle  with  performance degradation  in  longer  context  settings,  others,  such  as Gemini 1.5 Pro and the August variant of GPT-4, maintain their e ff ectiveness. The introduction of benchmarks like RULER and HELMET highlights how the rapid evolution of LLMs is compelling researchers to rethink and re fi ne evaluation methodologies.

## Comparing longcontext benchmarks

Figure 2.2.23 Source: Yen et al., 2024

|               | Type of tasks   | Type of tasks   | Type of tasks   | Type of tasks   | Type of tasks   | Type of tasks    | Benchmark features   | Benchmark features   |
|---------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|----------------------|----------------------|
|               | Cite RAG        | Cite RAG        | Long- QA        | Summ ICL        | Summ ICL        | Synthetic Recall | Robust Eval          | L > 128k             |
| ZeroSCROLLS   |                 |                 | W               |                 |                 |                  |                      |                      |
| LongBench     |                 |                 |                 |                 |                 |                  |                      | '                    |
|               |                 |                 |                 |                 |                 |                  | ;                    |                      |
| HELMET (Ours) |                 | V               |                 |                 | V               | V                | V                    | V                    |

## HELMET: average score

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000103_49296ca0eddbccfea325a8a8c9bbb02af649921f27a38d1529e2f6114bc4c15a.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000104_ea6b89190827a0cf68ddd3597db3629f114e4be7363b0007ff902af8da6cb91d.png)

## Chapter 2: Technical Performance

2.3 Image and Video

Computer vision allows machines to understand images and videos  and  to  create  realistic  visuals  from  textual  prompts or other inputs. This technology is widely used in fi elds such as  autonomous  driving,  medical  imaging,  and  video  game development.

## 2.3 Image and Video

## Understanding

Vision  models  are  evaluated  on  their  ability  to  understand and reason about the content of images and videos. Vision understanding  was  one  of  the fi rst  AI  capabilities  widely tested during the deep learning era. ImageNet, created by Fei-Fei  Li  and  extensively  covered  in  past  editions  of  the AI  Index,  served  as  a  foundational  benchmark  for  image understanding.  As  AI  systems  have  advanced,  researchers have  shifted  toward  evaluating  image  models  on  more complex  and  comprehensive  understanding  tasks,  such  as those involving video or commonsense reasoning in images.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000105_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

these cases, algorithms process natural language questions, identify  objects from  an  open  set  of  images,  and  generate answers based on image content or prior knowledge.

## VCR: Visual Commonsense Reasoning

In the ImageNet era, vision algorithms were tasked with more straightforward tasks (e.g., classifying images into prede fi ned categories). However, modern computer vision benchmarks like VCR and MVBench introduce more open-ended challenges,  where  no fi xed  categories  or  classes  exist.  In

Introduced  in 2019  by  researchers  from  the University of  Washington  and  the  Allen  Institute  for  AI,  the  Visual Commonsense Reasoning (VCR) challenge tests the commonsense visual reasoning abilities of AI systems. In this challenge, AI systems not only answer questions based on images but also reason about the logic behind their answers (Figure  2.3.1).  Performance  in  VCR  is  measured  using  the Q-&gt;AR score, which evaluates the machine's ability to both select the correct answer to a question (Q-&gt;A) and choose the appropriate rationale behind that answer (Q-&gt;R).

## Sample question from Visual Commonsense Reasoning (VCR) challenge

Source: Zellers et al., 2018

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000106_33f6815bcb29bcdaa4baeb6ca123d0b6c5312b43ab375e79ee143ae51c7a695c.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000107_5843bfd94f385090eb364864788228e5399cc5561e96904565414c8dee228d7d.png)

Figure 2.3.1

## Chapter 2: Technical Performance

## 2.3 Image and Video

The VCR benchmark was one of the few benchmarks routinely featured  in  the  AI  Index  where  AI  systems  consistently fell  short  of  the  human  baseline.  However,  2024  marked  a turning point, with AI systems fi nally reaching this baseline. A model posted to the leaderboard in July 2024 achieved a score of 85.0, matching the human benchmark (Figure 2.3.2). This milestone represented a signi fi cant 4.2% improvement on the benchmark since 2023. Even previously challenging benchmarks are now being surpassed.

## Visual Commonsense Reasoning (VCR) task: Q-&gt;AR score

Source: VCR Leaderboard, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000108_76957f696fad2e94c03bf741f64faa7423c16e80eb6895ff1aabd367d9ec698a.png)

Figure 2.3.2

## MVBench

MVBench,  introduced  by  a  team  of  researchers from Hong Kong and China in 2023, is a challenging, multimodal, video-understanding benchmark. 11 Unlike earlier video benchmarks  that primarily tested spatial  understanding through static image tasks, MVBench incorporates more complex video tasks requiring temporal reasoning across multiple frames (Figure 2.3.3).

## Spatial Understanding: Inferring from single frame

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000109_7de3dfaf3b1e463d244660bab8a6d82dba352b84a1be47eea4bf7e2584e5ec01.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000110_5257ce9f97513529ad35cabfa35600fdeaa7d6b29dd4aa0d6b63c4a1e67929dc.png)

## Temporal Understanding: Reasoning based on entire video

Action

Position

Attribute

Action Sequence

Moving Direction

State Change

Action Antonym

Action Localization

Moving Attribute

Action Prediction

Count

Character

Unexpected Action

Action Count

Character Order

Fine-

~grained Action

Moving Count

Object

Scene

Cognition

Object Shuffle

Scene Transition

Episodic Reasoning

Object Existence

Pose

Egocentric Navigation

Object Interaction

Fine-grained Pose

Counterfactual Inference

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000111_c84f3c9ee9d13f42c9993b9b5be79f210f224bed8e5eb8137d56d63306b90261.png)

11 The researchers were a ffi liated with the Chinese Academy of Sciences, University of Chinese Academy of Sciences, Shanghai AI Laboratory, the University of Hong Kong, Fudan University, and Nanjing University.

## Sample tasks on MVBench

Figure 2.3.3 Source: Li et al., 2023

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000112_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

## 2.3 Image and Video

As of 2024, the top model on the MVBench leaderboard is Video-CCAM-7B-v1.2,  built  on  the  Queen  2.5-7B-Instruct language model. Its score of 69.23 marks a signi fi cant 14.6% improvement  on  the  benchmark  since  its  introduction  in

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000113_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

late 2023 (Figure 2.3.4). These results highlight the gradual but  steady  progress  in  the  dynamic  video  understanding capabilities of AI models.

## MVBench: average accuracy

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000114_a5cd5e295e5b0ced5ef378b08d5bf1b0b898042f6035658a88781edb1129448f.png)

Figure 2.3.4

## Chapter 2: Technical Performance

2.3 Image and Video

## Generation

Image generation is the task of generating images that are indistinguishable  from  real  ones.  As  noted  in  last  year's  AI Index, today's image generators are so advanced that most people struggle to di ff erentiate between AI-generated images and actual images of human faces (Figure 2.3.5). Figure 2.3.6 highlights several generations from various Midjourney model variants from 2022 to 2025 for the prompt 'a hyper-realistic image  of  Harry  Potter.'  The  progression  demonstrates  the signi fi cant improvement in Midjourney's ability to generate hyper-realistic images over a two-year period. In 2022, the model  produced  cartoonish  and  inaccurate  renderings  of Harry Potter, but by 2025, it could create startlingly realistic depictions.

Figure 2.3.5

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000115_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000116_14884f2670f7be0d7fd11ceb06f99729393d06e073f22983691dd4b9fe0ffe21.png)

Midjourney generations over time: 'a hyper-realistic image of Harry Potter' Source: Midjourney, 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000117_25e7947644cdcefb6a8834f0058f85eb801a4d3cdbb38b3cf3dec6cef46ad7a8.png)

V1, February 2022

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000118_8eb9549834054b4ea46ed7c80cbb0ab892cb2c9b6523589b6e221c6e80e93f61.png)

V2, April 2022

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000119_bfc0317b5c0ca86afef3e8e8d30aa1642c83050f7d8b9b7844b78c3ff74b160a.png)

V3, July 2022

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000120_b8899fb1a687e3e4e8c4bea0d484b32da7ab4c65d05ad905266902d8cff43fa9.png)

V4, November 2022

V5, March 2023

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000121_9cb16ba34478cb3a297790704e0fd122ddd50446e7b8dce5f78b387c17d381ff.png)

V6, December 2023

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000122_7fa1f077f3bf8f66617bfb6b56ed889831a31622a188fb4c3e398bb1dc067559.png)

## Which face is real?

Source: Which Face Is Real, 2024

V6.1, July 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000123_978c3d21eaa13c9e66cc2f8688588bc4d748c706ec568c19e5cfb759c85f0f37.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000124_3a0f310d92f24511be9d91f962ccb410cc59f9a1d24820012f367ad8e12ad3f1.png)

Figure 2.3.6

## Chapter 2: Technical Performance

2.3 Image and Video

## Chatbot Arena: Vision

The AI community has increasingly embraced public evaluation  platforms,  such  as  the  Chatbot  Arena Leaderboard,  to  assess  the  capabilities  of  leading AI  systems,  including  top  AI  image  generators. This leaderboard also features a Vision Arena, which ranks the  performance  of  over  50  vision  models.  Users can submit text-to-image prompts, such as 'Batman drinking a  co ff ee,' and vote for their preferred generation (Figure 2.3.7). To date, the Vision Arena has garnered more than 150,000 votes.

## Sample from the Chatbot Vision Arena

Source: Chatbot Arena Leaderboard, 2025

As of early 2025, the top-ranked vision model on the leaderboard  is  Google's  Gemini-2.0-Flash-ThinkingExp-1219 (Figure 2.3.8). Similar to other Chatbot Arena categories-such as general, coding, and math-the leading models are closely clustered in performance. For example, the gap between the top model and the fourth-ranked  model,  ChatGPT-4o-latest  (2024-1120), is just 3.4%.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000125_3f7fa00170a481d083bbbdd838b75f99f35e1e5e00592f901fc3a8949a0fbcf8.png)

Figure 2.3.7

## LMSYS Chatbot Arena for LLMs: Elo rating (vision)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000126_517c4a44fc3d9f4d4b1b37a5dfe2372295becc2fcf1030340a25ebdf277af888.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000127_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Figure 2.3.8

## Chapter 2: Technical Performance

2.3 Image and Video

## Highlight:

## The Rise of Video Generation

As highlighted  in  last year's AI  Index,  recent years  have witnessed the rise of video generation models capable of creating videos from text prompts. While earlier models demonstrated  some  promise,  they  were  plagued  by signi fi cant limitations, such as producing low-quality videos,  omitting  sound,  or  generating  only  very  short clips. However, 2024 marked a signi fi cant leap forward in AI video  generation, with  several  major  industry  players unveiling advanced video generation systems.

In November 2023, Stability AI launched its Stable Video Di ff usion  model, their fi rst  foundation  model  capable  of generating  high-quality videos  (Figure  2.3.9). The  model

## Still generations from Stable Video Di ff usion

Source: Stability AI, 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000128_ea6e7e559413cb37ee7a77d4a89ae1fcce3e8471711c32561b83a22b7794156d.png)

## Still generation from Sora

Source: OpenAI, 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000129_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

follows  a  three-step  process:  text-to-image  pretraining, video pretraining, and  high-quality  video fi ne-tuning. Shortly  after,  in  March,  Stability  AI  introduced  Stable Video 3D, a model designed to generate multiple 3D views and videos of an object from a single image. In February 2024, OpenAI responded with a preview of Sora, its own video  generation  model,  which  moved  out  of  research mode and became publicly accessible in December 2024. Sora can generate 20-second videos at resolutions up to 1080p  (Figure  2.3.10).  As  a  di ff usion  model,  it  creates  a base video and progressively re fi nes it by removing noise over multiple steps to enhance quality.

Figure 2.3.9

Figure 2.3.10

## Chapter 2: Technical Performance

2.3 Image and Video

## Highlight:

## The Rise of Video Generation (cont'd)

Other major tech players have entered the video generation space. In October 2024, Meta unveiled the latest version of its Movie Gen model. Unlike earlier iterations, the new Movie Gen  includes  advanced  instruction-based  video  editing features,  personalized  video  generation  from  images,  and the  ability  to  incorporate  sound  into  videos.  Meta's  most advanced Movie Gen model can create 16-second videos at 16 frames per second, with a resolution of 1080p. Google also made signi fi cant strides in 2024, launching two major video generation  models:  Veo  in  May  and  Veo  2  in  December. Internal  benchmarking  by  Google  revealed  that  Veo  2 outperformed other leading video generators, such as Meta's Movie Gen, Kling v1.5, and Sora Turbo. In user comparisons, videos generated by Veo 2 were consistently favored over those produced by competing models (Figure 2.3.11).

## Veo 2: overall preference

Source: DeepMind, 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000130_5fe5b72715d8f843e98616b9862934b383773470c1eb245307cb87a71f8f72b8.png)

Smaller players have also made notable contributions to video generation, with models such as Runway's Gen-3 Alpha, Luma's  Dream  Machine,  and  Kuaishou's  Kling  1.5.  The  remarkable  progress  in  this fi eld  is  evident  when  comparing videos generated in 2023 to those produced in 2024. A popular prompt on the internet, 'Will Smith eating spaghetti,' demonstrates this advancement, with videos generated in 2025 from one popular video generator Pika showcasing a dramatic improvement in quality compared to their 2023 counterparts (Figure 2.3.12).

## Will Smith eating spaghetti, 2023 vs. 2025

Source: Pika, 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000131_a62877a3180f67fd0ff889ffb5fa31d27ee1d957512773c2b9c7dd757e859bf5.png)

Figure 2.3.12

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000132_7fe6dafa2de881df1e9b7fa9025d68e591cff47e2570d38ef628931ff075a239.png)

## Chapter 2: Technical Performance

2.4 Speech

AI  systems  are  adept  at  processing  human  speech,  with audio capabilities that include transcribing spoken words to text  and  recognizing  individual  speakers.  More  recently, AI has advanced in generating synthetic audio content.

## 2.4 Speech

## Speech Recognition

Speech  recognition  is  the  ability  of  AI  systems  to  identify spoken words and convert them into text. Speech recognition has progressed so much that today many computer programs and texting apps are equipped with dictation devices that can reliably transcribe speech into writing.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000133_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

## LSR2: Lip Reading Sentences 2

The  Oxford-BBC  Lip  Reading  Sentences  2  (LRS2)  dataset, introduced in 2017, is one of the most comprehensive public datasets  for  lipreading  in  authentic,  in-the-wild  scenarios (Figure 2.4.1). The dataset consists of audio-visual clips from a  variety  of  talk  shows  and  news  programs.  On  automatic speech recognition (ASR) tasks, systems' ability to transcribe speech are evaluated on word error rate (WER), with lower scores indicating more precise transcription.

## Still images from the BBC lip reading sentences 2 dataset

Source: Chung et al., 2024

Figure 2.4.1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000134_f5fd2f223e0275a5ce45fb0ad8acf24779996dc16fae87fb941c1445e6025cdc.png)

## 2.4 Speech Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000135_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

This year, the model Whisper-Flamingo set a new standard on the LRS2 benchmark, achieving a word error rate of 1.3 percent,  surpassing  the  previous  state-of-the-art  score  of

## LRS2: word error rate (WER)

1.5  set  in  2023  (Figure  2.4.2).  However,  given  the  already low WER, signi fi cant further improvements appear unlikely, suggesting that the benchmark may be nearing saturation.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000136_5404ebb21d4114cafdbf04140011fdaaf8aab83ee2ac99f294ba62dc5a325571.png)

Figure 2.4.2

## Chapter 2: Technical Performance

2.5 Coding

Coding involves the generation of instructions  that  computers  can  follow to  perform  tasks.  Recently,  LLMs  have become  pro fi cient coders, serving as valuable assistants to computer scientists. There  is  also  increasing  evidence  that many  coders fi nd  AI  coding  assistants highly useful. As highlighted in last year's AI Index, LLMs have become increasingly pro fi cient coders, to the extent that many foundational  coding  benchmarks,  such as HumanEval, are slowly becoming saturated.  In  response,  researchers  have shifted  their  focus  toward  testing  LLMs on more complex coding challenges.

## Sample HumanEval problem

Source: Chen et al., 2023

```
def incr_list(l: list): Return list with elements incremented by 1 incr_list([1, 2, 3]) [2 , 3 , 4] incr_list([5, 3 , 5 , 2 , 3 , 3 , 9 , 0 , 123]) [6 , 4 , 6 , 3 , 4 , 4 , 1 , 124] return [i + 1 for 1 in 1] 10 ,
```

## 2.5 Coding

## HumanEval

HumanEval, a benchmark introduced by OpenAI researchers in 2021, evaluates the coding abilities of AI systems through 164 challenging, handwritten programming problems (Figure 2.5.1). The current leader in HumanEval performance is Claude 3.5 Sonnet (HPT), which achieved a score of 100% (Figure 2.5.2).

Figure 2.5.1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000137_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

## HumanEval: Pass@1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000138_b749119c725edbf05eb804f5457d045c7447047ab930d33ef15c27b07020c647.png)

Figure 2.5.2

## 2.5 Coding Chapter 2: Technical Performance

## SWE-bench

In October 2023, researchers from Princeton and the University of  Chicago  introduced  SWE-bench,  a  dataset  comprising 2,294  software  engineering  problems  sourced  from  real GitHub issues and popular Python repositories (Figure 2.5.3). SWE-bench presents a tougher test for AI coding pro fi ciency, demanding that systems coordinate changes across multiple functions, interact with various execution environments, and perform complex reasoning. SWE-bench features a Lite subset that is curated to make evaluation more accessible and a Veri fi ed subset that is fi ltered  by  a  human  annotator. The charts below report on the Veri fi ed score.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000139_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## A sample model input from SWE-bench

Source: Jimenez et al., 2023

SWE-bench highlights the  rapid  improvement  of  LLMs  on tasks that were once considered extremely demanding. At the end of 2023, the best performing model on SWE-bench achieved a score of just 4.4%. By early 2025, the top model, OpenAI's o3 model, is reported to have successfully solved 71.7% of the problems on the Veri fi ed benchmark set (Figure 2.5.4).  This  signi fi cant  performance  increase  suggests that AI researchers may soon need to develop more challenging coding benchmarks to e ff ectively test LLMs.

Figure 2.5.3

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000140_6f0a09d7dbce621ba1dd0d8348350ced1224501186ca5f7e16734727c8168b2a.png)

## SWE-bench: percent solved

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000141_6fc7ae8c702924c71846c605d260a999ed01b668513462517801ce7fd51629a6.png)

## 2.5 Coding Chapter 2: Technical Performance

## BigCodeBench

One limitation  of  existing  coding  benchmarks  is that  many are  restricted  to  short,  self-contained  algorithmic  tasks  or standalone  function  calls.  However,  solving  complex  and practical  tasks  often  requires  the  ability  to  invoke  diverse functions, such as tools for data analysis or web development. E ff ective  coding  also  requires  the  ability  to  follow  coding instructions expressed in language, a task not tested by many current coding benchmarks.

To  address  the  limitations  of  existing  coding  benchmarks, an  international  team  in  2024  released  BigCodeBench,  a comprehensive,  diverse,  and  challenging  benchmark  for

## Programming tasks in BigCodeBench

Source: Zhuo et al., 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000142_760527020daa7059ac516b1bfe34234e402cfa5fa5a389aa96ac036fc2f2ce13.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000143_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

coding  evaluation  (Figure  2.5.5).  BigCodeBench  requires LLMs to  invoke  multiple  function  calls  across  139  libraries and seven domains, encompassing 1,140 fi ne-grained tasks. Current AI systems struggle on BigCodeBench. For example, on both the 'complete' (code completion based on structured docstrings) and 'instruct' (code completion based on natural-language instructions) tasks on the hard subset of the benchmark, the current best model, OpenAI's o1, achieves an average score of just 35.5 (Figure 2.5.6). Models perform slightly better on the full set of the benchmark (Figure 2.5.7). BigCodeBench highlights the gap that persists for AI systems to achieve human-level coding pro fi ciency.

## 2.5 Coding Chapter 2: Technical Performance

## Chatbot Arena: Coding

The Chatbot Arena LLM leaderboard now features a coding fi lter,  o ff ering  valuable  insights  into  how  coders  and  the broader  community  perceive  the  coding  capabilities  of di ff erent models. This public feedback adds a new dimension to  evaluating  model  performance.  Currently,  the  top-rated

LLM for coding is Gemini-Exp-1206, with an arena score of 1,369, closely followed by OpenAI's latest o1 model at 1,361. Among Chinese  models,  DeepSeek-V3  leads  with  a  score of  1,317,  trailing  the  highest-ranking  model  by  3.8%  (Figure 2.5.8).

## LMSYS Chatbot Arena for LLMs: Elo rating (coding)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000144_d063ec3f438d53775e099b05d5042ac88a9cf0e7874ed0a04544977286a8a29f.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000145_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.6 Mathematics

Mathematical problem-solving benchmarks  evaluate  AI systems' ability to reason mathematically. AI models can be tested with  a  range  of  math  problems, from  grade-school level to competition-standard mathematics.

## 2.6 Mathematics

## GSM8K

GSM8K, introduced by OpenAI in 2021, is a dataset containing approximately 8,000 diverse grade-school math  word  problems  that  challenges  AI  models to generate multistep solutions using arithmetic operations (Figure 2.6.1). Alongside  MMLU, GSM8K has become a widely used benchmark for evaluating advanced  LLMs.  However,  recent  concerns  have emerged regarding potential contamination and saturation of the benchmark.

The top-performing model on GSM8K is a variant of Claude  Sonnet  3.5,  which  was  optimized  using  the HPT prompting strategy and achieved a 97.72% score (Figure 2.6.2). This  marks  a  signi fi cant improvement

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000146_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Sample problems from GSM8K

Source: Cobbe et al., 2023

Problem: Beth bakes 2 dozen batches of cookies in week. If Ihese cookies are shared amongst 16 people equally; how many cookies does each person consume?

Solutlon: Beth bakes total of 4*2 dozen cookies

There are 12 cookies in dozen and she makes dozen cookies for , lotal of 12*8

She splits the 96 cookies equally amongst 16 people so they each eat 96/16

&lt;&lt;96/16-62&gt;

cookies

Final Answer:

Problem: Mrs. Lim milks her cows Iwice day.  Yesterday morning she she got 82 gallons. This morning she 18 gallons fewer than she had yesterday morning. Atter selling some gallons ot milk in the afternoon, Mrs . Lim has only 24 gallons lett. How much was her revenue for the milk each gallon costs 53.50? gol got

Mrs. Lim got 68 gallons 18 gallons &lt;68-18=502&gt;50 gallons this morning

So she was able to get total of 68 gallons 82 gallons 50 gallons 2&lt;68+82+50-2002&gt;200 gallons.

She was able to sell 200 gallons

24 gallons

&lt;&lt;200-24=1763&gt;176 gallons\_

Thus, her total revenue for the milk is 53.50/gallon 176 gallons

Final Answer: 616

Problem: Tina buys 3 12-packs of soda for a party;  Including Tina people are at the party.  Half of the people at the party have sodas each, 2 of the people have and person has 5. How many sodas are left over when the party over?

6 people attend the party; so half of them Is 6/2= &lt;&lt;6/2=32&gt;

people

Each of those people drinks

sodas,

tney drink

Two people drink

sodas

sodas

With one person drinking that brings the total drank I0 5+9+8+3= &lt;&lt;5+9+8+3-252225 sodas

As Tina started off wlth 36 sodas, that means there are 36-25=&lt;&lt;36-25=112211 sodas left

Final Answer: 11

Figure 2.6.1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000147_3d457014852f81980c473e4705e565a0f08baab5573ac7f82a73be52c3d6cc7a.png)

over the previous high of 91.00% in 2023. However, in 2024, several models from Mistral, Meta, and Qwen scored around 96%, indicating that the GSM8K benchmark may be approaching saturation.

## GSM8K: accuracy

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000148_bc281bdc9d724c351878241fba388b0ec9fa6f156d8d39e6c79e63b9a8904d57.png)

Figure 2.6.2

## 2.6 Mathematics Chapter 2: Technical Performance

## MATH

MATH is a dataset of 12,500 challenging, competition- level mathematics problems introduced by UC Berkeley and  University  of  Chicago  researchers  in  2021  (Figure 2.6.3). AI systems struggled on MATH when it was fi rst released, managing to solve only 6.9% of the problems. Performance  has  signi fi cantly improved.  In  January 2025,  OpenAI's  o3-mini  (high)  model  was  released and  achieved  the  best  performance  on  the  MATH dataset, solving 97.9% of the problems (Figure 2.6.4). As highlighted in last year's AI Index, MATH was one of the few datasets where AI systems had not yet outperformed the human baseline. This fact no longer remains true.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000149_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Sample problem from MATH dataset

Source: Hendrycks et al., 2023

## MATH Dataset (Ours

Problem: Tom has a red marble, a green marble; blue marble; and three identical yellow marbles How many different groups of two marbles can Tom choose?

Solution: There are two cases here: either Tom chooses two yellow marbles (1 result) , or he chooses two marbles of different colors =6 results) . The total number of distinct pairs of marbles Tom can choose is 1 + 6 =

Problem: The equation 22 + 22 = i has two complex solutions. Determine the product of their real parts.

Solution: Complete the square by adding 1 to (~1 +cos

<!-- formula-not-decoded -->

Figure 2.6.3

## MATH word problem-solving: accuracy

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000150_25892f4653aa544bf8207f8f04b3f182dbdbd2c9fa2887b0a37156edb45f5752.png)

## Chatbot Arena: Math

The Chatbot Arena includes a math fi lter, allowing the public to  rank  models  based  on  their  performance  in  generating math-related  answers.  The  Math  Arena  evaluates  over  181 models and has collected more than 340,000 public votes.

Unlike the general and coding arenas, where Gemini-based models  lead,  the  top-ranked  model  in  the  Math  Arena  is OpenAI's  o1  variant,  released  in  December  2024  (Figure 2.6.5).

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000151_dddfc0244b2f95c83bcf95802750b64f47eaa081a95810e12485e16a217e0ee5.png)

## FrontierMath

Members of the math community have highlighted limitations in  the  current  suite  of  math  benchmarks,  calling  for  the development  of  new  benchmarks  to  evaluate  increasingly advanced AI systems. One signi fi cant challenge is saturation: AI systems are approaching near-perfect performance on  benchmarks  like  GSM8K  and  MATH,  which  primarily assess high school and college-level mathematics. To push the boundaries further, researchers have voiced a need for benchmarks that test truly advanced mathematics, including problems in number theory, real analysis, algebraic geometry, and category theory.

FrontierMath is a new benchmark introduced by Epoch AI that features hundreds of original, exceptionally challenging mathematical problems. These problems, vetted by expert  mathematicians,  often  require  hours,  days,  or  even collaborative research e ff orts to solve. Figure 2.6.6 illustrates sample  problems  included  on  the  benchmark.  Epoch  AI evaluated six leading LLMs on the FrontierMath benchmark: o1-preview,  o1-mini,  GPT-4o,  Claude  3.5  Sonnet,  Grok  2 Beta,  and  Gemini  1.5  Pro  002.  At  the  time  the  benchmark was  released,  the  best-performing  model,  Gemini  1.5  Pro, managed to solve just 2.0% of the problems-a signi fi cantly lower success rate than it achieved on other math benchmarks (Figure  2.6.7).  However,  OpenAI's  o3  model  is  reported to  have  scored  25.2%  on  the  benchmark.  The  creators  of FrontierMath  hope  the  benchmark  will  remain  a  rigorous challenge for cutting-edge AI systems for years to come.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000152_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

## 2.6 Mathematics Chapter 2: Technical Performance

## Sample problems from FrontierMath Source: Glazer et al., 2024

## conjecture

Definitions: For a positive integer n, let vp(n) denote the largest integer such that p 1.

For p a prime and a # 0 (mod p), we let ordp(a) denote the smallest positive integer such that a = (mod p). For æ &gt; 0, we let

<!-- formula-not-decoded -->

Problem. Let Sz denote the set of primes p for which

<!-- formula-not-decoded -->

and let dr denote the density

<!-- formula-not-decoded -->

of Sz in the primes. Let

<!-- formula-not-decoded -->

Compute [108do]

Answer: 367707

MSC classification: Number theory

## FrontierMath: percent solved

Source: Glazer et al., 2024; OpenAI, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000153_084f3ec5b2e37436d6cb5140d91145a36d10914005ff98c93f46f6b5880450e3.png)

Figure 2.6.7

Model

Construct a degree 19 polynomial p(æ) € C[r] such that X {p(z) p(y)} € pl x P has at least 3 (but not all linear) irreducible components over € Choose p(æ) to be odd, monic, have real coefficients and linear coefficient -19 and calculate p(19)

Answer: 1876572071974094803391179

MSC classification: 14 Algebraic geometry; 20 Group theory and generalizations; 11 Number theory generalizations

Let an for n € Zbe the sequence of integers satisfying the recurrence formula

<!-- formula-not-decoded -->

with initial conditions ai for 0 &lt; i &lt; 3. Find the smallest prime p = 4 mod 7 for which the function Z Z given by n can be extended to a continuous function on Zp

Answer: 9811

MSC classification: 11 Number theory

Figure 2.6.6

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000154_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Highlight:

## Learning and Theorem Proving

DeepMind employed its systems, AlphaProof and AlphaGeometry  2,  to  solve  four  out  of  six  problems  in the  2024  International  Mathematical  Olympiad  (IMO), achieving a performance level equivalent to that of a silver medalist. AlphaGeometry solved 25 out of 30 Olympiad geometry problems in the benchmarking set, surpassing the average score of an IMO silver medalist, who typically solves 22.9 (Figure 2.6.8). The IMO, established in 1959, is the world's oldest and most prestigious competition for young mathematicians.

AlphaProof is a reinforcement learning system derived from AlphaZero, which was previously applied to chess, shogi, and  Go.  It  trains  itself  to  solve  problems  by  generating hypotheses that are then veri fi ed using the Lean interactive proof  system.  A fi ne-tuned  Gemini  model  is  utilized  to translate natural language problem statements into formal representations, building a comprehensive training library. In this year's competition, AlphaProof successfully solved two algebra problems and one number theory problem, but failed to solve two combinatorics problems.

AlphaGeometry  2  is  a  neuro-symbolic  hybrid  system featuring a language model based on Gemini and trained on extensive synthetic data. Prior to 2024, AlphaGeometry could  solve  83%  of  historical  IMO  geometry  problems. During the 2024 competition, it solved the sole geometry problem in just 24 seconds. For the 2024 test, competition problems  were  manually  translated  into  Lean's  formal representation.

It remains unknown how AlphaProof and AlphaGeometry would perform on traditional theorem-proving benchmarks such as TPTP, which has been used since 1997 to assess the  performance  of  automatic  theorem-proving  (ATP) systems, particularly those applied to software veri fi cation. The AI Index reported on the state of ATP in its 2021 report.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000155_7fe6dafa2de881df1e9b7fa9025d68e591cff47e2570d38ef628931ff075a239.png)

## Number of solved geometry problems in IMO-AG-30

Source: Trinh et al., 2024 | Chart: 2025 AI Index report

Figure 2.6.8

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000156_917ea46ba966193849dc452bd8e48f6bfd6e3a52aea2d6db72f4bda467bd0513.png)

A 2024 update of that report, based on the latest version of TPTP containing over 25,000 problems, indicates that fully automatic systems can now solve 89% of the problems in TPTP v.9.0.0.

Ideally, TPTP systems could be tested on IMO problems, and AlphaProof and AlphaGeometry on TPTP problemssome  of  which  have  never  been  solved  by  humans,  let alone by ATP systems. Unfortunately, neither of these tests has been conducted. The primary reason is that the logics supported by the di ff erent systems di ff er signi fi cantly, and translators  between  them  do  not  yet  exist.  Additionally, while substantial, the TPTP library is not large enough to serve as a training set for AlphaProof without generating a considerable number of synthetic examples.

## Chapter 2: Technical Performance

2.7 Reasoning

Reasoning in AI involves the ability of AI systems to draw logically valid conclusions from di ff erent forms of information. AI systems are increasingly  being tested  in  diverse  reasoning  contexts,  including visual (reasoning about images), moral (understanding moral dilemmas), and social reasoning (navigating social situations).

## 2.7 Reasoning

## Sample MMMU questions

Source: Yue et al., 2023

## General Reasoning

General reasoning pertains to AI systems  being  able  to  reason  across broad,  rather  than  speci fi c,  domains. As part of a general reasoning challenge,  for  example,  an  AI  system might be asked to reason across multiple  subjects  rather  than  perform one narrow task (e.g., playing chess).

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000157_2a5a9b2a6de43ca11ac60577e9051c6f122d1271c786223429c2185833000131.png)

| Art & Design                                                                                                                                                                                                                                                                  | Business                                                                                                                                                       | Science                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Question: Among the following harmonic intervals , which one is constructed incorrectly? Options: (A) Major third <image 1> (B) Diminished fifth <image 2> Minor seventh <image 32 Diminished sixth <image 4>                                                                 | Question: collected by Gallup <image 1> Find the probability that the selected Emotional Health Index Score is betwcen 80.5 and 82? Options: (A) (B) 0.2142    | The graph shown is compiled from data  Question: <image 1> The region bounded by the shown above Choose integral expression that can be used to find the area of R Options: g(x)ldx [g(x) f(x)Jdx g(x)Jdx x(x)]dx graph |
| Subject: Music; Subfield: Music; Image Type: Sheet Music; Difficulty: Medium                                                                                                                                                                                                  | Subject: Marketing; Subfield: Market Research; Image Type: Plots and Charts; Difficulty: Medium                                                                | Subject: Math; Subfield: Calculus; Image Type: Mathematical Notations; Difficulty: Easy                                                                                                                                 |
| Health & Medicine                                                                                                                                                                                                                                                             | Humanities & Social Science                                                                                                                                    | Tech & Engineering                                                                                                                                                                                                      |
| Question: You are shown subtraction <image 1> , T2 weighled <image 2> and Tl weighted axial <image 3> from a screening breast MRL: What is the of the in the left breast? Options: Susceptibility artifact (B) Hlematoma Fat necrosis (D) Silicone granuloma ctiology finding | Qucstion: political cartoon; the United States is fulfilling which of the following roles? <image 1> Option: (A) Oppressor Imperialist Savior (D) Isolationist | Question: Find the VCE for the circuit shown in <image 1>. Neglect VBE Answer: 3.75 Explanation: .IE = [(VEE) (RE)] = [(5 V) / (4 k-ohm)] 1.25 mA; VCE VCC - IERL = 10 V (1.25 mA) 5 k-ohm; VCE                         |
| Subject: Clinical Medicine; Subfield: Clinical Radiology; Image Type: Body Scans: MRI, CT; Difficulty: Hard                                                                                                                                                                   | Subject: Subfield: Modern History; Image Type: Comics and Cartoons; Difficulty: Easy History;                                                                  | Subject: Electronics; Subfield: Analog electronics; Image Type: Diagrams; Difficulty: Hard                                                                                                                              |

## MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI

Figure 2.7.1

In  recent  years,  the  reasoning  abilities  of  AI  systems  have advanced  so  much  that  older  benchmarks  like  SQuAD  (for textual reasoning) and VQA (for visual reasoning) have become saturated, indicating a need for more challenging reasoning tests.

Responding  to  this,  researchers  from  the  United  States  and Canada recently developed  MMMU,  the massive multidiscipline multimodal understanding and reasoning benchmark for expert AGI (arti fi cial general intelligence). MMMU comprises about 11,500 college-level questions from six core disciplines: art and design, business, science, health and medicine, humanities and social science, and technology and engineering (Figure 2.7.1). The  question  formats  include  charts,  maps,  tables,  chemical structures,  and  more.  MMMU  is  among the  most  demanding tests of perception, knowledge, and reasoning in AI to date. As of January 2025, the highest-performing model is OpenAI's o1, achieving a score of 78.2%-a signi fi cant improvement from the state-of-the-art score of 59.4% reported in last year's AI Index (Figure 2.7.2). While this top score remains below the medium and  high  human  expert  baselines,  as  with  other  benchmarks covered in the Index, AI systems are rapidly closing the gap.

## MMMU on validation set: overall accuracy

Source: MMMU Leaderboard, 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000158_3ffdceabeecfd6a02abbb3cd0ad580398bcf1da8745ef30e856f38b04fbfab46.png)

Figure 2.7.2

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000159_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.7 Reasoning

## GPQA: A Graduate-Level Google-Proof Q&amp;A Benchmark

In  2023,  researchers  from  NYU,  Anthropic,  and  Meta introduced the GPQA benchmark to test general, multisubject  AI  reasoning.  This  dataset  consists  of  448 di ffi cult  multiple-choice  questions  that  cannot  be  easily answered  by  web  search.  The  questions  were  crafted by  subject-matter  experts  in  various fi elds  like  biology, physics, and chemistry (Figure 2.7.3). On the diamond setthe  most  challenging  subset  of  the  dataset  and  the  one most frequently tested  by AI  developers-human  experts achieved an accuracy rate of 81.3%.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000160_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Last  year's  AI  Index  reported  that  the  best-performing  AI model, GPT-4, achieved only 38.8% on the diamond test set. In just a year, top AI systems have made signi fi cant strides, with  OpenAI's  o3  model,  launched  in  December  2024, posting a state-of-the-art score of 87.7%, a 48.9 percentage point improvement from the state-of-the-art score in 2023 (Figure  2.7.4).  In  fact,  o3's  score  was  the fi rst  to  exceed the  baseline  set  by  expert  human  validators.  AI  systems are  rapidly  advancing  on  challenging  new  benchmarks  like MMMU and GPQA, which were recently introduced to push the limits of AI capabilities.

## Sample chemistry question from GPQA

Source: Rein et al., 2023

| Chemistry (general)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A reaction of a liquid organic compound; which molecules consist of carbon and hydrogen atoms; is performed at 80 centigrade and 20 bar for 24 hours. In the proton nuclear magnetic resonance spectrum; the signals with the highest chemical shift of the reactant are replaced by a signal of the product that is observed about three to four units downfield. Compounds from which position in the periodic system of the elements, which are also used in the corresponding large-scale industrial process; have been mostly likely initially added in small amounts? A) A metal compound from the fifth period. B) A metal compound from the fifth period and a non-metal compound from the third period. C) A metal compound from the fourth period. D) A metal compound from the fourth period and a non-metal compound from the second period. |

Figure 2.7.3

## GPQA on the diamond set: accuracy

Source: AI Index, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000161_9db2bf964143993639240191db0d3b785753ad1ba22c0c87374fe520d33972fe.png)

## Chapter 2: Technical Performance

2.7 Reasoning

## ARC-AGI

As AI systems continue to advance, claims about the imminent arrival  of  arti fi cial  general  intelligence  (AGI)  have  become more  frequent.  There  is  no  universally  accepted  de fi nition of  AGI.  Some  computer  scientists  de fi ne  it  as  AI  systems that  match  or  surpass  human  cognitive  abilities  across  a broad range of tasks. Others emphasize that the de fi nition should encompass the capacity for general learning and skill acquisition, describing AGI as a system 'capable of e ffi ciently acquiring new skills and solving novel problems for which it was neither designed nor trained.'

ARC-AGI  is  a  benchmark  introduced  in  2019  by  François Chollet,  the  creator  of  Keras,  a  popular  open-source  deep

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000162_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

learning  library.  ARC-AGI  tests  the  ability  of  systems  to generalize beyond  prior  training.  More  speci fi cally, the ARC-AGI  benchmark  presents  AI  systems  with  a  set  of independent tasks. Each task includes demonstration or input pairs followed by one or more test or output scenarios (Figure 2.7.5).  This  benchmark  emphasizes  generalized  learning ability:  It  is  impossible  for  systems  to  prepare  in  advance, as each task introduces a unique logic. The tasks require no specialized world knowledge or language skills but instead draw  on  assumed  prior  knowledge,  such  as  the  concept of  objects,  basic  topology,  and  elementary  arithmeticconcepts typically mastered by children at an early age.

## Sample ARC-AGI task

Source: Chollet et al., 2025

Figure 2.7.5

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000163_8307e86ce05d856c2bb69d1b5ec5c16a9cc877bb55cc23d2c7bfa0dfb5cd588e.png)

## 2.7 Reasoning Chapter 2: Technical Performance

ARC-AGI  has  proven  to  be  an  exceptionally  challenging benchmark. When it was fi rst run in 2020, the top-performing system achieved a score of only 20% (Figure 2.7.6). Four years later, this score had risen to just 33%. However, this year has seen substantial progress, with OpenAI's o3 model achieving a score of 75.7%. In settings where o3 was allocated a highcompute budget exceeding the benchmark's $10,000 limit, it achieved a score of 87.5%.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000164_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Researchers attribute the overall slow progress in previous years  to  an  overemphasis  on  scaling  AI  models-making them larger and feeding them increasing amounts of training data.  While  this  approach  improved  task-speci fi c skills, it  did  little  to  enhance  the  ability  of  AI  systems  to  tackle problems  without  prior  exposure  or  training data. This year's  improvements  suggest  a  shift  in  focus  toward  more meaningful advancements  in generalization and search capabilities.

ARC-AGI-1 on private evaluation set: high score

Source: Chollet et al., 2025; OpenAI, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000165_efe7d685b1370aa48453d13cb039f73e5472d7d50514be8a99739c11d3ccfc7e.png)

Figure 2.7.6

## Chapter 2: Technical Performance

2.7 Reasoning

## Humanity's Last Exam

As highlighted in both this and last year's AI Index, many  popular  AI  benchmarks,  such  as  MMLU,  GSM8K, and HumanEval,  have  reached  saturation. In response, researchers  have  developed  more  challenging  benchmarks to  better  assess  AI  capabilities.  Recently,  members  of  the team  behind  MMLU  introduced  Humanity's  Last  Exam (HLE), a new benchmark comprising 2,700 highly challenging

## Same questions on HLE

Source: Phan et al., 2025

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000166_806b9571f7f06682bc59d951e9d6bfcebdd3262ea67c5b4b51357ba53340b75b.png)

## Chemistry

Question:

endlandrlc acld B methyl ester

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000167_4dfd05ca1fa977bef9b44c4712ad6a91ff6e62b3cc0f24af09a65f98772438d1.png)

The reaction shown is a thermal pericyclic cascade that converts the starting heptaene into endiandric acid B methyl ester. The cascade involves three steps: two electrocyclizations followed by a cycloaddition. What types of electrocyclizations are involved in and step 2 and what type of cycloaddition is involved in 3? step step

Provide your answer for the electrocyclizations in the form of [nT]con or [nn]-dis (where n is the number of T electrons involved, and whether it is conrotatory or disrotatory) , and your answer for the cycloaddition in the form of [m+n] (where m and n are the number of atoms on each component)

8 Noah B

Stanford University

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000168_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

questions across dozens of subject areas (Figure 2.7.7). The dataset features multimodal questions, contributed by subject  matter  experts,  including  leading  professors  and graduate-level reviewers, that resist simple internet lookups or database retrieval. Additionally, each question was tested against state-of-the-art LLMs before inclusion; if an existing model could answer it, the question was rejected.

## Ecology

## Question:

Hummingbirds within Apodiformes uniquely have a bilaterally paired oval bone; a sesamoid embedded in the caudolateral portion of the expanded , cruciate aponeurosis of insertion of m. depressor caudae. How many paired tendons are supported by this sesamoid bone? Answer with a number.

8 Edward V

- Massachusetts Institute of Technology

## Linguistics

## Question:

am providing the standardized Biblical Hebrew source text from the Biblia Hebraica Stuttgartensia (Psalms 104:7). Your task is to distinguish between closed and open syllables. Please identify and list all closed syllables (ending in a consonant sound) based on the latest research on the Tiberian pronunciation tradition of Biblical Hebrew by scholars such as Geoffrey Khan, Aaron D. Hornkohl, Kim Phillips, and Benjamin Suchard\_ Medieval sources, such as the Karaite transcription manuscripts, have enabled modern researchers to better understand specific aspects of Biblical Hebrew pronunciation in the Tiberian tradition; including the qualities and functions of the shewa and which letters were pronounced as consonants at the ends of syllables

8 Lina B University of Cambridge

Figure 2.7.7

## Chapter 2: Technical Performance

2.7 Reasoning

Initial  testing  indicates  that  HLE  is  highly  challenging  for current  AI  systems.  Even  top  models,  such  as  OpenAI's o1,  score  just  8.8%  (Figure  2.7.8).  The  researchers  behind

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000169_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

the  benchmark  are  closely  monitoring  how  quickly  LLMs improve, and they speculate that performance could exceed 50% by the end of 2025.

## Humanity's Last Exam (HLE): accuracy

Figure 2.7.8

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000170_ba74cfe82ceb52b882fe050f1adaaa8eecc7c7ec0e2af9b0cb7a0babf7cc2084.png)

## Planning

Planning is an intelligent task that involves reasoning about  actions  that  alter  the  world.  It  requires  considering hypothetical future states, including potential external actions and other transformative events.

## PlanBench

Claims  have  been  made  that  LLMs  can  solve  planning problems. A group from Arizona State University has proposed PlanBench, a benchmark suite containing problems used in the automated planning community, especially those used in the International Planning Competition. PlanBench is designed to test LLMs on planning tasks. The benchmark tests models on 600 problems in which a hand tries to construct stacks of blocks when it is only allowed to move one block at a time to a table or to the top of a clear block. After the benchmark was released in 2022, researchers demonstrated that  models  like  GPT-4  and  GPT-3.5  still  struggled  with planning tasks.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000171_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

The release of OpenAI's o1 was met with enthusiasm from the AI research community, as it was designed to actively reason rather than function purely as an autoregressive LLM. When tested on the PlanBench benchmark, o1 showed signi fi cant improvements,  though  it  still  struggles  with  reliable  and consistent planning. In the Blocksworld zero-shot evaluation (one speci fi c planning evaluation domain), o1 achieved a score of 97.8%-far surpassing the next best LLM, Llama 3.1 405B (62.6%),  and  dramatically  outperforming  GPT-4o  (35.5%) (Figure 2.7.9). In the more challenging Mystery Blocksworld domain, where some answers are syntactically obfuscated, o1 scored 52.8% zero-shot, compared to just 0.8% for Llama 3.1 405B. GPT-4, by contrast, scored 0%.

Planning is  a  combinatorial  problem,  and  solving  problems with long solutions is expected to take more than linear time. Not  surprisingly,  when  tested  on  instances  that  require  at least 20 steps, o1 manages to solve just 23.6%.

## PlanBench: instances correct

Source: Valmeekam et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000172_887f476e75c130ecb0cd4f0ce132e59c0c2ca6918dce145916b370c9f9feddf9.png)

## 2.8 AI Agents Chapter 2: Technical Performance

AI agents, autonomous or semiautonomous systems designed to operate within  speci fi c  environments to accomplish goals, represent an  exciting  frontier in  AI  research. These agents have a diverse range of potential  applications,  from  assisting in  academic research and scheduling meetings to facilitating online shopping  and  vacation  booking.  As suggested by many recent corporate releases,  agentic  AI  has  become  a topic of increasing interest in the technical world of AI.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000173_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

## 2.8 AI Agents

For decades, the topic of AI agents has been widely discussed in the AI community, yet few benchmarks have achieved widespread adoption, including those featured in last year's Index, such as AgentBench and MLAgentBench. This is partly due to the  inherent  complexity  of  benchmarking  agentic tasks, which  are typically  more diverse,  dynamic,  and  variable  than  tasks  like  image  classi fi cation  or  answering language questions. As AI continues to evolve, it will become important to develop e ff ective methods to evaluate AI agents.

## VisualAgentBench

VisualAgentBench  (VAB),  launched  in  2024,  represents  a signi fi cant step forward in the evaluation of agentic AI. This benchmark re fl ects the growing multimodality of AI models and their increasing pro fi ciency in navigating both virtual and embodied environments. VAB addresses the need to assess agent  performance  in  diverse  settings  that  extend  beyond environments  reliant  solely  on  linguistic  commands.  VAB

tests agents across three broad categories of tasks: embodied agents (operating  in  household  and  gaming  environments), GUI agents (interacting with mobile and web applications), and visual  design  agents  (such  as  CSS  debugging)  (Figure 2.8.1). This comprehensive approach creates a robust evaluation  suite  of  agents'  capabilities  across  varied  and dynamic contexts.

## Tasks on VisualAgentBench

Source: Liu et al., 2024

Figure 2.8.1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000174_64abdfca938ec11876b9dddd1baf26a97d8f8cc2cf85fd75f83be64203fc5305.png)

## 2.8 AI Agents Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000175_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

VAB presents a signi fi cant challenge for AI systems. The topperforming model, GPT-4o, achieves an overall success rate of just 36.2%, while most proprietary language models average around  20%  (Figure  2.8.2).  According  to  the  benchmark's authors, these results reveal that current AI models are far from ready for direct deployment in agentic settings.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000176_dbea6418c1ac31b1272aa3b077dbf03de6567f9616ed9152896fdb36572fe8c8.png)

Figure 2.8.2

## RE-Bench

The emergence of increasingly capable agentic AI systems has fueled predictions that AI might soon take on the work of computer scientists or  researchers.  However,  until  recently, there were few benchmarks designed to rigorously test the R&amp;D capabilities of top-performing AI systems.  In  2024,  researchers  addressed this gap with the launch of RE-Bench, a benchmark featuring  seven  challenging,  open-ended  ML research environments. These tasks, informed by  data  from  71  eight-hour  attempts  by  over 60 human experts, include optimizing a kernel, conducting a scaling law experiment, and fi netuning GPT-2 for question answering, among others (Figure 2.8.3).

## RE-Bench Process and Flow

Source: Wijk et al., 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000177_41568d9feed9f7039945540e7c314de0c461c3b886f3e47968666f70882b9033.png)

Figure 2.8.3

## 2.8 AI Agents Chapter 2: Technical Performance

Researchers uncovered two key fi ndings when comparing the performance of humans and frontier AI models. In short time horizon settings, such as with a two-hour budget, the best AI systems achieve scores four times higher than human experts (Figure 2.8.4). However, as the time budget increases, human performance begins to surpass that of AI. With an eight-hour budget, human performance slightly exceeds AI, and with a

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000178_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

32-hour budget, humans outperform AI by a factor of two. The  researchers  also  note  that  for  certain  tasks,  AI  agents already  demonstrate  expertise  comparable  to  humans  but can  deliver  results  signi fi cantly  faster  and  at  a  lower  cost. For example, AI agents can write custom Triton kernels more quickly than any human expert.

RE-Bench: average normalized score@k

Source: Wijk et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000179_8a296b599ea4aaf83898acfe9903e51642410c0652548b5bb2cf532faf0c90bc.png)

## 2.8 AI Agents Chapter 2: Technical Performance

## GAIA

GAIA is a benchmark for General AI assistants introduced  by  Meta  in  May  2024.  It  consists  of  466 questions  designed  to  assess  AI  systems'  ability  to perform  a  broad  range  of  tasks,  including  reasoning, multimodal  processing,  web  browsing,  and  tool  use. Unlike straightforward, exam-style questions,  GAIA challenges AI models with complex, multistep problems that may require searching the open web, interpreting multimodal inputs, and reasoning  through intricate scenarios  (Figure  2.8.5).  When  researchers  launched GAIA, they found that existing LLMs lagged signi fi cantly behind human performance. For instance, GPT-4 with plugins  correctly  answered  only  15%  of  the  questions, compared to 92% for human respondents.

As  with  other  recently  introduced  AI  benchmarks, performance on GAIA has improved rapidly. In 2024, the top system achieved a score of 65.1%, marking a roughly 30  percentage  point  increase  from  the  highest  score recorded in 2023 (Figure 2.8.6).

## Sample questions on GAIA

Source: Meta, 2024

## Level 1

Question:   What was the actual enrollment count of the clinical trial on H. pylori in acne vulgaris patients from Jan-May 2018 as listed on the NIH website? Ground truth: 90

## Level 2

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000180_19c97ad39bc6ae4cc3cff8b6a09577818251f334ef3aec5a5798d2417cb7f11e.png)

Question: If this whole pint is made up of ice cream, how many percent above or below the US federal standards for butterfat content is it when using the standards as reported by Wikipedia in 2020? Answer as + or a number rounded to one decimal place. Ground truth: +4.6

## Level 3

on 2006 January 21, two astronauts are visible, with one appearing much smaller than the other:. As of August 2023, out of the astronauts in the NASA Astronaut Group that the smaller astronaut was a member of, which one spent the least time in space; and how many minutes did he in space, rounded to the nearest minute? Exclude any astronauts who did not any time in space.  Give the Ground truth: White; 5876 Day spend spend

Figure 2.8.5

## GAIA: average score

Source: GAIA Leaderboard, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000181_6994550ad69bdd643e82f9fa0632c639b721f1a9203d3f99ce25a302a2f62ae7.png)

Figure 2.8.6

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000182_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

## 2.9 Robotics and Automous Motion

Advancements  in  AI  over  the  past decade have paved the way for exciting new developments in the fi eld  of  robotics.  Especially  with  the rise of foundation models, robots are  now  able to  iteratively  learn  from their  surroundings,  adapt fl exibly  to new  settings,  and  make  autonomous decisions.  This  section  explores  key robotic benchmarks and recent trends, including the rise of humanoids, algorithmic advancements from DeepMind, and the emergence of robotic foundation models. It concludes  by  studying  developments in self-driving cars.

## 2.9 Robotics and Autonomous Motion

## Robotics

## RLBench

One of the most widely adopted benchmarks in the robotics community is RLBench (Robot Learning Benchmark). Launched in 2019, it features 100 unique tasks of varying complexity, from simple target reaching to opening an oven and placing a tray inside. 12 Researchers typically evaluate new robotic systems on a standardized subset of 18 tasks to gauge performance. Figure 2.9.1 visualizes some of the tasks in RLBench.

## Tasks on VisualAgentBench

Source: James et al., 2019

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000183_81079a343b37bec37365c13321c1391b0daebf40f5bcd4bc197c943430da885a.png)

Figure 2.9.1

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000184_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

As of January 2025, the top-performing model on this subset is  SAM2Act,  a  collaboration  between  researchers  at  the University  of  Washington,  Universidad  Católica  San  Pablo, Nvidia,  and  the  Allen  Institute  for  AI.  SAM2Act  achieved

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000185_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

an  86.8%  success  rate,  marking  a  2.8  percentage  point improvement over the previous state-of-the-art in 2024 and a 66.7 percentage point increase from the leading score in 2021 (Figure 2.9.2).

## RLBench: success rate (18 tasks, 100 demo/task)

Source: Papers With Code, 2025 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000186_998c7f44adac2644bf4ffb408bf4804f115e39a2fa7ab9b429ea5336066682ca.png)

Figure 2.9.2

## Chapter 2: Technical Performance

## Highlight:

## Humanoid Robotics

2024  was  a  signi fi cant  year  for  robotics,  marked  by  the growing  prevalence  of  humanoid  robots-machines  with humanlike  bodies  designed  to  mimic  human  functions. For  example,  Figure  AI,  a  robotics  startup  dedicated  to developing  general-purpose  humanoid  robots,  launched Figure 02 in 2024, its most advanced model yet. Standing 5 feet 6 inches tall, weighing 154 pounds, and capable of handling  a  44-pound  payload,  Figure  02  operates  for  up to fi ve  hours  on  a  single  charge.  Figure  robots  are  able to  perform  complex  tasks  such  as  making  co ff ee  and assisting  in  automotive assembly by placing sheet metal into a car fi xture (Figure 2.9.3 and Figure 2.9.4). They are also integrated with OpenAI and can engage in speech-tospeech reasoning, whereby the robot explains its actions and responds to queries about its behavior. Figure's success follows  that  of  other  companies  that  released  humanoid robots,  like  T esla's  Optimus, fi rst  launched  in  2002  and redesigned in 2023, and Boston Dynamics' Atlas humanoid.

Figure robot making co ff ee Source: Figure AI

Figure 2.9.3

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000187_615b1ac6b975ae81de7534a78fbfa2d7f7d5d1d582290ec17b54ff9a70548a9e.png)

Figure robot assisting in automotive assembly Source: Figure AI

Figure 2.9.4

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000188_8b8834ee0e857ac32bc3f9c93f839365df0c0aef4feeab335ef868820530c65d.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000189_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

## Highlight:

## DeepMind's Developments

In 2023, DeepMind launched two robotic models, PaLM-E and RT-2. These models were novel in their use of  transformer-based  architectures,  typically  found  in language modeling, and their training on both manipulation data  and  language  data.  This  dual  training  approach enabled them to excel at both robotic manipulation and text  generation. In 2024, DeepMind introduced AutoRT, an AI  system that  leverages  large  foundation  models to autonomously generate diverse training  data for  robots. It  coordinates  multiple  video-equipped  robots,  guiding them  through  various  environments,  devising  creative tasks for them to perform, and meticulously documenting these tasks (Figure 2.9.5). This documentation then serves as training data for future robotic learning. To date, AutoRT has generated a dataset of 77,000 robotic trials spanning 6,650 unique tasks.  Greater  amounts  of  robotic training data  will  be  important  to  improve  the  training  of  future robotic systems.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000190_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## AutoRT work fl ow

Source: Google DeepMind, 2024

Conversely, SARA-RT,  also  from  Google  DeepMind, improves  the  e ffi ciency  of  transformer-based  robotic models  by  signi fi cantly  improving  their  speed.  While transformers are powerful, they are also computationally intensive  as  they  rely  on  quadratic  complexity  attention mechanisms. This means that doubling the input size of data  provided to  a  model  can  quadruple  computational requirements.  This  challenge  complicates  attempts  to scale robotic models. SARA-RT addresses this challenge

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000191_80fe6bc9d56c7f2e0632fa9ea3d407e85be03b3aa199123b54297fdedd998548.png)

Figure 2.9.5

with  a  technique  called  'up-training,'  which  converts  the quadratic  complexity  of  standard  transformers  into  a  linear model. This method drastically reduces computational demands while maintaining performance quality. Figure 2.9.6 compares speed tests of AI models enhanced with the SARA technique  against  those  without.  In  point  cloud  processing,

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000192_ef6b24eab9467b0c18dfb9c4ddbcb082fb16b1608fc56943251107315827dc17.png)

## Chapter 2: Technical Performance

## Highlight:

## DeepMind's Developments (cont'd)

which  enables  robots  to  interpret  3D  environments,  and  in image processing, SARA-based models run signi fi cantly faster while avoiding major increases in run-time at scale.

Other developments from DeepMind include ALOHA (Autonomous Learning of High-level Activities) and DemoStart. ALOHA Unleashed is a breakthrough in enabling robots  to  perform  intricate  dexterous  manipulation  tasks, such as tying shoelaces or hanging T-shirts on coat hangers- tasks  that  historically  have  been  extremely  challenging  for robots. The researchers demonstrated that combining a large imitation learning dataset with a transformer-based learning architecture  is  a  highly  e ff ective  approach  for  overcoming these  di ffi culties.  The  ALOHA  approach  enabled  Google's robot to e ff ectively learn a diverse range of tasks, including hanging a shirt, stacking kitchen items, and tying shoelaces (Figure 2.9.7). As shown in Figure 2.9.8, ALOHA-trained robots achieved a high success rate across these tasks.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000193_e3d0ad60a7c89e99a8d7e505df58f9a0b15e058f2bffbd5544ff126aab578ebd.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000194_7fe6dafa2de881df1e9b7fa9025d68e591cff47e2570d38ef628931ff075a239.png)

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

## Highlight:

## DeepMind's Developments (cont'd)

Similarly,  DemoStart  introduces  a  novel  auto-curriculum reinforcement learning method that enables a robotic arm to  master  complex  behaviors  using  only  sparse  rewards and a limited number of demonstrations. This breakthrough highlights the potential for robots to learn e ffi ciently with minimal data, reducing the need for data-intensive training and making advanced robotics more accessible and widely

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000195_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

adopted.  DeepMind  also  introduced  a  robotic  model  in 2024 that was capable of reaching amateur human-level performance  in  competitive  table  tennis  (Figure  2.9.9). Given that achieving human-level speed and performance on real-world tasks is an important benchmark for robotics research,  this  achievement  is  a  notable  step  forward  in robotic ability.

## Robots playing amateur-level table tennis

Source: Google DeepMind, 2024

Figure 2.9.9

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000196_2ca9cff24cd658e86ee56dd90728ef6a09f6b8686f184b70507ba689daacb390.png)

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

## Highlight:

## Foundation Models for Robotics

In  2024,  there  was  a  strong  push  toward  developing foundational  models  for  robotics-systems  capable  of reasoning with language while physically operating in the real  world.  Nvidia  introduced  GR00T  (Generalist  Robot 00  Technology),  a  general-purpose  foundation  model for  humanoid  robots  designed  to  understand  natural language and mimic human  movements.  Alongside GR00T, Nvidia released data pipelines, simulation frameworks,  and  the  Thor  robotics  computer.  Figure 2.9.10 illustrates the components of GROOT's launch. This robotic development suite is intended to make it easier for the robotic community to scale and build increasingly advanced robotics.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000197_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Nvidia was not alone in this space. Covariant launched RFM-1, a robotic foundation model with language capabilities  and  real-world  maneuverability.  Meanwhile, LLaRA, developed by researchers at Stony Brook University  and  the  University  of  Wisconsin-Madison, integrates  perception,  communication,  and  action  into a  monolithic,  end-to-end  deep  learning  model.  These new models continue a trend from 2023, which saw the launch of robotic foundation models like RT-2, PaLM-E, and Open-X Embodiment.

## GROOT blueprint for synthetic motion generation

Source: Nvidia, 2024

Figure 2.9.10

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000198_a17133cd6d61bee855572dcecb0d996a199bcfc4ddf1ff00b1169fc76df76a7c.png)

## Chapter 2: Technical Performance

## Self-Driving Cars

Self-driving vehicles have long been a goal for AI researchers and technologists. However, their widespread adoption has been  slower  than  anticipated.  Despite  many  predictions that  fully  autonomous  driving  is  imminent,  widespread  use of  self-driving  vehicles  has yet  to  become  a  reality.  Still,  in recent  years,  signi fi cant  progress  has  been  made.  In  cities like  San  Francisco  and  Phoenix, fl eets  of  self-driving  taxis are  now  operating  commercially.  This  section  examines recent advancements in autonomous driving, focusing on deployment, technological breakthroughs and new benchmarks, safety performance, and policy challenges.

## Deployment

Self-driving cars are increasingly being deployed worldwide. Cruise, a subsidiary of General Motors, launched its autonomous vehicles  in  San  Francisco  in  late  2022  before having its license suspended in 2023 after a litany of safety incidents. Waymo, a subsidiary of Alphabet, began deploying its  robotaxis in Phoenix in early 2022 and expanded to San Francisco in 2024. The company has since emerged as one of the more successful players in the self-driving industry: As of January 2025, Waymo operates in four major U.S. citiesPhoenix,  San  Francisco,  Los  Angeles,  and  Austin  (Figure 2.9.11). Data sourced from October 2024 suggests that across the four cities the company provides 150,000 paid rides per week, covering over a million miles. Looking ahead, Waymo plans to test its vehicles in 10 additional cities, including Las Vegas,  San  Diego,  and  Miami.  The  company  chose  testing locations, such as upstate New York and Truckee, California, that experience snowy weather so it can assess the vehicles in  diverse  driving  conditions.  There  has  also  been  notable progress  in  self-driving  trucks,  with  companies  like  Kodiak completing its fi rst driverless deliveries and Aurora reporting steady  advancements,  including  over  1  million miles of autonomous freight  hauling  on  U.S.  highways  since  2021albeit  with  human  safety  drivers  present.  Still,  challenges remain  in  bringing  this  technology  to  market,  with  Aurora recently announcing it would delay the commercial launch of its fl eet from the end of 2024 until April 2025.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000199_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Waymo rider-only miles driven without a human driver

Source: Waymo, 2024 | Table: 2025 AI Index report

| LRFDWLRQ                | 5LGHUGLYPH<c=16,font=/AAAANM+CircularStd-Bold>RQO\GLYPH<c=3,font=/AAAANM+CircularStd-Bold>PLOHVGLYPH<c=3,font=/AAAANM+CircularStd-Bold>WKURXJK 6HSWHPEHUGLYPH<c=3,font=/AAAANM+CircularStd-Bold>GLYPH<c=21,font=/AAAANM+CircularStd-Bold>GLYPH<c=19,font=/AAAANM+CircularStd-Bold>GLYPH<c=21,font=/AAAANM+CircularStd-Bold>GLYPH<c=23,font=/AAAANM+CircularStd-Bold>   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L o s A n g e l e s     | 1 . 9 4 7 M                                                                                                                                                                                                                                                                                                                                                            |
| S a n F r a n c i s c o | 1 0 . 20 9 M                                                                                                                                                                                                                                                                                                                                                           |
| P h o e n i x           | 20 . 823 M                                                                                                                                                                                                                                                                                                                                                             |
| A u s t i n             | 1 2 4 K                                                                                                                                                                                                                                                                                                                                                                |

Figure 2.9.11

China's  self-driving  revolution  is  also  accelerating,  led  by companies like Baidu's Apollo Go, which reported 988,000 rides across China in Q3 2024, re fl ecting a 20% year-over-year increase. In October 2024, the company was operating 400 robotaxis and announced plans to expand its fl eet to 1,000 by the end of 2025. Pony.AI, another Chinese autonomous vehicle manufacturer, has pledged to scale its robotaxi fl eet from 200 to at least 1,000 vehicles-with expectations that the fl eet will reach 2,000 to 3,000 by the end of 2026. China is leading the way in autonomous vehicle testing, with reports indicating  that  it  is  testing  more  driverless  cars  than  any other country and currently rolling them out across 16 cities. Robotaxis  in  China  are  notably  a ff ordable-even  cheaper, in  some  cases,  than  rides  provided  by  human  drivers.  To support  this growth, China  has prioritized establishing national regulations to govern the deployment of driverless cars.  Beyond the self-driving  revolution taking  place  in the U.S. and China, European startups like Wayve are beginning to gain traction in the industry.

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

## Technical Innovations and New Benchmarks

Over  the  past  year,  self-driving  technology  has  advanced signi fi cantly,  both  in  vehicle  capabilities  and  benchmarking methods.  In  October  2024,  Tesla  unveiled  the  Cybercab,  a two-passenger autonomous vehicle without a steering wheel or  pedals,  which  is  set  for  production  in  2026  at  a  price  of under $30,000. Tesla also  unveiled the  Robovan,  an  electric autonomous van designed to transport up to 20 passengers. Meanwhile, Baidu's Apollo Go launched its latest-generation robotaxi, the RT6, across multiple cities in China (Figure 2.9.12). With a price tag of just $30,000 and a battery-swapping system, the  RT6  represents  a  major  step  toward  making  self-driving technology more cost-e ff ective and scalable. As costs continue to decline, the adoption of autonomous vehicles is expected to accelerate. Notable business partnerships have also advanced self-driving  technology,  including  Uber's  collaboration  with WeRide-the world's fi rst publicly listed robotaxi companyto develop an autonomous ride-sharing platform in Abu Dhabi.

In 2024, several new benchmarks were introduced to evaluate self-driving capabilities. One  notable example  is nuPlan, developed by Motional. It is a large-scale, autonomous driving dataset designed to test machine-learning-based motion planners.  The  benchmark  includes  1,282  hours  of  diverse driving scenarios from multiple cities, along with a simulation and  evaluation  framework  that  enables  planners'  actions  to be tested in closed-loop settings. Another recent benchmark is  OpenAD,  the fi rst  real-world,  open-world  autonomous driving benchmark for 3D object detection. OpenAD focuses on domain generalization-the ability of autonomous driving systems to  adapt  across  diverse  sensor  con fi gurations-and open-vocabulary recognition, which allows systems to identify previously unseen semantic categories.

## An overview of Bench2Drive

Source: Jia et al., 2024

Figure 2.9.13

Baidu's RT-6 Source: Verge, 2024

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000200_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

Figure 2.9.12

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000201_9b2b6205c26ef41aef4114c81d09d518035c02b18306a874d355a46289e449ce.png)

Most existing benchmarks  for end-to-end autonomous driving rely on open-loop evaluation, which can be restrictive. Open-loop settings fail to test how autonomous agents  react  to  real-world  conditions  and  often  lead  to models that memorize driving patterns rather than learning to  drive  authentically.  While  closed-loop  benchmarks  like Town05Long and Longest6 exist, they primarily assess basic driving skills rather than performance in complex, interactive scenarios.  Bench2Drive  is  another  new  benchmark  that improves on these limitations by providing a comprehensive, realistic, closed-loop testing simulation environment for endto-end  autonomous  vehicles  (Figure  2.9.13).  It  includes  a training set with over 2 million fully annotated frames sourced from more than 10,000 clips, as well as an evaluation suite with 220 short routes designed to test autonomous driving capabilities in diverse conditions. Figure  2.9.14 displays the  driving  scores  of  various  autonomous  driving  methods evaluated on the Bench2Drive benchmark. 13

1. Strong Expert Unified &amp; Diverse LargeScale Training Set

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000202_3aa80532d8b35a1249c8883b2fb8a4613a2438d6b1bbe847b5db9de877181baf.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000203_702f7444e093313d680ffbe084c92189ceffd02258c4f4d33547f73cdae941fd.png)

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000204_5719d5cc3d371c0d60197b3a11e28a21ce0d9e2ab2e3cc5adc006ad52458f46c.png)

2. Quasi-Realistic Scenario Closed-Loop (E2E) Evaluation

Multi-dimensional Ability Assessment

13 This metric accounts for both route completion and infractions, averaging route completion percentages while applying penalties based on infraction severity. For more detail on the driving score methodology, see Section 3 of the Bench2Drive paper .

## Chapter 2: Technical Performance

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000205_b0bb4348efc1a7d526b1d1edb38b00657fdcab0ed1579ff817abfe336570f57c.png)

2.9 Robotics and Automous Motion

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000206_2aefc4fbe24b88323284096026c8ed56e36caace03479e7cace884d7d0b7730b.png)

## Safety Standards

Emerging  research  suggests  that  self-driving  cars  may  be safer  than  human-driven  vehicles.  Figure  2.9.15  compares the number of reported incidents per million miles driven by Waymo vehicles to the estimated rates if humans had driven the  same  distance.  The  data  shows  that  Waymo  vehicles had signi fi cantly fewer incidents, including 1.42 fewer airbag deployments, 3.16 fewer crashes with reported injuries, and

3.65 fewer police-reported crashes per million miles (Figure 2.9.15).  Figure  2.9.16  highlights  the  di ff erences  in  incident rates across various crash locations, revealing that across all locations  with  available  data,  Waymo  vehicles  consistently recorded lower rates of airbag deployments, injury-reported crashes, and police-reported incidents.

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

## Waymo driver vs. human benchmarks in Phoenix and San Francisco

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000207_085ddcde5df81fe9a5c8c30001cbfe84a70f3367b978e45f91c65c58455ed76d.png)

Figure 2.9.15 14

## Waymo driver percent diǄerence to human benchmark in Phoenix and San Francisco

Source: Waymo, 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000208_2bcfb8cdb4bcbb7525e7897ee637fe04aafe849057925c9992b5cde107929b30.png)

14 Waymo's safety data is continuously updated in real time, so the totals reported in this section may not fully align with those currently displayed on their website.

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000209_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)

## Chapter 2: Technical Performance

2.9 Robotics and Automous Motion

Waymo,  in  collaboration  with  Swiss  Re,  one  of  the  world's leading reinsurers, also conducted a study analyzing liability claims related to collisions over several million miles driven by its fully autonomous vehicles. The study compared Waymo's liability claims to human-driver baselines derived from Swiss Re's  extensive  dataset,  which  includes  over  500,000  claims and 200 billion miles of driving data. The results showed that Waymo vehicles had an 88% reduction in property damage claims  and  a  92%  reduction  in  bodily  injury  claims  (Figure 2.9.17). In real terms, across 25.3 million miles driven, Waymo vehicles were involved in just nine property damage claims and two bodily injury claims, whereas human drivers over the same distance  would  be  expected  to  incur  78  property  damage claims and 26 bodily injury claims. The Waymo drivers were also  signi fi cantly  safer  than  latest-generation  human-driven vehicles that are equipped with added safety features.

## Comparison of liability insurance claims by type: Waymo driver vs. human-driven vehicles

Source: Di Lillo et al., 2024 | Chart: 2025 AI Index report

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000210_b063c4f0e8d2584fe2c1e1a1d4563c305df95af972f615212aeb3f9ba082e6f5.png)

Figure 2.9.17

![Image](hai_ai_index_report_2025_chapter_2-parsed-w-imgs_artifacts/image_000211_75b618b84a50065a5ffd19997404edddf41e30325da5200790a6e2bcefcd05cb.png)