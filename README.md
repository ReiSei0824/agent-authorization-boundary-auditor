# Agent Authorization Boundary Auditor

将能行动的 AI 工作流拆成可执行的最小权限矩阵：资源范围、默认决策、审批门、证据与回滚。它适合审查 agent、MCP、插件和自动化，不替代渗透测试或法律意见。

## Triggers

- “帮我审查这个 agent 能否访问客户工单并自动回复。”
- “哪些外部动作必须人工批准？”
- “Audit this MCP workflow before production rollout.”
- “Create a least-privilege authorization matrix for our browser agent.”

## Workflow

1. 登记目标、环境、数据和工具资产。
2. 按副作用给动作分级。
3. 建立最小权限授权矩阵。
4. 设计审批、隔离与回滚。
5. 用正常、越权、注入、凭据与超时场景验收。
6. 输出 GO / GO_WITH_GATES / NO_GO 决定。

## Output

输出可复制的授权矩阵、验收用例、未解决项、上线门槛和回滚条件。示例：浏览器 agent 可以读取指定域名的公开说明页，但把内容发送到外部邮箱时必须展示收件人和摘要并由负责人批准。

## Install

本地目录可保留中文名称；安装目录必须使用 skill 的英文名：

```text
~/.claude/skills/agent-authorization-boundary-auditor/SKILL.md
```

发布仓库建议名：`agent-authorization-boundary-auditor`。复制该目录的 `SKILL.md` 到上述安装目录即可；无需 API key。

## File tree

```text
agent-authorization-boundary-auditor/
├── SKILL.md
├── README.md
├── audit_authorization.py
└── test_audit_authorization.py
```

## Notes

先在预发或一次性环境完成验收。对外发送、发布、支付、删除和权限变更应始终保持独立审批与可撤销凭据。
