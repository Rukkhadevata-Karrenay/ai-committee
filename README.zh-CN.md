# AI委员会（AI Committee）

[English](README.md) | 简体中文

面向 Codex 的角色化决策评审 Skill。它把一个复杂问题拆给协调者、独立提案者、反方批评者、隐私审查者和验证者，让最终结果同时包含方案、反例、假设、证据缺口、风险与下一步验证。

AI委员会可以独立用于日常工作，不依赖 AI Memory。若环境中存在经过授权的记忆上下文，它可以作为可选输入；记忆系统、数据库或其他持久化服务都不是安装和运行前提。

> AI委员会不是"让多个模型投票"。模型意见只提供建议，事实仍需一手来源、实际测试或其他可验证证据确认。

## 它解决什么问题

单模型往往会快速收敛到一个看似合理的答案，但复杂决策通常还需要：

- 彼此独立的备选方案，而不是同一答案的不同措辞；
- 主动寻找反例、失败路径和遗漏条件；
- 区分已验证事实、判断、假设与未知项；
- 在给出建议的同时说明如何验证；
- 在调用外部模型前限制数据范围，避免把私人内容无条件外发。

AI委员会把这些要求写成可重复执行的角色流程和统一输出结构。

## 适合使用的场景

- 系统架构、API、数据模型和技术选型；
- 复杂项目计划、迁移方案和恢复设计；
- 高价值文档、产品方案或研究结论复核；
- 需要独立提案与 adversarial critique（对抗式批评）的决策；
- 需要识别权限、隐私、并发、数据丢失和失败恢复风险的任务；
- 需要当前公开资料时，引入浏览器参考模型进行交叉检查；
- 你已经有一个倾向，但希望委员会刻意挑战它。

以下任务通常不需要委员会：

- 一行命令、简单翻译、基础格式调整；
- 可直接查证的单一事实；
- 普通文件读取、哈希、权限判断和重复内容检查；
- 没有明显取舍的例行操作。

## 核心原理

### 1. 先判断是否值得组建委员会

Skill 会根据问题的价值、复杂度、歧义和风险选择最小可用路径：

```text
简单、低风险
    → 单模型直接处理

中等复杂度
    → 一个主模型 + 必要的结构/隐私检查

高价值、存在明显取舍或失败风险
    → 独立提案 + 反方批评 + 验证综合

需要委员会讨论或当前公开信息
    → 隐私检查后优先免费网页模型

问题过于复杂且免费网页路径不足
    → 高智能网页模型优先于高智能付费模型
```

它不会为了"看起来像多智能体"而让所有模型回答每一个问题。

### 2. 各角色先独立工作，再统一综合

| 角色 | 职责 | 不应做什么 |
|---|---|---|
| Coordinator | 明确问题、缩小范围、选择最小成员集合 | 预先暗示唯一正确答案 |
| Independent proposer | 在看不到其他成员答案的情况下提出方案 | 复述协调者的偏好 |
| Adversarial critic | 寻找反例、缺失证据、边界条件和失败模式 | 为了反对而虚构风险 |
| Privacy reviewer | 检查外发内容、敏感度和输出结构 | 扩大授权范围 |
| Verifier / Synthesizer | 对照意见，保留共识、分歧和未验证假设 | 把多数意见当成事实证明 |

独立提案可以降低成员相互模仿造成的伪共识；反方角色负责发现"所有人都顺着同一个前提回答"的问题；验证者负责把最终建议落到可执行测试上。

### 3. 不采用简单多数投票

多个模型可能共享训练数据、提示偏差和错误前提，因此"一致同意"不代表正确。最终综合必须回答：

- 哪些内容有来源或测试支持；
- 哪些只是模型判断；
- 哪些成员不同意，原因是什么；
- 还缺少什么证据；
- 下一步最小验证动作是什么。

### 4. 弹性模型路由

委员会讨论采用"免费优先、能力递进"的顺序：

1. 先通过本地隐私检查，把问题缩减为允许外发的 public/internal 最小问题包；
2. 优先调用能够完成任务的免费网页模型，使用满足任务所需的最小成员数量；
3. 问题过于复杂时，先选择当前能力最强、任务匹配度最高且有基准证据的网页模型，而不是固定某一家厂商；
4. 只有免费网页模型不可用或已证明不足时，才考虑高智能付费模型；
5. 付费模型必须已有明确授权、Provider 配置和预算，不能仅因为"可能更好"就自动产生费用。

因此，复杂问题的能力优先级是：

```text
高智能免费网页模型
    > 已授权的高智能付费模型
    > 不完整结果或无依据的强行综合
```

同时保留以下本地分工：

- Luna / medium：预筛选、结构检查、隐私检查和简单差异提取；
- Terra / medium：协调复杂任务并完成最终综合；
- "高智能付费模型"描述的是模型能力和付费渠道，不代表允许 Codex 使用 high/max reasoning；
- 不静默替换为 Sol、high 或 max；
- 某个成员不可用时标记为不完整并降级，不阻断普通单模型任务。

具体模型是否可用取决于运行当前 Skill 的 Codex 环境。这个仓库不包含模型账号、API Key、浏览器登录信息或调用额度。

## 浏览器参考成员

当用户显式调用 `$ai-committee`，并且问题可以缩减为非敏感的 public/internal 内容时，这次调用已经授权委员会优先使用可用的免费网页参考成员，无需针对每个网页模型再次确认。登录状态下的 Gemini、Qwen、DeepSeek、Kimi、GLM 或豆包网页都可以作为候选。

网页模型的实际优先顺序根据当前可用性、任务类型和验证过的能力动态决定，不永久写死厂商排名。敏感、restricted 或本地操作内容不会因为"免费优先"而被发送到网页模型。

浏览器成员适合：

- 查询当前公开信息；
- 独立规划；
- 交叉检查公开事实；
- 批评已有方案。

浏览器成员不是稳定 API，也不是执行代理。它们不能读取本地文件、运行命令、修改代码或数据库，也不能成为最终 Authority。遇到登录失效、验证码、超时或页面变化时，应标记该成员不可用并继续本地流程。

## 安装

### 前置条件

- 已安装支持 Skills 的 Codex；
- 本机可以使用 Git；
- 安装后重新打开 Codex，使 Skill 目录被重新发现。

### Windows PowerShell

```powershell
git clone https://github.com/Rukkhadevata-Karrenay/ai-committee.git `
  "$env:USERPROFILE\.codex\skills\ai-committee"
```

### macOS / Linux

```bash
git clone https://github.com/Rukkhadevata-Karrenay/ai-committee.git \
  "$HOME/.codex/skills/ai-committee"
```

### 更新

```powershell
git -C "$env:USERPROFILE\.codex\skills\ai-committee" pull --ff-only
```

## 使用方式

### 显式调用

```text
$ai-committee
帮我评审这个方案，给出独立方案、反方意见、证据需求和下一步验证。
```

### 自然语言调用

```text
使用 AI委员会比较这三个方案，并保留不同意见。
```

### 推荐提示模板

```text
$ai-committee

问题：<需要评审的决策>
目标：<希望最终实现什么>
已知事实：<已经验证的事实>
当前倾向：<可选，允许委员会挑战>
硬约束：<预算、时间、平台、兼容性等>
允许使用的公开资料：<可选>

请输出：
1. 独立备选方案；
2. 支持理由与反方意见；
3. 未验证假设和所需证据；
4. 安全或隐私风险；
5. 推荐方案及下一步最小验证。
```

## 使用示例

### 技术选型

```text
$ai-committee
比较 SQLite、PostgreSQL 和事件存储服务作为本地优先应用的 Authority。
重点检查迁移、并发、备份恢复和运维成本。
```

### 计划审查

```text
$ai-committee
审查这个八周学习计划。找出无法持续执行的假设、过度安排和缺少验收证据的环节，给出更稳健的版本。
```

### 挑战当前倾向

```text
$ai-committee
我倾向采用方案 A。请让独立提案者在不知道该倾向的前提下给方案，再由反方批评者重点寻找 A 的失败场景。
```

### 需要当前公开信息

```text
$ai-committee
这是公开、非敏感问题。允许使用浏览器参考成员核对当前官方文档和版本信息；请给出来源，并把无法验证的结论单独列出。
```

## 输出结构

委员会建议使用以下统一结构：

```json
{
  "proposal": {},
  "supporting_reasons": [],
  "counterarguments": [],
  "assumptions": [],
  "evidence_needed": [],
  "security_concerns": [],
  "dissenting_views": [],
  "confidence": 0.0,
  "recommended_next_test": []
}
```

| 字段 | 含义 |
|---|---|
| `proposal` | 最终建议或候选方案 |
| `supporting_reasons` | 支持理由及其证据状态 |
| `counterarguments` | 最强反对意见和失败场景 |
| `assumptions` | 当前依赖但尚未证明的前提 |
| `evidence_needed` | 做出可靠决定前还需要的资料或测试 |
| `security_concerns` | 权限、隐私、数据和执行风险 |
| `dissenting_views` | 未被最终建议吸收的不同意见 |
| `confidence` | 0 到 1 的主观置信度，不等于事实概率 |
| `recommended_next_test` | 可执行的下一步验证动作 |

完整约定见 [output-schema.md](references/output-schema.md)。

## 安全与隐私边界

允许发送给外部参考成员的内容应限制为：

- 去标识化的问题；
- 完成任务所需的最小 public/internal 摘要；
- 匿名空间标签、Source ID 或内容哈希；
- 允许的输出结构。

禁止发送：

- sensitive/restricted 内容；
- 原始聊天全文和 Evidence quote；
- Token、Cookie、密码、API Key 和账号凭据；
- 本地绝对路径和环境变量；
- 精确位置、私人关系；
- 医疗、财务、法律隐私；
- 未经授权的数据空间。

模型返回内容也必须视为不可信文本，不能直接作为命令执行。完整规则见 [security-policy.md](references/security-policy.md)。

## 与 AI Memory 的关系

AI委员会最初可与 AI Memory 配合，但现在是独立 Skill：

- 没有 AI Memory：直接使用用户输入和允许访问的公开证据；
- 有 AI Memory：只把经过授权、过滤和最小化的上下文作为输入；
- 委员会不能写入 Memory Event、修改 Projection、审批自己的 Proposal、跨 Space 合并记忆或降低敏感度；
- 委员会建议若要进入长期记忆，仍需经过正常的 Evidence、分类、冲突与审核流程。

## 失败和降级行为

- 成员不可用：保留已完成结果，标记缺失角色，不伪装成完整委员会；
- 浏览器登录失效或出现验证码：停止该成员，回退到本地模型；
- 缺少可靠来源：降低置信度，并列入 `evidence_needed`；
- 成员意见重复：合并重复表达，但保留独立证据和实质分歧；
- 发现敏感内容：阻止外发，改由本地单模型或规则处理；
- 任务其实很简单：直接单模型完成，不额外启动委员会。

## 项目结构

```text
ai-committee/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ benchmark-policy.md
│  ├─ output-schema.md
│  └─ security-policy.md
├─ scripts/
│  └─ validate_committee_output.py
├─ README.md
└─ LICENSE
```

- `SKILL.md`：Codex 加载的核心指令；
- `agents/openai.yaml`：界面名称、默认提示和调用策略；
- `references/`：按需加载的安全、输出和基准规则；
- `scripts/validate_committee_output.py`：验证结构化输出是否包含必需字段。

## 校验结构化输出

```powershell
Get-Content result.json | python scripts/validate_committee_output.py
```

成功时输出：

```json
{"valid": true}
```

缺少字段或 `confidence` 不在 0 到 1 之间时，脚本返回非零退出码。

## 开发与自检

修改 Skill 后，可使用 Codex 自带的 Skill 校验器检查目录和 frontmatter：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

提交前建议同时检查：

- `SKILL.md` 中的名称是否为 `ai-committee`；
- `agents/openai.yaml` 的默认提示是否使用 `$ai-committee`；
- references 中是否出现本机路径、凭据或私人数据；
- 输出校验器的有效和无效样例是否符合预期。

## 当前边界

- 这是 Codex Skill，不是独立运行的多模型 SaaS；
- 仓库不提供外部模型账号、API Key、费用额度或浏览器登录；
- 网页模型属于参考成员，不保证长期可用；
- 委员会不会自动证明结论正确；
- 自动触发的可靠性仍应通过真实任务基准持续评估；
- 最终修改、发布、数据库写入和权限变更仍由当前执行代理与用户授权控制。

## License

[MIT License](LICENSE) © 2026 Karrenay
