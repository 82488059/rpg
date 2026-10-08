# rpg

Python 写的简易 RPG 游戏原型。

## 结构

- `rpg/StartScreen.py`：启动界面
- `rpg/HeroBase.py`、`rpg/combats/`：角色与战斗
- `rpg/ctrl/`、`rpg/dialog/`、`rpg/conf/`：控件、对话框与配置

解决方案文件：`rpg.sln`（若用 IDE 管理）；主要逻辑为 Python。

## 运行

```bash
cd rpg
python StartScreen.py
```

需要 Python 3，以及运行时用到的 GUI/字体依赖（如仓库内 `SIMYOU.TTF`）。
