# Install offline-ux-kit

## 给使用者

推荐把下面这句话交给你的 Agent：

```text
安装 offline-ux-kit：https://raw.githubusercontent.com/Fable-Forge/offline-ux-kit/main/docs/install.md
```

## 给执行安装的 Agent

### 目标

从 `https://github.com/Fable-Forge/offline-ux-kit` 安装 `offline-ux-kit`，验证目标目录、运行时资源和 `SKILL.md`，并诚实报告哪些 Agent 已可发现。

### 边界

- 安装前确定用户要支持 Codex、Claude Code、通用 Agent Skills 中的哪些运行时。
- 不覆盖内容不同的现有目录；发现冲突时先报告哈希或差异。
- 不写入当前项目工作区之外的无关位置。
- 不声称正在运行的会话会热加载；需要时请用户开启新会话验证。

### 推荐安装

```bash
npx skills add Fable-Forge/offline-ux-kit
```

### 手动目标目录

| 运行时 | 目标目录 |
|---|---|
| Codex | `~/.codex/skills/offline-ux-kit/` |
| Claude Code | `~/.claude/skills/offline-ux-kit/` |
| Agent Skills | `~/.agents/skills/offline-ux-kit/` |

手动安装时，复制 `SKILL.md`、`agents/`、`assets/`、`references/` 和功能性 `scripts/`。`assets/offline-ux.js` 是工作流依赖，不能遗漏。README、许可证、示例、测试、报告样例和 GitHub workflow 不属于运行时 payload。

### 验证

1. 确认目标目录中的 `SKILL.md` 与 `assets/offline-ux.js` 存在。
2. 对比源与目标 payload 的 SHA-256 或逐文件清单。
3. 若本机有 Agent Skills/Codex validator，运行结构校验。
4. 在新会话中用 README 所述自然语言场景测试是否真实触发并读取运行时资源。
5. 分别报告 `结构有效`、`安装可见`、`真实触发` 和 `真实浏览器验收`；未执行的项目标为 `pending_external`。
