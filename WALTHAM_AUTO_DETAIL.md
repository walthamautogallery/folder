# 🚗 Waltham Auto Detail — Memória do Projeto

> **Palavra-chave de ativação: "detail"** — quando o usuário disser "detail",
> carregue este arquivo e continue o projeto exatamente de onde parou.
> Última atualização: 2026-07-29 · Owner: admin@walthamautogallery.com

---

## 🎯 O que é

Criar **Waltham Auto Detail** — um negócio/marca de detalhe automotivo, como
**braço (DBA)** da **Lehnen & Ristov LLC** (mesma empresa da Waltham Auto Gallery).
**Não é empresa nova.** Mesmo EIN, banco, QuickBooks e seguro.

---

## ✅ Decisões travadas

### Estrutura legal
- **DBA "Waltham Auto Detail"** sob a **Lehnen & Ristov LLC**.
- Único passo formal: **Business Certificate (DBA)** no **City Clerk de Waltham**
  (~$30–65, presencial/online, vale 4 anos).
- Avisar a seguradora do novo endereço/operação (mesma apólice da LLC).

### Local — 38 Felton St, Waltham, MA
- Aluguel **$3.000/mês**. **Semipronto + já com permits.** ✅
- Zona **industrial/flex** — correta para detalhe (descarte de água exige isso).
- Tamanho estimado ~1.200–1.450 SF (1–2 baias) pelo comp de mercado (~$25–29/SF/ano).
- **Veredito: bom negócio** (baia permitida e semipronta em Waltham por $3k é justo/barato).
- **Due diligence pendente (amarrar no contrato):**
  1. Os permits cobrem **"motor vehicle detailing/service"** (não só "commercial")?
  2. Existe **separador óleo/água** / dreno ligado ao esgoto? (runoff não pode ir p/ storm drain — regra MassDEP/Waltham).
  3. Elétrica **200A** + água quente (extrator, politriz, compressor, steamer).
- ⚠️ **Concorrência no mesmo corredor:**
  - **A-List Auto Detailing** — 42 Felton St, Unit 3 (porta ao lado!)
  - **JV Auto Detailing** (a da tabela de preços) — Waltham, @jv.autodetailing
  - A R Auto Detailing, Absolute Auto Detail — também Waltham.
  - Campo de batalha = **Google Business Profile + reviews**, mais que o site.

### Nome / marca
- **"Waltham Auto Detail"** — confirmado. Forte p/ **SEO local + GEO**: é o match
  exato da busca "waltham auto detail" e coloca acima dos "X Auto Detail" concorrentes.
- Cola na marca-mãe **Waltham Auto Gallery** (cruzamento de clientes: todo carro
  vendido na Gallery é lead do Detail).

### Site + operação
- **Site feito no GHL (GoHighLevel):** site + agenda + CRM + automações
  (missed-call text-back, lembrete de agendamento, **pedido automático de review**).
- Mapear o domínio **walthamautodetail.com** por cima do GHL.
- Site estático do repo (`index.html` / gerador de folder) fica **opcional**.

### Fluxo do dinheiro
- **QuickBooks = fonte da verdade do dinheiro.** GHL cuida do que **não é** dinheiro.
- Cliente fecha no GHL → **QB cobra** (payment link remoto + **GoPayment** presencial)
  → **GHL↔QBO sincroniza** cliente e status de pago.
- Regra de ouro: **um só sistema cobra**, pra não dobrar receita nos livros.

---

## 💵 Tabela de preços (base JV, corrigida Car < SUV < Truck)

| Serviço        | Car    | SUV    | Truck  |
|----------------|--------|--------|--------|
| Mini Detail    | $160   | $180   | $200   |
| Full Interior  | $300   | $350   | $400   |
| Full Exterior  | $300   | $350   | $400   |
| Full Detail    | $400   | $450   | $500   |
| **Platinum**   | $1.000 | $1.150 | $1.200 |

- **Ceramic Pro:** pacotes de **$599 a $3.500** (sob orçamento por veículo).
- **PPF:** de **$650 a $8.000** (sob orçamento por veículo).

---

## 🧾 QuickBooks — plano de execução

> **Bloqueio atual:** as chamadas ao QB retornam `requires approval`. Não é falta
> de acesso à API (o app da Intuit existe) — é a **permissão do conector no Claude**
> que está em "perguntar" e o pop-up não sobe. Destravar: Configurações de conectores
> → QuickBooks (Intuit) → **allow/ativado**. Depois é só mandar "pode tentar".

Quando liberar, criar dentro do **mesmo** arquivo QB (NÃO abrir company nova):
1. **Class tracking = ON** → classes `Auto Gallery` e `Auto Detail`.
2. **Products/Services** dos serviços da tabela → conta de receita **"Detailing Revenue"**.
3. Aluguel $3k/mês → despesa **Rent** marcada na classe `Auto Detail`.
4. Invoices/Estimates do detalhe → serviço + classe `Auto Detail`.

---

## 🌐 Domínio & redes (registrar já)
- **walthamautodetail.com** — sem site ativo (bom sinal). Confirmar disponibilidade
  no GoDaddy/Namecheap e **registrar**. (WHOIS não roda neste ambiente — proxy bloqueia.)
- **@walthamautodetail** no Instagram e Facebook — aparentam livres; garantir os dois.

---

## 📋 Próximos passos (TODO)

- [ ] Registrar **walthamautodetail.com** + **@walthamautodetail** (IG/FB).
- [ ] Abrir **Google Business Profile** no 38 Felton St → **maior retorno agora**
      (escrever descrição, categorias e serviços com preços — texto a produzir).
- [ ] Liberar permissão do **conector QuickBooks** no Claude → criar classes + serviços.
- [ ] Filiar o **DBA** no City Clerk de Waltham.
- [ ] Due diligence do imóvel: permits (uso), separador óleo/água, elétrica 200A.
- [ ] Montar **site no GHL** + mapear domínio.
- [ ] Escrever **texto do Google Business Profile**.

---

## 🔌 Acessos disponíveis nesta conta
GitHub (repo `walthamautogallery/folder`, GitHub Pages) · QuickBooks (Intuit) ·
Buffer (social) · Gmail · Google Calendar · Google Drive · GoHighLevel (externo, do usuário).
