# societe-vehicleshare — 车辆共享公司数据库设计 | Conception de la base de données d'une société de partage de véhicules

**UTC · NF18 « Bases de données » · Printemps 2024 (P24) · Groupe 4**

![Diagramme de classes UML](UML_D5_G4.png)

> **中文**：本仓库是我的数据库课程作品集，以课程设计项目 vehicleShare（车辆共享平台的信息系统）为主体，另附课程 TD 习题、示例代码与历史归档。
>
> **Français** : Ce dépôt est mon portfolio du cours NF18 « Bases de données » : il met en avant le projet vehicleShare (système d'information d'une société de location de véhicules), complété par les exercices des TD, des exemples de cours et une archive.

## 项目简介 | Présentation du projet

**中文**
vehicleShare 是一家提供"个人之间自助式车辆租赁"服务的公司：车主在网上发布车辆公告并设定可用时段，租客（个人或企业）在线预订并签署租赁合同。本课程项目的目标是为该公司设计并实现完整的信息系统：从需求分析出发建立 UML 类图，推导关系模型（MLD），在 PostgreSQL 中落地数据库与完整性约束，开发基于 Python / psycopg2 的命令行应用，对数据模式做规范化检验，最后给出以 JSON 列存储半结构化数据的 NoSQL 演进版本。

**Français**
vehicleShare est une société de location de véhicules entre particuliers en libre-service : les propriétaires publient des annonces et définissent les périodes de disponibilité, les locataires (particuliers ou entreprises) réservent en ligne et signent un contrat de location. Ce projet de cours consiste à concevoir et réaliser le système d'information complet de la société : analyse des besoins, diagramme de classes UML, modèle logique de données (MLD), implémentation sous PostgreSQL avec ses contraintes d'intégrité, application en ligne de commande en Python/psycopg2, normalisation du schéma, puis une variante « NoSQL » fondée sur des colonnes JSON.

## 主要功能 | Fonctionnalités principales

**中文**
- **公告管理**：发布 / 修改 / 删除车辆公告，按类别、评分、举报数、可用日期等多条件检索；
- **预订与租赁合同**：个人租客或企业（企业可委派其司机）签署合同，可选免赔方案（无减免 / 减免免赔 / 零免赔）与里程上限；
- **车辆状况检查**：取车与还车各一次，记录照片、里程、油量与损伤清单；
- **发票**：租金 + 超里程计费 + 归还时油量不足的补偿计费；
- **评价与举报**：租后可打 0–5 分并举报车辆；被举报 3 次的公告自动下架，需质量负责人重新激活；
- **车辆周边信息**：保险合同、可选配置、可用时段、允许行驶的国家。

**Français**
- **Gestion des annonces** : publier, modifier, supprimer des annonces ; recherche multicritères (catégorie, note, signalements, disponibilité) ;
- **Réservation et contrat de location** : signé par un particulier ou par une entreprise (avec ses conducteurs), avec options de franchise (« sans réduction », « franchise réduite », « zéro franchise ») et seuil kilométrique ;
- **États des lieux** : au départ et au retour — photos, kilométrage, carburant, check-list des dégâts ;
- **Facture** : montant = prix de location + dépassement du seuil kilométrique + carburant manquant ;
- **Commentaires et signalements** : note de 0 à 5 et signalement possibles après la location ; après 3 signalements l'annonce est désactivée automatiquement, sa réactivation nécessite le responsable qualité ;
- **Autour du véhicule** : contrat d'assurance, options, périodes de disponibilité, pays de circulation autorisés.

## 交付流程 | Démarche du projet

项目按五次正式交付推进，并额外完成一次 NoSQL 扩展。
Le projet a été réalisé en cinq rendus, complétés par une extension NoSQL.

| Rendu | Contenu / 内容 | Fichiers / 文件 |
| --- | --- | --- |
| Rendu 1 | 需求澄清笔记 + 首版 UML 类图 / Note de clarification + premier diagramme de classes | `Rendu Relationnel/Rendu 1/` |
| Rendu 2 | 修订版 UML + 逻辑数据模型（MLD）/ UML v2 + MLD | `Rendu Relationnel/Rendu 2/` |
| Rendu 3 | PostgreSQL 实现：建表、插入数据、查询 / Implémentation PostgreSQL : création, insertion, requêtes | `Rendu Relationnel/Rendu 3/` |
| Rendu 4 | Python / psycopg2 命令行应用 / Application en ligne de commande | `Rendu Relationnel/Rendu 4/` |
| Rendu 5 | 规范化分析 / Normalisation du schéma | `Rendu Relationnel/Rendu 5/` |
| NoSQL | JSON 半结构化数据版本：保险、发票、评论存为 JSON 列 / Variante avec données semi-structurées | `Rendu NoSQL/` |

## 数据模型概览 | Modèle de données en bref

**中文**
- 用户体系：统一的 `Utilisateur` 表（登录名、密码、类型、启用状态）+ 子表 `Proprietaire` / `Locataire` / `Entreprise`；企业下挂若干 `Conducteur`；
- 车辆 `Vehicule` 以车牌号为主键，关联车主、保险合同（NoSQL 版存为 JSON）、可用时段 `Periode`、选项 `Option` 与可行驶国家 `Pays`；
- 交易链：公告 `Annonce` → 租赁合同 `Contrat_location` → 状况检查 `Etat_des_lieux`（取车 / 还车各一次）+ 发票 `Facture`（NoSQL 版存为 JSON）+ 评论 `Commentaire`（NoSQL 版存为 JSON）。

**Français**
- Utilisateurs : une table mère `Utilisateur` (pseudo, mot de passe, type, actif) et des sous-tables `Proprietaire` / `Locataire` / `Entreprise` ; chaque entreprise possède ses `Conducteur` ;
- `Vehicule` est identifié par son immatriculation et relié à son propriétaire, à son contrat d'assurance (en JSON dans la variante NoSQL), à ses périodes de disponibilité (`Periode`), à ses `Option` et à ses pays de circulation (`Pays`) ;
- Chaîne transactionnelle : `Annonce` → `Contrat_location` → `Etat_des_lieux` (départ et retour) + `Facture` (JSON côté NoSQL) + `Commentaire` (JSON côté NoSQL).

## 仓库结构 | Arborescence

```
.
├── README.md                    ← 你正在阅读的文件 / le fichier que vous lisez
├── Rendu Relationnel/           # Rendu 1–5：澄清 → UML/MLD → SQL → Python → 规范化
├── Rendu NoSQL/                 # JSON 半结构化数据扩展 / variante JSON
├── UML_D5_G4.png                # UML 类图 / diagramme de classes
├── cours-et-exercices/          # 课程 TD 习题与示例 / TD et exemples de cours
│   ├── td/                      # TD3–TD5 习题（SQL + Python）
│   └── demos/demo-json/         # JSON / JavaScript 演示
└── archive/                     # 历史草稿 / brouillons anciens
```

- 课程习题与学习内容详见 **[cours-et-exercices/README.md](cours-et-exercices/README.md)** / Exercices et contenus d'apprentissage : voir ce dossier.
- 历史草稿见 **[archive](archive/)** / Brouillons anciens.

## 运行方式 | Mise en route

**中文**
1. 准备一个 PostgreSQL 环境（本地或远程）。
2. 依次执行 `Rendu Relationnel/Rendu 3/` 中的 `create_projet.sql`、`insert_projet.sql`，再用 `select_projet.sql` 验证查询。
3. 命令行应用：安装依赖 `pip install psycopg2`，在 `Rendu Relationnel/Rendu 4/app_python.py` 顶部填入数据库连接参数后运行 `python app_python.py`。
4. NoSQL 版本同理，脚本位于 `Rendu NoSQL/`。

**Français**
1. Prévoir un environnement PostgreSQL (local ou distant).
2. Exécuter `create_projet.sql` puis `insert_projet.sql` (dossier `Rendu Relationnel/Rendu 3/`), et tester avec `select_projet.sql`.
3. Application : installer `psycopg2`, renseigner les paramètres de connexion en tête de `Rendu Relationnel/Rendu 4/app_python.py`, puis lancer `python app_python.py`.
4. La variante NoSQL fonctionne de la même manière (dossier `Rendu NoSQL/`).

## 技术要点 | Points techniques

- 完整性约束：`CHECK`（电话格式、年龄 ≥ 18、评分 0–5、"被举报 ≥ 3 次则公告必须停用"、合同租客与企业二选一）、外键、复合主键；
- `SERIAL` 自增主键与继承关系建模（母表 + 子表）；
- psycopg2 参数化查询（`%s` 占位符）避免 SQL 注入；
- NoSQL 变体：`JSON` 列配合 `->>` 操作符查询（如按保险类型、评分、举报状态筛选）。

**Français**
- Contraintes d'intégrité : `CHECK` (format du téléphone, âge ≥ 18, note entre 0 et 5, « annonce inactive dès 3 signalements », locataire *ou* entreprise par contrat), clés étrangères, clés primaires composées ;
- Clés `SERIAL` et modélisation de l'héritage (table mère + sous-tables) ;
- Requêtes paramétrées avec psycopg2 (`%s`) contre l'injection SQL ;
- Variante NoSQL : colonnes `JSON` interrogées avec l'opérateur `->>` (par type d'assurance, note, signalement…).

## 学习收获 | Ce que ce cours m'a apporté

**中文**
- 掌握了从需求分析到落地交付的完整数据库设计方法：澄清需求 → UML 建模 → 关系模式 → SQL 实现 → 应用开发 → 规范化（BCNF）检验 → 半结构化数据演进；
- 熟悉 PostgreSQL 的完整性约束体系（`CHECK`、复合主键 / 外键、`SERIAL`）与 `JSON` 数据类型；
- 能够用 Python（psycopg2）编写带参数化查询的数据库应用，防止 SQL 注入；
- 熟练编写多表 `JOIN`、外连接反连接、`GROUP BY` / `HAVING`、子查询等分析型 SQL。

**Français**
- Une méthode complète de conception de base de données : clarification → UML → MLD → SQL → application → normalisation (BCNF) → données semi-structurées ;
- La maîtrise des contraintes d'intégrité de PostgreSQL (`CHECK`, clés composées, `SERIAL`) et du type `JSON` ;
- Des applications Python/psycopg2 avec requêtes paramétrées (protection contre l'injection SQL) ;
- L'écriture de requêtes analytiques : JOIN multi-tables, anti-jointures, `GROUP BY` / `HAVING`, sous-requêtes.

## 成员 | Membres — Groupe 4

- Joséphine Lapié
- Yicong Li
- Raphaël Hagron
- Manuel Acker

课程指导 / Responsable : Alessandro Victorino

## 关于我 | À propos

**LI Yicong** — 学生 @ UTC / étudiant à l'UTC

<!-- 在此补充你的链接 / Ajoutez ici vos liens : site personnel, GitHub, LinkedIn, e-mail -->

## 备注 | Remarque

**中文**：代码中的数据库连接参数已替换为占位符（如 `your_user` / `your_password`），使用前请填入你自己的配置（或改用环境变量）；请勿在公开仓库提交真实凭据。

**Français** : Les paramètres de connexion présents dans le code ont été remplacés par des valeurs fictives (`your_user`, `your_password`, etc.) ; renseignez votre propre configuration (ou des variables d'environnement) avant toute réutilisation, et ne publiez jamais d'identifiants réels dans un dépôt public.
