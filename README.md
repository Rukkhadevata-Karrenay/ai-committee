# AI委员会（AI Committee）

一个可独立使用的 Codex Skill，用角色化评审帮助处理复杂决策、技术方案、研究问题、计划审查和风险分析。

它不会把“多数模型同意”当成事实。输出会保留支持理由、反方意见、假设、证据缺口、安全风险和下一步验证。

## 适用场景

- 架构设计与技术选型
- 高价值计划或重要文档审查
- 独立方案与反方批评
- 复杂决策中的风险和证据缺口
- 需要当前公开信息时的浏览器参考模型评估

简单、例行、容易验证的任务仍走单模型路径。AI Memory 是可选上下文源，不是运行前提。

## 安装

```powershell
git clone https://github.com/Rukkhadevata-Karrenay/ai-committee.git `
  "$env:USERPROFILE\.codex\skills\ai-committee"
```

重新打开 Codex 后，显式调用：

```text
$ai-committee
帮我评审这个方案，给出独立方案、反方意见、证据需求和下一步验证。
```

也可以自然语言调用：

```text
使用 AI委员会比较这三个方案，并保留不同意见。
```

## 工作方式

- Coordinator：压缩问题，选择最小成员集合
- Independent proposer：独立提出方案
- Adversarial critic：寻找反例、缺失证据和失败模式
- Privacy reviewer：检查外发范围与输出结构
- Verifier：区分事实、判断、分歧和未验证假设

模型成员的回答始终是参考材料，不能直接修改代码、数据库、权限、记忆或备份状态。

## 安全边界

禁止向外部参考模型发送敏感或受限信息、原始私聊、凭据、Token、Cookie、本地绝对路径、精确位置以及医疗、财务、法律等隐私内容。成员输出同样按不可信数据处理。

完整规则见 [security-policy.md](references/security-policy.md)，统一输出结构见 [output-schema.md](references/output-schema.md)。

## 校验输出

```powershell
Get-Content result.json | python scripts/validate_committee_output.py
```

## License

[MIT](LICENSE)
