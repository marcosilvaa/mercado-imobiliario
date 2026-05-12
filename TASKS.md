# TASKS.md — Inteligência Imobiliária Maringá

Backlog executável derivado do `PRD.md`. Foco atual: planejamento antes de implementação. Sprints são sequenciais; tasks marcadas como futuras não devem ser iniciadas antes das dependências.

## [X] Sprint 0 — Specification and Execution Setup

**Goal:** fechar documentação, decisões iniciais e gates antes de escrever código.

**Dependencies:** contexto atual do repositório e PRD.

**Status:** Complete.

**Tasks:**

### [X] T0.1 — Consolidar PRD

**Subtasks:**

- [X] Revisar visão, problema, objetivos e escopo.
- [X] Separar MVP, pós-MVP e SaaS futuro.
- [X] Registrar premissas e questões abertas.
- [X] Validar alinhamento com Spec-Driven Development.

**Deliverables:** `PRD.md` atualizado.

**Done Criteria:** PRD contém requisitos, arquitetura lógica, stack, roadmap, riscos e critérios de aceite.

### [X] T0.2 — Criar backlog rastreável

**Subtasks:**

- [X] Quebrar roadmap em sprints.
- [X] Definir objetivo, dependências, entregáveis e done criteria por sprint.
- [X] Garantir que tasks derivem de requisitos do PRD.

**Deliverables:** `TASKS.md`.

**Done Criteria:** backlog permite iniciar execução técnica sem nova exploração aberta.

### [X] T0.3 — Definir gates técnicos iniciais

**Subtasks:**

- [X] Confirmar comandos de validação do projeto.
- [X] Definir padrão de testes unitários, integração e contrato.
- [X] Registrar que código futuro deve passar por `poetry check`, `compileall` e testes quando existirem.

**Deliverables:** seção operacional futura no backlog.

**Done Criteria:** cada sprint técnica possui validação esperada.

### Sprint 0 Completion Evidence

- [X] `PRD.md` contém overview, problema, objetivos, escopo, requisitos, modelo de dados, deduplicação, arquitetura, stack, roadmap, riscos, premissas, questões abertas e critérios de aceite.
- [X] `TASKS.md` contém backlog sequencial por sprints, tasks, subtasks, dependências, entregáveis e critérios de conclusão.
- [X] Rastreabilidade macro registrada em `Cross-Sprint Traceability`.
- [X] Gates técnicos iniciais definidos abaixo para guiar as próximas sprints.

### Technical Validation Gates

Use estes gates nas próximas sprints. Ajustar somente quando a stack mudar.

| Gate | Command | Applies To | Expected Result |
|---|---|---|---|
| Metadata | `poetry check` | Todo sprint que altera projeto Python | Metadata válido |
| Syntax | `poetry run python -m compileall src` | Todo sprint com código Python | Sem erro de compilação |
| Unit tests | `poetry run pytest tests/unit` | Normalização, scraper, matching, serviços | Testes unitários passam |
| Contract tests | `poetry run pytest tests/contract` | Integração com Sub100 e fixtures | Contrato esperado preservado |
| Integration tests | `poetry run pytest tests/integration` | Banco, API, jobs e agregações | Fluxos integrados passam |
| Full test suite | `poetry run pytest` | Antes de encerrar sprint técnica | Suite completa passa |
| Data quality | comando/script futuro de quality check | Coleta, normalização e gold metrics | Contagens, schema e nulos críticos dentro dos limites |
| Frontend build | comando futuro do app web | Sprints de dashboard | Build sem erro |

### Testing Standards

- [X] Testes unitários devem cobrir funções puras: construção de URL, parsing, normalização, score de deduplicação e regras de status.
- [X] Testes de contrato devem usar fixtures pequenas do Sub100 e validar campos críticos sem depender da API ao vivo.
- [X] Testes de integração devem validar persistência, migrations, endpoints e jobs com banco isolado.
- [X] Testes de frontend devem validar filtros, renderização de estados vazios e contratos principais da API quando dashboard existir.
- [X] Nenhuma sprint técnica deve ser concluída com erro conhecido sem registrar blocker explícito no backlog.

## [ ] Sprint 1 — Source Discovery and Scraping Contract

**Goal:** validar Sub100 como fonte antes de estruturar pipeline permanente.

**Dependencies:** Sprint 0.

**Tasks:**

### [ ] T1.1 — Mapear contrato da API Sub100

**Subtasks:**

- [ ] Documentar endpoint usado.
- [ ] Documentar parâmetros de cidade, tipo, transação, paginação e ordenação.
- [ ] Capturar amostras pequenas de venda e aluguel.
- [ ] Identificar campos críticos e opcionais.

**Deliverables:** documento ou seção de contrato da fonte.

**Done Criteria:** campos necessários para normalização estão listados e classificados.

### [ ] T1.2 — Definir critérios de coleta confiável

**Subtasks:**

- [ ] Definir limites de páginas para desenvolvimento e produção.
- [ ] Definir timeout, delay, retry e backoff.
- [ ] Definir comportamento quando página falhar.
- [ ] Definir métrica mínima de sucesso por execução.

**Deliverables:** critérios operacionais de scraping.

**Done Criteria:** falhas esperadas têm resposta definida e rastreável.

### [ ] T1.3 — Planejar testes de contrato

**Subtasks:**

- [ ] Definir fixtures JSON representativas.
- [ ] Definir teste para schema mínimo.
- [ ] Definir teste para página vazia.
- [ ] Definir teste para campos ausentes.

**Deliverables:** plano de testes de contrato.

**Done Criteria:** fonte pode mudar sem quebrar silenciosamente a aplicação.

## [ ] Sprint 2 — Data Architecture and Persistence

**Goal:** desenhar e implementar base histórica bronze/silver com PostgreSQL/PostGIS.

**Dependencies:** Sprint 1.

**Tasks:**

### [ ] T2.1 — Especificar schema relacional

**Subtasks:**

- [ ] Modelar `source`, `scraping_run`, `raw_listing_snapshot`.
- [ ] Modelar `listing`, `location`, `price_observation`, `availability_event`.
- [ ] Modelar `property` e `property_listing_match`.
- [ ] Definir chaves, índices e constraints.

**Deliverables:** modelo de dados detalhado e migrations futuras.

**Done Criteria:** schema cobre entidades do PRD sem misturar bruto, normalizado e agregado.

### [ ] T2.2 — Definir estratégia PostGIS

**Subtasks:**

- [ ] Definir tipos geográficos para ponto e região.
- [ ] Definir uso de bairros como texto, geometria ou ambos.
- [ ] Definir índice espacial.
- [ ] Definir precisão geográfica (`exact`, `neighborhood`, `unknown`).

**Deliverables:** decisão de geodados.

**Done Criteria:** mapa e agregações regionais têm base consistente.

### [ ] T2.3 — Planejar persistência imutável de snapshots

**Subtasks:**

- [ ] Definir hash de payload.
- [ ] Definir política de duplicidade por run.
- [ ] Definir retenção de dados brutos.
- [ ] Definir rastreabilidade bruto -> normalizado.

**Deliverables:** regra de persistência bronze.

**Done Criteria:** nenhum payload bruto é sobrescrito por transformação posterior.

## [ ] Sprint 3 — Scraper Productionization

**Goal:** transformar coleta exploratória em componente operacional testável.

**Dependencies:** Sprint 1 e Sprint 2.

**Tasks:**

### [ ] T3.1 — Refatorar scraper para configuração explícita

**Subtasks:**

- [ ] Remover caminhos hard-coded.
- [ ] Parametrizar cidade, tipo, transação, páginas e destino.
- [ ] Separar construção de URL, fetch, parse e persistência.
- [ ] Trocar prints por logs estruturados.

**Deliverables:** scraper modular.

**Done Criteria:** scraper roda com parâmetros e não depende de estado implícito.

### [ ] T3.2 — Implementar tracking de run

**Subtasks:**

- [ ] Criar início e fim de execução.
- [ ] Registrar status `success`, `partial_success`, `failed`.
- [ ] Registrar contagens de páginas e itens.
- [ ] Registrar erros resumidos.

**Deliverables:** registro de execução persistido.

**Done Criteria:** toda coleta pode ser auditada depois da execução.

### [ ] T3.3 — Criar testes do scraper

**Subtasks:**

- [ ] Testar URL builder.
- [ ] Testar parse com fixture.
- [ ] Testar timeout/falha HTTP mockada.
- [ ] Testar campos ausentes.

**Deliverables:** testes unitários e de contrato.

**Done Criteria:** scraping pode evoluir sem regressão silenciosa.

## [ ] Sprint 4 — Normalization and Historical Events

**Goal:** transformar snapshots em entidades analíticas temporais.

**Dependencies:** Sprint 2 e Sprint 3.

**Tasks:**

### [ ] T4.1 — Normalizar anúncios

**Subtasks:**

- [ ] Mapear campos Sub100 para `listing`.
- [ ] Normalizar tipo, transação, anunciante e atributos.
- [ ] Tratar campos ausentes como nulos.
- [ ] Registrar fonte e chave externa.

**Deliverables:** camada silver de anúncios.

**Done Criteria:** anúncios são consultáveis sem depender do JSON bruto.

### [ ] T4.2 — Normalizar localização

**Subtasks:**

- [ ] Normalizar endereço, bairro, cidade e UF.
- [ ] Persistir latitude e longitude quando disponíveis.
- [ ] Registrar precisão geográfica.
- [ ] Definir fallback quando coordenadas faltarem.

**Deliverables:** tabela `location` populada.

**Done Criteria:** dashboard consegue filtrar por bairro e usar mapa quando houver coordenada.

### [ ] T4.3 — Criar histórico de preço

**Subtasks:**

- [ ] Detectar preço novo.
- [ ] Detectar alteração de preço.
- [ ] Persistir condomínio e taxas quando existirem.
- [ ] Evitar duplicar observação idêntica no mesmo dia.

**Deliverables:** `price_observation`.

**Done Criteria:** série temporal de preço pode ser consultada por anúncio.

### [ ] T4.4 — Criar eventos de disponibilidade

**Subtasks:**

- [ ] Detectar anúncio presente.
- [ ] Detectar ausência em coleta posterior.
- [ ] Detectar retorno.
- [ ] Diferenciar status inferido de venda/locação real.

**Deliverables:** `availability_event`.

**Done Criteria:** ciclo de vida do anúncio é rastreável sem inferência indevida.

## [ ] Sprint 5 — Deduplication MVP

**Goal:** identificar imóveis únicos prováveis com abordagem conservadora.

**Dependencies:** Sprint 4.

**Tasks:**

### [ ] T5.1 — Definir normalização de matching

**Subtasks:**

- [ ] Normalizar textos de endereço, bairro e condomínio.
- [ ] Normalizar números de área, quartos, banheiros e vagas.
- [ ] Criar fingerprint inicial.
- [ ] Versionar regras de normalização.

**Deliverables:** camada de preparação de matching.

**Done Criteria:** entradas equivalentes geram representação comparável.

### [ ] T5.2 — Implementar candidate blocking

**Subtasks:**

- [ ] Agrupar por cidade, transação, tipo e bairro.
- [ ] Adicionar faixas de área e preço.
- [ ] Usar proximidade geográfica quando disponível.
- [ ] Evitar comparação global desnecessária.

**Deliverables:** candidatos de comparação.

**Done Criteria:** matching escala sem comparar todos contra todos.

### [ ] T5.3 — Implementar score de deduplicação

**Subtasks:**

- [ ] Calcular similaridade por atributos estruturados.
- [ ] Calcular similaridade textual básica.
- [ ] Combinar score ponderado.
- [ ] Registrar evidências por match.

**Deliverables:** `property_listing_match`.

**Done Criteria:** match automático só ocorre acima do threshold definido no PRD.

### [ ] T5.4 — Validar amostra manual

**Subtasks:**

- [ ] Selecionar amostra de matches automáticos.
- [ ] Selecionar amostra de candidatos incertos.
- [ ] Medir falsos positivos aparentes.
- [ ] Ajustar limiar se necessário.

**Deliverables:** relatório de validação de deduplicação.

**Done Criteria:** threshold inicial é justificado por evidência mínima.

## [ ] Sprint 6 — Analytics API

**Goal:** expor dados agregados para dashboard e validação interna.

**Dependencies:** Sprint 4 e Sprint 5.

**Tasks:**

### [ ] T6.1 — Definir contratos de API

**Subtasks:**

- [ ] Endpoint de visão geral.
- [ ] Endpoint de mapa.
- [ ] Endpoint de séries temporais.
- [ ] Endpoint de detalhe de imóvel/anúncio.
- [ ] Endpoint de qualidade operacional.

**Deliverables:** contratos OpenAPI planejados.

**Done Criteria:** frontend pode ser construído contra contratos claros.

### [ ] T6.2 — Criar agregações por região

**Subtasks:**

- [ ] Contagem por bairro.
- [ ] Preço médio, mediano e dispersão.
- [ ] Separação por venda/aluguel.
- [ ] Filtros por período, tipo e status.

**Deliverables:** consultas ou views analíticas.

**Done Criteria:** métricas principais do dashboard são calculáveis.

### [ ] T6.3 — Criar séries temporais

**Subtasks:**

- [ ] Série de estoque.
- [ ] Série de preço médio/mediano.
- [ ] Série de mudanças de preço.
- [ ] Série por bairro e transação.

**Deliverables:** endpoints/queries de séries.

**Done Criteria:** evolução temporal pode ser renderizada sem processamento pesado no frontend.

### [ ] T6.4 — Criar testes de API e agregação

**Subtasks:**

- [ ] Testar filtros.
- [ ] Testar métricas com fixture pequena.
- [ ] Testar casos sem dados.
- [ ] Testar separação venda/aluguel.

**Deliverables:** testes de integração.

**Done Criteria:** agregações são verificáveis e não dependem de inspeção manual.

## [ ] Sprint 7 — Dashboard MVP

**Goal:** entregar interface analítica de exploração imobiliária.

**Dependencies:** Sprint 6.

**Tasks:**

### [ ] T7.1 — Criar shell do dashboard

**Subtasks:**

- [ ] Definir layout principal.
- [ ] Criar navegação mínima.
- [ ] Criar estado global de filtros.
- [ ] Separar venda e aluguel de forma evidente.

**Deliverables:** primeira tela do app.

**Done Criteria:** usuário acessa dashboard sem landing page intermediária.

### [ ] T7.2 — Criar filtros analíticos

**Subtasks:**

- [ ] Filtro por bairro.
- [ ] Filtro por tipo de imóvel.
- [ ] Filtro por período.
- [ ] Filtro por faixa de preço.
- [ ] Filtro por status.

**Deliverables:** controles de filtro.

**Done Criteria:** filtros alteram consultas e estado da tela.

### [ ] T7.3 — Criar mapa

**Subtasks:**

- [ ] Renderizar pontos de imóveis/anúncios.
- [ ] Renderizar camada de densidade quando viável.
- [ ] Exibir legenda e precisão geográfica.
- [ ] Diferenciar venda e aluguel.

**Deliverables:** mapa geográfico.

**Done Criteria:** usuário enxerga concentração espacial e pode explorar regiões.

### [ ] T7.4 — Criar cards e séries

**Subtasks:**

- [ ] Cards de contagem, média, mediana e dispersão.
- [ ] Série de estoque.
- [ ] Série de preço.
- [ ] Série de alterações de preço.

**Deliverables:** métricas visuais.

**Done Criteria:** dashboard responde às perguntas principais do PRD.

### [ ] T7.5 — Criar painel operacional

**Subtasks:**

- [ ] Mostrar último run.
- [ ] Mostrar status e volume.
- [ ] Mostrar falhas recentes.
- [ ] Mostrar campos críticos ausentes.

**Deliverables:** visão de saúde da base.

**Done Criteria:** operação sabe se dados estão atuais e confiáveis.

## [ ] Sprint 8 — Quality, Deploy and Observability

**Goal:** preparar MVP para operação controlada.

**Dependencies:** Sprint 7.

**Tasks:**

### [ ] T8.1 — Containerizar serviços

**Subtasks:**

- [ ] Definir containers de backend, frontend e banco.
- [ ] Definir volumes e variáveis de ambiente.
- [ ] Definir perfil local e produção simples.

**Deliverables:** Docker Compose.

**Done Criteria:** stack sobe localmente com comando documentado.

### [ ] T8.2 — Criar scheduler de coleta

**Subtasks:**

- [ ] Configurar execução diária.
- [ ] Registrar falha e sucesso.
- [ ] Evitar execução concorrente acidental.
- [ ] Permitir execução manual controlada.

**Deliverables:** job agendado.

**Done Criteria:** coleta roda sem intervenção manual e gera run auditável.

### [ ] T8.3 — Implementar observabilidade mínima

**Subtasks:**

- [ ] Logs estruturados.
- [ ] Health check do backend.
- [ ] Métricas de coleta.
- [ ] Alerta simples para falha de run.

**Deliverables:** painel/log operacional mínimo.

**Done Criteria:** falhas principais são detectáveis sem abrir o banco manualmente.

### [ ] T8.4 — Criar documentação operacional

**Subtasks:**

- [ ] Documentar setup local.
- [ ] Documentar comandos de validação.
- [ ] Documentar execução manual de coleta.
- [ ] Documentar troubleshooting básico.

**Deliverables:** README ou docs operacionais.

**Done Criteria:** novo operador consegue rodar e validar o MVP.

## [ ] Sprint 9 — ML Dataset and Baseline

**Goal:** preparar precificação preditiva sem acoplar ao produto pago.

**Dependencies:** Sprint 8 e histórico mínimo coletado.

**Tasks:**

### [ ] T9.1 — Definir dataset de treino

**Subtasks:**

- [ ] Definir alvo para venda e aluguel.
- [ ] Definir features obrigatórias.
- [ ] Definir filtros de qualidade.
- [ ] Definir split temporal.

**Deliverables:** especificação do dataset ML.

**Done Criteria:** dataset é reproduzível e rastreável.

### [ ] T9.2 — Gerar baseline estatístico

**Subtasks:**

- [ ] Criar baseline por bairro/tipo/área.
- [ ] Medir MAE, RMSE e MAPE.
- [ ] Medir erro por faixa de preço.
- [ ] Registrar limitações.

**Deliverables:** relatório baseline.

**Done Criteria:** modelo futuro precisa superar baseline documentado.

### [ ] T9.3 — Treinar primeiro modelo tabular

**Subtasks:**

- [ ] Treinar regressão inicial.
- [ ] Comparar com baseline.
- [ ] Versionar modelo e métricas.
- [ ] Documentar segmentos onde falha.

**Deliverables:** modelo offline validado.

**Done Criteria:** modelo só avança se métrica justificar uso controlado.

## [ ] Sprint 10 — Prediction API and SaaS Preparation

**Goal:** preparar monetização futura por tokens depois de ML validado.

**Dependencies:** Sprint 9.

**Tasks:**

### [ ] T10.1 — Especificar API de predição

**Subtasks:**

- [ ] Definir input de imóvel.
- [ ] Definir output de estimativa, intervalo e versão.
- [ ] Definir erros de validação.
- [ ] Definir limites de uso.

**Deliverables:** contrato de inferência.

**Done Criteria:** frontend e billing podem depender de contrato estável.

### [ ] T10.2 — Modelar autenticação e usuários

**Subtasks:**

- [ ] Definir papéis iniciais.
- [ ] Definir modelo de usuário.
- [ ] Definir autenticação recomendada.
- [ ] Definir proteção das rotas pagas.

**Deliverables:** especificação auth.

**Done Criteria:** SaaS futuro tem fronteira de acesso clara.

### [ ] T10.3 — Modelar tokens e ledger

**Subtasks:**

- [ ] Definir wallet.
- [ ] Definir transações de crédito e débito.
- [ ] Definir regra de não debitar em falha técnica.
- [ ] Definir auditoria.

**Deliverables:** especificação de tokens.

**Done Criteria:** cobrança por inferência é auditável e reversível quando necessário.

### [ ] T10.4 — Planejar billing

**Subtasks:**

- [ ] Escolher gateway.
- [ ] Definir pacotes de tokens.
- [ ] Definir callback/webhook.
- [ ] Definir conciliação de pagamento.

**Deliverables:** plano de billing futuro.

**Done Criteria:** monetização pode ser implementada sem redesenhar domínio principal.

## Cross-Sprint Traceability

| PRD Area | Sprint Coverage |
|---|---|
| Source validation | Sprint 1 |
| Data model | Sprint 2 |
| Scraping productionization | Sprint 3 |
| Historical price and availability | Sprint 4 |
| Unique property and deduplication | Sprint 5 |
| Analytics API | Sprint 6 |
| Dashboard MVP | Sprint 7 |
| Deploy and observability | Sprint 8 |
| ML preparation | Sprint 9 |
| SaaS and tokens | Sprint 10 |

## Global Definition of Done

- Task possui dependência clara.
- Task gera entregável verificável.
- Código futuro acompanha teste adequado ao risco.
- Mudança preserva rastreabilidade de dados.
- Dados brutos nunca são sobrescritos.
- Requisitos do PRD continuam refletidos no backlog.
- Ambiguidades novas são registradas no PRD antes de implementação.
