APP_NAME = "生成AI英会話アプリ"
MODE_1 = "日常英会話"
MODE_2 = "シャドーイング"
MODE_3 = "ディクテーション"
USER_ICON_PATH = "images/user_icon.jpg"
AI_ICON_PATH = "images/ai_icon.jpg"
AUDIO_INPUT_DIR = "audio/input"
AUDIO_OUTPUT_DIR = "audio/output"
PLAY_SPEED_OPTION = [2.0, 1.5, 1.2, 1.0, 0.8, 0.6]
ENGLISH_LEVEL_OPTION = ["初級者", "中級者", "上級者"]

# 英語講師として自由な会話をさせ、文法間違いをさりげなく訂正させるプロンプト
SYSTEM_TEMPLATE_BASIC_CONVERSATION = """
    You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user. If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
"""
SYSTEM_TEMPLATE_BASIC_CONVERSATION_INTERMEDIATE = """
    You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user. If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
"""







# 約15語のシンプルな英文生成を指示するプロンプト
SYSTEM_TEMPLATE_CREATE_PROBLEM = """
    Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
    - Casual conversational expressions
    - Polite business language
    - Friendly phrases used among friends
    - Sentences with situational nuances and emotions
    - Expressions reflecting cultural and regional contexts

    Limit your response to an English sentence of approximately 15 words with clear and understandable context.
 
"""
#中級英文作成プロンプト
SYSTEM_TEMPLATE_CREATE_PROBLEM_INTERMEDIATE = """
    Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
    - Casual conversational expressions
    - Polite business language
    - Friendly phrases used among friends
    - Sentences with situational nuances and emotions
    - Expressions reflecting cultural and regional contexts

    Limit your response to an English sentence of approximately 25 words with clear and understandable context.
    
"""
#上級英文作成プロンプト
SYSTEM_TEMPLATE_CREATE_PROBLEM_ADVANCED = """
    Generate 2 sentence that reflect natural English used in daily conversations, workplace, and social settings:
    - Casual conversational expressions
    - Polite business language
    - Friendly phrases used among friends
    - Sentences with situational nuances and emotions
    - Expressions reflecting cultural and regional contexts

    Limit your response to an English sentence of approximately 50 words with clear and understandable context.

"""

#問題文と回答を比較し、評価結果の生成を支持するプロンプトを作成アドバンス
SYSTEM_TEMPLATE_EVALUATION_ADVANCED = """
    あなたは英語学習の専門家です。
    以下の「LLMによる問題文」と「ユーザーによる回答文」を比較し、分析してください：

    【LLMによる問題文】
    問題文：{llm_text}

    【ユーザーによる回答文】
    回答文：{user_text}

【評価方針】
    語順・語彙・主要語の一致を重視。意訳は減点対象。
    スペル・句読点・大文字小文字も評価対象。完全一致に近いほど高評価。
【出力フォーマット（日本語）】
【評価】
✓ 良かった点：
- （箇条書きで2〜4項目）
△ 改善が必要な点：
- （箇条書きで2〜4項目）

【詳細】
- 単語の正確性：主要語の一致/脱落/置換を簡潔に指摘
- 文法の正確性：品詞/時制/一致/冠詞/前置詞など
- 文の完成度：意味の通りやすさ、情報の欠落や冗長さ

【スコア】  # 0〜100、整数
- 語彙一致：100
- 文法：100
- 完成度：100
- 総合：100  

【アドバイス】
- 次回に向けた具体的な練習ポイントを1〜3行

【励まし】
- ユーザーの努力を認める1文

【禁止事項】
- 参照文と無関係な新情報の追加をしない
- ユーザー発話の意味を大きく変える修正提案をしない
- 冗長な説明や専門用語の多用を避け、簡潔に

"""










SYSTEM_TEMPLATE_EVALUATION_INTERMEDIATE = """
    あなたは英語学習の専門家です。
    以下の「LLMによる問題文」と「ユーザーによる回答文」を比較し、分析してください：

    【LLMによる問題文】
    問題文：{llm_text}

    【ユーザーによる回答文】
    回答文：{user_text}

    【分析項目】
    1. 単語の正確性（誤った単語、抜け落ちた単語、追加された単語）
    2. 文法的な正確性
    3. 文の完成度

    フィードバックは以下のフォーマットで日本語で提供してください：

    【評価】 # ここで改行を入れる
    ✓ 正確に再現できた部分 # 項目を複数記載
    △ 改善が必要な部分 # 項目を複数記載
    
    【アドバイス】
    次回の練習のためのポイント

    ユーザーの努力を認め、前向きな姿勢で次の練習に取り組めるような励ましのコメントを含めてください。
"""