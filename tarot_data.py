import random

# Build a full 78-card deck: 22 Major Arcana + 56 Minor Arcana
MAJOR = [
    ("愚者", "The Fool"), ("魔术师", "The Magician"), ("女祭司", "The High Priestess"),
    ("女皇", "The Empress"), ("皇帝", "The Emperor"), ("教皇", "The Hierophant"),
    ("恋人", "The Lovers"), ("战车", "The Chariot"), ("力量", "Strength"), ("隐者", "The Hermit"),
    ("命运之轮", "Wheel of Fortune"), ("正义", "Justice"), ("倒吊人", "The Hanged Man"),
    ("死神", "Death"), ("节制", "Temperance"), ("恶魔", "The Devil"),
    ("高塔", "The Tower"), ("星", "Star"), ("月", "Moon"), ("太阳", "Sun"),
    ("审判", "Judgement"), ("世界", "The World")
]

SUITS = [
    ("权杖", "Wands"),
    ("圣杯", "Cups"),
    ("宝剑", "Swords"),
    ("钱币", "Pentacles"),
]

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "侍从", "骑士", "女王", "国王"]

def _minor_meaning(suit_cn, rank):
    # More detailed two-sentence template meanings for upright/reversed
    base = f"{suit_cn} {rank}"
    if rank == 'A':
        return (
            f"{base}：代表新的机会或创意的萌发，潜力巨大，适合开始行动。",
            f"{base}：可能被错过或尚未成熟，需要等待时机或更多准备。",
        )
    if rank in ['2','3','4']:
        return (
            f"{base}：强调协作、学习与渐进式成长，稳定且可期待成果。",
            f"{base}：合作受阻或沟通不良，需调整期待并回到基础建设。",
        )
    if rank in ['5','6','7']:
        return (
            f"{base}：提示冲突、考验或竞争，需坚持原则并灵活应对。",
            f"{base}：斗争或选择可能导致疲惫或失利，需审慎权衡代价。",
        )
    if rank in ['8','9','10']:
        return (
            f"{base}：表示努力带来成熟与收获，成果明显但仍需守护。",
            f"{base}：过劳、守成不力或资源耗尽的信号，需要调整节奏与优先级。",
        )
    if rank == '侍从':
        return (
            f"{base}：象征消息、探索与学习的开始，带来好奇与灵感。",
            f"{base}：可能表现为幼稚或误导，信息需核实后再行动。",
        )
    if rank == '骑士':
        return (
            f"{base}：代表行动力与前进的动力，适合追求目标与推进计划。",
            f"{base}：急躁或冲动带来的风险，建议放慢速度并评估路线。",
        )
    if rank == '女王':
        return (
            f"{base}：象征关怀、成熟的情感力量与直觉判断，善于支持他人。",
            f"{base}：情绪主导或过度保护，需建立界限并照顾自身需求。",
        )
    if rank == '国王':
        return (
            f"{base}：体现掌控、实践与领导力，稳重且能带来结构化成果。",
            f"{base}：可能变得专制或冷漠，提醒以智慧和同理心领导。",
        )
    return (f"{base}：详尽含义。", f"{base}：逆位的详细含义。")

CARDS = []

# Detailed Major Arcana meanings (upright, reversed)
MAJOR_MEANINGS = {
    0: (
        "愚者：正位 — 跳入未知，信任旅程与直觉，新的开始充满可能性。",
        "愚者：逆位 — 轻率或准备不足，提醒回顾风险并审慎决定。",
    ),
    1: (
        "魔术师：正位 — 能量与资源合一，具创造力并能将想法付诸行动。",
        "魔术师：逆位 — 能力被滥用或资源分散，需要集中与诚实。",
    ),
    2: (
        "女祭司：正位 — 倾听直觉与潜意识，内在智慧正在显现。",
        "女祭司：逆位 — 隐匿或与直觉断开，提醒寻找内在真相。",
    ),
    3: (
        "女皇：正位 — 丰盛、滋养与创造的能量，适合培育项目或关系。",
        "女皇：逆位 — 过度依赖或创作阻滞，需照顾个人界限与节奏。",
    ),
    4: (
        "皇帝：正位 — 结构、制度和稳固的领导力，有助建立秩序。",
        "皇帝：逆位 — 控制欲或僵化，提醒以柔性带来更好效果。",
    ),
    5: (
        "教皇：正位 — 传统、学习与寻求指导的时机，价值观显著。",
        "教皇：逆位 — 质疑权威或对传统反感，需寻找个人信念。",
    ),
    6: (
        "恋人：正位 — 重要的选择或亲密关系带来和谐与成长。",
        "恋人：逆位 — 冲突或优柔寡断，需厘清价值观与真实所需。",
    ),
    7: (
        "战车：正位 — 意志力强烈，适合集中力量突破阻碍。",
        "战车：逆位 — 方向混乱或失控，需要重整目标与方法。",
    ),
    8: (
        "力量：正位 — 以温柔与勇气驾驭挑战，内在力量增强。",
        "力量：逆位 — 自我怀疑或滥用力量，需回归同理心与耐心。",
    ),
    9: (
        "隐者：正位 — 反思与独处带来洞见，适合沉淀与寻求真相。",
        "隐者：逆位 — 孤立或逃避，需重新建立与他人的连接。",
    ),
    10: (
        "命运之轮：正位 — 机遇与转变的循环，顺应变化有利。",
        "命运之轮：逆位 — 延迟或阻碍，提醒耐心与调整期待。",
    ),
    11: (
        "正义：正位 — 公平、因果与清晰判断，适合处理法律或契约事务。",
        "正义：逆位 — 偏见或不公平，需寻找真相并承担责任。",
    ),
    12: (
        "倒吊人：正位 — 改变视角、放手或暂停以获得新的理解。",
        "倒吊人：逆位 — 抵抗放下或滞留，需要行动或重新评估。",
    ),
    13: (
        "死神：正位 — 结束带来新生，必要的转化与更新。",
        "死神：逆位 — 抗拒改变导致停滞，鼓励接受循环。",
    ),
    14: (
        "节制：正位 — 调和、耐心與整合不同元素以达平衡。",
        "节制：逆位 — 失衡或极端，提醒回归中庸与节制。",
    ),
    15: (
        "恶魔：正位 — 面对束缚或诱惑，识别依附与习惯性的模式。",
        "恶魔：逆位 — 逐渐解脱或认清桎梏，踏上自由之路。",
    ),
    16: (
        "高塔：正位 — 突发的觉醒或破坏，虽痛苦但能摧毁不稳的基底。",
        "高塔：逆位 — 延迟的崩解或仍在逃避，需要重建更坚实的根基。",
    ),
    17: (
        "星：正位 — 希望、疗愈与灵感，未来有治愈与机会。",
        "星：逆位 — 失望或迷失方向，需重拾信念与实践。",
    ),
    18: (
        "月：正位 — 潜意识、梦境与不确定，警惕幻象与情绪波动。",
        "月：逆位 — 真相显现或误解被澄清，内心更清晰。",
    ),
    19: (
        "太阳：正位 — 成功、喜悦与能量，适合庆祝并放大积极成果。",
        "太阳：逆位 — 小阻碍或延迟快乐，核心仍是光明与成长。",
    ),
    20: (
        "审判：正位 — 觉醒、反省与重生的召唤，承担与释放并存。",
        "审判：逆位 — 自我审判或拒绝承担，需诚实面对过去与选择。",
    ),
    21: (
        "世界：正位 — 完成、整合与圆满的成就，适合收官并庆贺。",
        "世界：逆位 — 未完全收尾或等待收束，可能需要再努力一段路。",
    ),
}

# Add Major Arcana (ids 0-21)
for i, (cn, en) in enumerate(MAJOR):
    up, rev = MAJOR_MEANINGS.get(i, (f"{cn}：正位含义。", f"{cn}：逆位含义。"))
    CARDS.append({
        "id": i,
        "name": f"{cn} {en}",
        "upright": up,
        "reversed": rev,
    })

# Add Minor Arcana (ids continue)
cid = len(CARDS)
for suit_cn, suit_en in SUITS:
    for rank in RANKS:
        upright, reversed_mean = _minor_meaning(suit_cn, rank)
        CARDS.append({
            "id": cid,
            "name": f"{suit_cn} {rank}",
            "upright": upright,
            "reversed": reversed_mean,
        })
        cid += 1


def get_card_by_id(cid):
    if 0 <= cid < len(CARDS):
        return CARDS[cid]
    return None


def draw_cards(n=3):
    """Return n unique random cards with `reversed` flag."""
    n = max(1, min(n, len(CARDS)))
    picks = random.sample(range(len(CARDS)), n)
    result = []
    for pid in picks:
        entry = CARDS[pid]
        card = {"id": entry["id"], "name": entry["name"], "reversed": random.random() < 0.35}
        result.append(card)
    return result


def interpret_card(card):
    """Given card dict {id:, reversed:}, return interpretation text."""
    cid = int(card.get("id"))
    reversed_flag = bool(card.get("reversed", False))
    entry = get_card_by_id(cid)
    if not entry:
        return {"id": cid, "text": "未知牌。"}
    text = entry["reversed"] if reversed_flag else entry["upright"]
    return {"id": cid, "name": entry["name"], "reversed": reversed_flag, "text": text}
